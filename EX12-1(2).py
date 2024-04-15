# Amanda Hinnerichs
# April 11, 2024
# EX12-1
# A simple calculator that asks for user input and makes the calculation

#Functions++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def add(a,b):
    c=a+b
    return(c)

def sub(b,a):
    c=b-a
    return(c)

def multi(a,b):
    c=a*b
    return(c)

def div(a,b):
    c=a/b
    return(c)

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++



#main======================================================================================
print("Simple Calculator 12.1")


first = int(input("\nEnter the first number "))
second = int(input("Enter the second number "))


# call functions to perform calculations using the input from the user
sum = add(first,second)
print(f'\n{first} + {second} = {sum}')


minus = sub(first,second)
print(f'\n{second} - {first} = {minus}')


times = multi(first,second)
print(f'\n{first} * {second} = {times}')


division = div(first,second)
print(f'\n{first} / {second} = {division}')
