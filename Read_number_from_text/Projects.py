
def basicCukes(basicpath):
    """This function reads the basic.txt file which contains 
    the basic cupcakes into lists by grouping them into weeks."""
    basic = []
    basicInt = []
    tempList = []
    text = open('files/Basic.txt', "r")
    basic = text.readlines()
    length = len(basic)
    for i in range(length):
        temp = int(basic[i])
        tempList.append(temp)
        if len(tempList) == 7:
            basicInt.append(tempList)
            #print(tempList)
            tempList = []
    basicInt.append(tempList)

    return basicInt

# print(basicInt)

def deluxCupcakes(path):
    """This function reads the delux.txt file which contains 
    the delux cupcakes into lists by grouping them into weeks."""
    delux = []
    deluxInt = []
    tempList = []
    text = open('files/Delux.txt', "r")
    delux = text.readlines()
    length = len(delux)
    for i in range(length):
        temp = int(delux[i])
        tempList.append(temp)
        if len(tempList) == 7:
            deluxInt.append(tempList)
            #print(tempList)
            tempList = []
    deluxInt.append(tempList)

    return deluxInt

def total_list_grouped_by_week():
    """This groups total price by week"""
    total = []
    totalInt = []
    tempList2 = []
    text2 = open("Totals.txt", "r")
    total = text2.readlines()
    length_total = len(total)
    for i in range(length_total):
        temp = int(total[i])
        tempList2.append(temp)
        if len(tempList2) == 7:
            totalInt.append(tempList2)
            #print(tempList)
            tempList2 = []
    totalInt.append(tempList2) 

    return totalInt

#print(totalInt)
#print(tempList2)

def sum_of_list(list):
    sum = 0
    for i in range(len(list)):
        sum += list[i]

    return sum

def weeklyRevenueTotals(list): 
    weeklyRevenueTotal = []
    for i in range(len(list)):
        weeklyRevenueTotal.append(sum_of_list(list[i]))
    return weeklyRevenueTotal

getWeeklyRevenue = weeklyRevenueTotals(total_list_grouped_by_week())
print(getWeeklyRevenue)

def formatPrinting():
    pass