
def split_date():
    """This function reads the date_concat.txt file which contains 
    the date string to be formatted."""
    basic = []
    dateFormatedList = []
    text = open('files/date_concat_fidelity_ind_may_2021.txt', "r")
    basic = text.readlines()
    length = len(basic)
    for i in range(length):
        temp = str(basic[i])  
        if temp != "NULL\n":
            temp = temp[0:4] + "-" + temp[4:6] + "-" + temp[6:]
            dateFormatedList.append(temp)
            #print(tempList)
            temp=""
        else:
            dateFormatedList.append(temp)
            temp=""
    date_formatted = open("date_formatted_fidelity_ind_may_2021.txt", "w")
    for i in range(length):
        date_formatted.write(dateFormatedList[i])
        

    #return basicInt
split_date()
