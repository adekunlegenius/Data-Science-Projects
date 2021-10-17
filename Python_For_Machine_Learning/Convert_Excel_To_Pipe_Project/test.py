from datetime import *
from os import terminal_size
import numpy
import pandas as pd 
import re
if None:
    print('Helo world')
else:
    print('Helo world else')
print('Helo world')
print(None)
print('          Park well'.strip())
# data = {'name':'kunle'}


# text_formated = open('.\sheet1.txt', 'w')
# pipe_sep_string = 'Writing test.............'
# temp = text_formated.write(pipe_sep_string)
# if temp:
#     print('Successfuly written text', temp)
# else:
#     print('writting failed')

print('-------------------------------------------------')

print('WHERE EVER YOU GO'.lower())

print("god's presence is everywhere".upper())
# if '':
#     print(data)
#     print('you can also do bool test')
# else:
#     print('this is not good bool test')

print('-------------------------------------------------')
# test_data = pd.read_excel("./Test.xlsx", parse_dates=["date_strings"], index_col=None, dtype=object, sheet_name='Sheet2')
# test_data_keys = list(test_data)
# print(len(test_data_keys))
# print(test_data_keys)
# print(test_data)
# date_test = DateFormated('2021-08-12')
# print(date_test.get_date_string_with_last_day())
# print(get_date_name('2021-08-31').month)
# if len(test_data_keys) > 1:
#     for sheet_name in test_data_keys:
#         #if test_data[sheet_name] == None: 
#         path = "./" + sheet_name + '.txt'
#         #write_to_text(path, test_data[sheet_name])
#         #print(test_data[i])
#         print(test_data[sheet_name].to_csv(sep='|', index=False, header=False))
# else:
#     #print(test_data[test_data_keys[0]]) 
#     test_data[8]= '30-Sep-2021'       
#     test_data.to_csv('.\Test.csv', sep='|')
#     pass
#print(test_data)

# test_string = '003 Sub standard'
# print(str(3).lower())
# if re.search("sub", str(test_string).lower()) != None:
#     print(test_string)
#     re.search('sub', test_string)
#     print('POWER'.upper())
# else:
#     print('002')
# global day_month_feb ; day_month_feb=list(range(1, 29))
# #print(date.today())
# print(day_month_feb)
# message = [{'green':'message1'}, {'green':'meassage2'}]
# for diction in message:
#     for k, v in diction.items():
#         print(k, v)

test = [4, 5, 6, 7, 8, 19]

print(str(test.index(19)+1).zfill(2))

print(str(test[5]).zfill(2))