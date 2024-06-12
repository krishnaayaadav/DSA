# loops 
import random

""" loops are use to perform certain task at certain time or while certain condition is true"""


# for loop , while


company_employees_count = 5000


def calculate_salary():
    return random.randint(a=10000, b=90000)


# for loop

def all_employee_salry(emp_count):
    for i in range(0, emp_count):
        print(calculate_salary())


# all_employee_salry(10)


def print_table(number:int):

    for i in range(1, 11): # range from 1-to-11 1,2,3,4,5,6,7,8,9,10

        print(f'\n{i}*{number} =: {i*number}')

# print_table(2)


# while loop
""" while loop is used to perform certain task/actions while(jab tak) given condition is true """
message="Welcome to Python Programming"
def greet(message):
    print(message)
    return message
    
auth_status = True

count = 0

while auth_status == True:

    greet(message + f' {count}' )
    count  += 1