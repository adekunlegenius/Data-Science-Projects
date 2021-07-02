print("Hello World")

print('*'*10)

def add (num1, num2):
    return num1 + num2

def mult (num1, num2):
    return num1 * num2

def div (num1, num2):
    return num1 / num2

def sqr (num1, num2):
    return num1 / num2


print("This is a Simple Calculator")
print("For addition enter add")
print("For multiplication enter multiply")
print("For division enter division")
print("For division enter square")
print("For square root enter 4")
print("To exit press quit")

while(True):
    entry = input("Enter your desired operation: ")

    if entry  == 'add':
        result = add(float(input('Enter the first num: ')), float(input("Enter the second num: ")))
        print(result)
    elif entry =='multiply':
        result = mult(float(input('Enter the first num: ')), float(input("Enter the second num: ")))
        print(result)
    elif entry =='square':
        result = float(input('Enter the num: '))**2
        print(result)   
    elif entry =='division':
        result = div(float(input('Enter the first num: ')), float(input("Enter the second num: ")))
        print(result)
    elif entry == 'quit':
        break
    else:
        print("Invalid Input. Please enter the correct input")

