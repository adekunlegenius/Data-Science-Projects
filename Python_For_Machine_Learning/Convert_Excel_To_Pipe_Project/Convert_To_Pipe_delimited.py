
import numpy
import pandas as pd 
from datetime import *
from DateFormated import DateFormated
# import os
#class ExcelFile:

 #   def __init__(self, file_path):


def get_file_extension(path):
    extension = path.split('.')[-1]
    return extension.tolower()

def read_excel_file(path):
    data = pd.read_excel(path, sheet_name=None, index_col =None)
    return data

def get_dict_keys(dict_Obj):
    keys = list(dict_Obj)
    return keys

def get_column_heads(data_frame_Obj):
    heads = list(data_frame_Obj.columns.values) 
    return heads

def get_num_of_rows(data_frame_Obj):
    return len(data_frame_Obj)

def write_to_text(path, frame_Obj):
    pipe_sep_string = frame_Obj.to_csv(sep='|', index=False, line_terminator ='\n')
    #print(pipe_sep_string)
    text_formated = open(path, 'w')
    text_formated.write(pipe_sep_string, )
    text_formated.close()

def get_text_file_name(subID, frame_Obj, last_date_str):
    if len(get_column_heads(frame_Obj)) == 46:
        return sub + '-' + 'Individual-Borrower' +'-' + last_date_str
    elif len(get_column_heads(frame_Obj)) == 29:
        return sub + '-' + 'Credit-Information' +'-' + last_date_str
    elif len(get_column_heads(frame_Obj)) == 20:
        return sub + '-' + 'Corporate-Borrower' +'-' + last_date_str
    elif len(get_column_heads(frame_Obj)) == 41:
        return sub + '-' + 'Principal-Officers' +'-' + last_date_str
    elif len(get_column_heads(frame_Obj)) == 22:
        return sub + '-' + 'Guarantors-Information' +'-' + last_date_str
    else:
        return ''

# def get_date_name(date_string):
#     date_Obj = date.fromisoformat(date_string)
#     return date_Obj


test_data = read_excel_file('.\Test.xlsx')
test_data_keys = get_dict_keys(test_data)
print(len(test_data_keys))
print(test_data_keys)

date_test = DateFormated('2021-08-12')
print(date_test.get_date_string_with_last_day())
#print(get_date_name('2021-08-31').month)
# if len(test_data_keys) > 1:
#     for sheet_name in test_data_keys:
#         path = "./" + sheet_name + '.txt'
#         write_to_text(path, test_data[sheet_name])
#         #print(test_data[i])
#         #print(test_data[i].to_csv(sep='|'))
# else:
#     print(test_data[test_data_keys[0]])        
#test_data.to_csv('.\Test.csv', sep='|')
#print(test_data)

test = {'a':'abc','b':'adcde'}
#print(str(os.linesep))
#print(len(test))
#print(len(test_data))
#print(list(test_data))
#print(test_data['Name'])
#print(test_data[1])