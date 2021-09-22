
def add_zero_to_account():
    """This function reads the deprecated account no file, calls a function that appends the truncated  
    zeros and then write the result in another file."""
    basic = []
    accountCorrectedList = []
    text = open('files/truncated_account.txt', "r")
    basic = text.readlines()
    length = len(basic)
    for i in range(length):
        temp = str(basic[i])   
        accountCorrectedList.append(add_lending_zeros(temp, 11))
              
    account_formatted = open("account_corrected.txt", "w")
    for i in range(length):
        account_formatted.write(accountCorrectedList[i])

def add_zero_to_customer_id():
    """This function reads the deprecated customer_id no file, calls a function that appends the truncated  
    zeros and then write the result in another file."""
    basic = []
    customerIdCorrectedList = []
    text = open('files/truncated_account.txt', "r")
    basic = text.readlines()
    length = len(basic)
    for i in range(length):
        temp = str(basic[i])   
        customerIdCorrectedList.append(add_lending_zeros(temp, 11))
              
    account_formatted = open("account_corrected.txt", "w")
    for i in range(length):
        account_formatted.write(customerIdCorrectedList[i])

def add_lending_zeros(truncated, length):
    """ This function adds lending zero to a string of numbers with.
    the number as parameter and the length of the result number """
    diff = length - len(truncated)
    appended = truncated
    while diff>0:
        appended= "0"+ appended
        diff = diff - 1
    return appended


def format_file(path, actual_length, filename):
    """This function takes in the path of the file path reads, which contains the 
    deprecated numbers, as parameter. It also takes in the actual_length of each numbers in file as parameter.
    It calls a function that appends the truncated zeros and then write the result in filename."""
    basic = []
    customerIdCorrectedList = []
    text = open(path, "r")
    basic = text.readlines()
    length = len(basic)
    for i in range(length):
        temp = str(basic[i])   
        customerIdCorrectedList.append(add_lending_zeros(temp, actual_length+1))            
    account_formatted = open(filename, "w")
    for i in range(length):
        account_formatted.write(customerIdCorrectedList[i])


#format_file("files/truncated_ind_account.txt", 10, "ind_account_corrected.txt")
# format_file("files/truncated_ind_customerId.txt", 9, "ind_customerId_corrected.txt")
# format_file("files/truncated_corp_account.txt", 10, "corp_account_corrected.txt")
# format_file("files/truncated_corp_customerId.txt", 9, "corp_customerId_corrected.txt")

format_file("files/GTB_dud_cheque_truncated_ind_customer_id_08_21.txt", 10, "GTB_dud_cheque_corrected_ind_customer_id_08_21.txt")
format_file("files/GTB_dud_cheque_truncated_corp_customer_id_08_21.txt", 10, "GTB_dud_cheque_corrected_corp_customer_id_08_21.txt")
    
#print(add_lending_zeros("13456", 10))