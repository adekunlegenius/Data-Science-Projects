import collections
from datetime import *
import math
from os import terminal_size
#from typing import ChainMap
import numpy
import pandas as pd 
import tkinter
import re
# if None:
#     print('Helo world')
# else:
#     print('Helo world else')
# print('Helo world')
# print(None)
print('          Park well'.lstrip())
# data = {'name':'kunle'}

# def test(x:str)->int:
#     return int(x)
# test_map = list(map(lambda y: test(y), ['1', '2', '3', '4']))
# test_map2 = list(map(int, ['1', '2', '3', '4']))
#print([i for i in test_map])
#print(['1', '2', '3', '4'])
# rev = list(reversed(test_map))

# ziptest=zip([1,2,3], ["t", "v", "h"])
# print(*ziptest)
# print()
#print(*rev)
#print(*test_map)
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

# test = [4, 5, 6, 7, 8, 19]

# print(str(test.index(19)+1).zfill(2))

# print(str(test[5]).zfill(2))
# class Test:
#     def run(self):
#         global display_canvas
#         self.root = tkinter.Tk()
#         self.root.minsize(width=850, height=400)
#         display_canvas = tkinter.Canvas(self.root, height=125, width=700, borderwidth=4, background='white')
#         display_canvas.grid(row=10, padx=5, pady=20)
#         display_canvas.create_text(50, 80, text='Status:', tags='labels', fill='red')
#         display_canvas.create_text(65, 10, text='Status2:', tags='labels', fill='red')
#         display_canvas.create_text(70, 10, text='No file Choosen', tags=('labels'))
#         button = tkinter.Button(self.root, text='click', command=self.testcommand())
#         button.grid(row=20, column=0)
#         print(display_canvas.gettags('labels'))
#         self.root.mainloop()


#     def testcommand(self):
#         def callback():
#             if display_canvas.gettags('labels') != None:
#                 display_canvas.delete('labels')
#         return callback

# trytest = Test()
# trytest.run()

# print(*[{"va":1}, {"ba":2}])

# res = collections.ChainMap(*[{"va":1}, {"ba":2}])
# print(list(res.keys()))
# print(res['va'])
#print("key" in {"key":1, "value":2})
# testdic ={}
# testdic.update({"key":3})
# print(testdic)
# print("--------------")
# testdic.update({"key2":4})
#print(testdic)
def factorial(n):
    # Write your code here
    k= n
    if n<=0:
        return 1
    else:
        return n*factorial(n-1)
#print(factorial(3))
# if __name__ == "__main__":
    
#     n = int(input().strip())
#     if n<=0 or n>100000:
#         print("Invalid N input")
#     else:
#         phone_book = []
#         for i in range(n):
#             temp_input = input().rstrip().split()
#             phone_book.append({temp_input[0]:temp_input[1]})
#print(sum([1,2,3,4]))

#Prime numbers
def primeNumbers(n):
    prime_numbers=[]
    for k in range(1, n+1):
        #print("k First for",k)
        if k>1:
            if k ==2:
                prime_numbers.append(k)
                #print("prime_numbers:",prime_numbers)
            else:
                i = 2
                while i <k:
                    #print("i: second for",i)
                    if k%i ==0:
                        break
                    else:
                        if i ==k-1:
                            #print("k second for",k)
                            prime_numbers.append(k)
                            #print("prime_numbers second for:",prime_numbers)
                    i = i+1
    return prime_numbers
def divisorSum( n):
        
        num_divisor =  primeNumbers(1000) #[2, 3, 5, 7, 11, 13, 17, 19, 23,29,31,37,41,47,53,59,61,67,71, 73,79,83,89,97,101,103,107,109,113] #prime numbers divisors
        divisor_list = [1]
        temp_quotient = n
        i = 0
        if temp_quotient in num_divisor:
            divisor_list.append(temp_quotient)
        else:
            while(i<len(num_divisor) and temp_quotient!=1):
                
                # print("i:",i)
                # print("temp_quo:",temp_quotient)
                # print(num_divisor[i])
                while(temp_quotient%num_divisor[i]==0):
                    new_temp_fact = list(map(lambda x: x*num_divisor[i], divisor_list)) #[x*num_divisor[i] for x in divisor_list] --list comprehension
                    #print(new_temp_fact)
                    for j in new_temp_fact:
                        if j in divisor_list:
                            pass
                        else:
                            #print("j:",j)
                            divisor_list.append(j)
                    temp_quotient = temp_quotient//num_divisor[i]
                i= i+1    
        print(divisor_list)    
        return sum(divisor_list)
#print(divisorSum(6))
# num = primeNumbers(1000000000)
# print(num)
print(int(math.sqrt(36)))
