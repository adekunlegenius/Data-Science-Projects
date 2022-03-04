
import numpy

import pandas as pd 

#from datetime import *
from tkinter.constants import *
from DateFormated import DateFormated
from TransformToCode import TransformToCode
# import os

class ExcelFile:

    def __init__(self, file_path:str, subID:str, date, restrict_status_date_check:bool):
        """Initialise the class variables which are: the path of the to be read in form of file_path; 
        the subscriber ID (subID); the date of the data"""
        
        self.file_path =file_path  
        self.subID = subID
        self.date = date
        self.restrict_status_date = restrict_status_date_check

    def get_file_extension(self, path:str)->str:
        """The function takes in path of the file and returns the extension of the file in lower case"""
        extension = path.split('.')[-1]
        return extension.lower()

    def read_excel_file(self, app_Obj):
        """Reads the Excel sheets into a dictionary with sheet name as the key and DataFrame as the value.
        The function makes use of the read_excel() function found in openxl library to read the excel file. If openxl was unable to
        read the file xldr library would be made use of. """
        print('Execution reach here.... 1')
        print(self.file_path)
        print(self.get_file_extension(self.file_path) )
        if self.get_file_extension(self.file_path) == 'xlsx':
            print('Reading file.')
            app_Obj.set('Reading file.')
            app_Obj.set('Reading file..')
            app_Obj.set('Reading file...')
            print(self.file_path)
            self.dict_data = pd.read_excel(self.file_path, sheet_name=None, header=None, dtype=object, index_col =None)
            app_Obj.set('Reading file....')
            print('Reading file....')
            return self.dict_data
        elif self.get_file_extension(self.file_path) == 'xls':
            print('Reading.... 2')
            print(self.file_path)
            self.dict_data = pd.read_excel(self.file_path, sheet_name=None, dtype=object, header= None, index_col =None)
            print('Execution reach here.... 3')
            return self.dict_data
        
        else:
            raise ValueError('File extension error')
            

    def get_number_of_sheet(self)->int:
        """Returns the number of sheets in the ExcelFile class dictionary property (dict_data)."""
        return len(self.dict_data)


    def get_dict_keys(self, dict_Obj):
        """Returns lists of the sheet names in the excel file read (i.e the keys in the property (dict_data)"""
        keys = list(dict_Obj)
        return keys

    def get_column_heads(self, data_frame_Obj):
        """"""
        heads = list(data_frame_Obj.columns.values) 
        return heads

    def get_num_of_rows(self, data_frame_Obj):
        return len(data_frame_Obj)

    def write_to_text(self, path, frame_Obj)->bool:

        if len(self.get_column_heads(frame_Obj)) == 29:
            transform_to_code_Obj = TransformToCode(frame_Obj)
            transform_to_code_Obj.change_acct_status_to_code()
            transform_to_code_Obj.change_loan_classification_to_code()
            transform_to_code_Obj.change_currency_to_code()
            if self.restrict_status_date:
                transform_to_code_Obj.change_account_status_date(DateFormated(self.date).get_date_string_with_day(sep='-'))
            else:
                transform_to_code_Obj.change_account_status_date(DateFormated(self.date).get_date_string_with_last_day(sep='-'))
            transform_to_code_Obj.reset_affected_column_heads()
            converted_frame = transform_to_code_Obj.frameObj
            print('Reach here,,,,,')
            pipe_sep_string = converted_frame.to_csv(sep='|', index=False, header=False, line_terminator ='\n')
        else:
            pipe_sep_string = frame_Obj.to_csv(sep='|', index=False, header=False, line_terminator ='\n')
        #print(pipe_sep_string)
        text_formated = open(path, 'w', encoding='utf-8')
        if text_formated.write(pipe_sep_string):
            text_formated.close()
            return TRUE
        else:
            return FALSE

    def get_text_file_name(self, subID, frame_Obj, date_str):
        if len(self.get_column_heads(frame_Obj)) == 46:
            return subID + '-' + 'Individual-Borrower' +'-' + date_str
        elif len(self.get_column_heads(frame_Obj)) == 29:
            return subID + '-' + 'Credit-Information' +'-' + date_str
        elif len(self.get_column_heads(frame_Obj)) == 20:
            return subID + '-' + 'Corporate-Borrower' +'-' + date_str
        elif len(self.get_column_heads(frame_Obj)) == 41:
            return subID + '-' + 'Principal-Officers' +'-' + date_str
        elif len(self.get_column_heads(frame_Obj)) == 22:
            return subID + '-' + 'Guarantors-Information' +'-' + date_str
        else:
            return ''


    def get_absolute_parent_path(self, path_name, sep='/')->str:
        """The function"""
        path_list = path_name.split(sep)
        path_list.remove(path_list[-1])
        return sep.join(path_list)



    def write_to_file(self, app_Obj)->list:
        write_message = []
        print('Writing Execution reach here.... 1')
        app_Obj.set("Writing to file")
        if self.get_number_of_sheet() != 0:
            print('Writing Execution reach here.... 2')
            for sheet_name in self.dict_data:
                formatted_date_Obj = DateFormated(self.date)
                formatted_date_str = formatted_date_Obj.get_date_string_with_day(year_first=TRUE)
                text_file_name = self.get_text_file_name(self.subID, self.dict_data[sheet_name], formatted_date_str) #production code
                print(text_file_name)
                print(self.get_column_heads(self.dict_data[sheet_name]))
                print(len(self.get_column_heads(self.dict_data[sheet_name])))
                if text_file_name != '':
                    
                    write_path = self.get_absolute_parent_path(self.file_path) + '/' + text_file_name + '.txt'
                    if self.write_to_text(write_path, self.dict_data[sheet_name]):
                        message = text_file_name + ' Successfully generated'

                        write_message.append({'green':message})
                        print('Writing complete')
                    else:
                        message = 'An error was occurred while writing'+ text_file_name 
                        write_message.append({'red':message})
                else:
                    print('Writing Execution reach here.... 3')
                    # Test codes
                    #---------------------------------------------------------------------------
                    # text_file_name = self.subID + '-' + sheet_name + '-' + formatted_date_str
                    # write_path = self.get_absolute_parent_path(self.file_path) + '/' + text_file_name + '.txt'
                    # print('Writing Execution reach here.... 4')
                    # if self.write_to_text(write_path, self.dict_data[sheet_name]):
                    #     message = text_file_name + ' Successfully generated'
                    #     write_message.append(message)
                    # else:
                    #     message = 'An error was occurred while writing'+ text_file_name 
                    #     write_message.append(message)
                    #--------------------------------------------------------------------------
                    message = sheet_name + " could not be converted to text because it contains " + str(len(self.get_column_heads(self.dict_data[sheet_name]))) + ' no. of columns. Kindly confirm and try again'
                    print(message)
                    write_message.append({'red':message})
                #print('Writing complete')
                #app_Obj.set("Writing complete! Text file successfully generated")
            return write_message    
        else:
            message = 'No sheet in the excel file to convert'
            write_message.append(message)
            return write_message         
        


