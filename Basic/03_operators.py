# Operators
"""
 Operators are special sysmbols which are used to perform special operations as per the symbols that we are using

 Types of operators in python:
 
 1. Arithmetic Operators
 2. Assignment Operators
 2. Comparision Operators
 4. Logical Operators
 5. Membership Operators
 6. Identity Operators
 7. Bitwise operators

"""

#  Arithmetic operators
num1, num2 = 23, 34

total_sum = num1 + num2

print(total_sum)

# divsion 

result = total_sum /2
print(result)

# // floor division

result = total_sum // 2
print(result)

# exponent

result = total_sum ** 3 # 57 * 57 * 57
print(result)

# 2. Assignment Operators 

marks = 22 

marks +=10 # addition then assignment marks = marks + 10

print(marks)

# Comparision Operators

if(num1 > num2):  # 23 > 34: 23 is greater than 34 = false

    print(num1, 'is greater')

else:
    print(num1, 'is less')

# equal to

if(num1 == num2):
    print('both are equal')

else:
    print('both are not equal')

if(num1 != num2):
    print('both are not equal')


#  Logical Operators

username = ''

password = "sompasssword123"
is_authenticated = False

if(username and password):
    # now perform authentication validations
    is_authenticated = True
    print('Yes user is authenticated because username and password both exists')

age  = 24

if(age >= 25 or is_authenticated):
    print('Yes your eligible for job')

else:
    print('Soory  your  not celigible for job')


has_voter_id = False

if(is_authenticated or has_voter_id):
    print('Yes can  the Vote')

else:
    print('Soooryyy can not  the Vote')



# Membership Operators

name = 'krishna'

student_names= ['krishna', 'aisha', 'karan', 'amul']

if(name in student_names):
    print(f'Yes name exists in student_names list: {student_names}')

# Identity Operators

user_password = 'krishna123'
db_password   = 'Krishna123'

if(user_password is db_password):
    print('Yes both password are exactly same')

else:
    print('No both password are not  same')



# bitwise operators in python 

"""Bitwise operators are use to perform opertation on bits. that means if we have number so number will first convereted in binary format as o and 1 that the bitwise operations are performed"""

marks1 = 52
marks2 = 48


result  = marks1 & marks2
print(result)

result = marks1  | marks2

result = marks1 ^ marks2

print(result)

