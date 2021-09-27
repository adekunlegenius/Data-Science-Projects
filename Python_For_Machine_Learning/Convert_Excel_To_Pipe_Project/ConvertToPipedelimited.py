
from tkinter.constants import FALSE, TRUE
import numpy
import pandas as pd 
from datetime import *
from DateFormated import DateFormated
# import os
class ExcelFile:

    def __init__(self, file_path, subID, date):
        self.file_path =file_path
        self.subID = subID
        self.date = date

    def get_file_extension(self, path:str)->str:
        extension = path.split('.')[-1]
        return extension.lower()

    def read_excel_file(self):
        print('Execution reach here.... 1')
        print(self.file_path)
        print(self.get_file_extension(self.file_path) )
        if self.get_file_extension(self.file_path) == 'xlsx':
            print('Execution reach here.... 2')
            print(self.file_path)
            self.dict_data = pd.read_excel(self.file_path, sheet_name=None, index_col =None)
            print('Execution reach here.... 3')
            return self.dict_data
        elif self.get_file_extension(self.file_path) == 'xls':
            
            return
        else:
            raise ValueError('File extension error')
            

    def get_number_of_sheet(self)->int:

        return len(self.dict_data)


    def get_dict_keys(self, dict_Obj):
        keys = list(dict_Obj)
        return keys

    def get_column_heads(self, data_frame_Obj):
        heads = list(data_frame_Obj.columns.values) 
        return heads

    def get_num_of_rows(self, data_frame_Obj):
        return len(data_frame_Obj)

    def write_to_text(self, path, frame_Obj):
        pipe_sep_string = frame_Obj.to_csv(sep='|', index=False, line_terminator ='\n')
        #print(pipe_sep_string)
        text_formated = open(path, 'w')
        if text_formated.write(pipe_sep_string):
            text_formated.close()
            return TRUE
        else:
            return FALSE

    def get_text_file_name(self, subID, frame_Obj, last_date_str):
        if len(self.get_column_heads(frame_Obj)) == 46:
            return subID + '-' + 'Individual-Borrower' +'-' + last_date_str
        elif len(self.get_column_heads(frame_Obj)) == 29:
            return subID + '-' + 'Credit-Information' +'-' + last_date_str
        elif len(self.get_column_heads(frame_Obj)) == 20:
            return subID + '-' + 'Corporate-Borrower' +'-' + last_date_str
        elif len(self.get_column_heads(frame_Obj)) == 41:
            return subID + '-' + 'Principal-Officers' +'-' + last_date_str
        elif len(self.get_column_heads(frame_Obj)) == 22:
            return subID + '-' + 'Guarantors-Information' +'-' + last_date_str
        else:
            return ''


    def get_absolute_parent_path(self, path_name, sep='/')->str:

        path_list = path_name.split(sep)
        path_list.remove(path_list[-1])
        return sep.join(path_list)



    def write_to_file(self):
        write_message = []
        print('Writing Execution reach here.... 1')
        if self.get_number_of_sheet() != 0:
            print('Writing Execution reach here.... 2')
            for sheet_name in self.dict_data:
                formatted_date_Obj = DateFormated(self.date)
                formatted_date_str = formatted_date_Obj.get_date_string_with_last_day()
                text_file_name = self.get_text_file_name(self.subID, self.dict_data[sheet_name], formatted_date_str) #production code
                if text_file_name != '':
                    
                    write_path = self.get_absolute_parent_path(self.file_path) + '/' + text_file_name + '.txt'
                    if self.write_to_text(write_path, self.dict_data[sheet_name]):
                        message = text_file_name + ' Successfully generated'
                        write_message.append(message)
                    else:
                        message = 'An error was occurred while writing'+ text_file_name 
                        write_message.append(message)
                else:

                    # Test codes
                    #---------------------------------------------------------------------------
                    # text_file_name = self.subID + '-' + sheet_name + '-' + formatted_date_str
                    # write_path = self.get_absolute_parent_path(self.file_path) + '/' + text_file_name + '.txt'
                    # if self.write_to_text(write_path, self.dict_data[sheet_name]):
                    #     message = text_file_name + ' Successfully generated'
                    #     write_message.append(message)
                    # else:
                    #     message = 'An error was occurred while writing'+ text_file_name 
                    #     write_message.append(message)
                    #--------------------------------------------------------------------------
                    message = sheet_name + " could be converted to text because it contains " + str(len(self.get_column_heads(self.dict_data[sheet_name]))) + ' no. of columns. Kindly confirm and try again'
                    write_message.append(message)
                print('Writing complete')
            return write_message    
        else:
            message = 'No sheet in the excel file to convert'
            write_message.append(message)
            return write_message         
        


