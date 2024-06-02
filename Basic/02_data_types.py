"""

  Data-types: 

    is way of classification of data into different classes or categorization of data into different categories.
    So that we get know what are different operations which can be performed on particular data-sets.

    Major data types in Python are:

    1. String
    2. Integer
    3. Float
    4. Booleans
    5. List
    6. Tuples
    7. Dictionary
    8. Sets
    9. Complex numbers


"""

# 1. String

username = 'krish'

sir_name = 'yadav'

email = 'krishna123@gmail.com'

university_name = 'LPU'

job_role = 'Fullstack Django Developer'

# 2. Integer

stu_id = 344545

emp_id = 4059405

stu_rol = 34

pincode = 456568

country_code = 91


# 3. Float

stu_marks = 89.9

salary = 850000.5

total_sum = 7895.3445


# 4. Booleans

is_passed = True

is_checked = False

is_eligible = True

# 5. Lists

student_names = ['krishna', 'aman', 'karan', 'ayush', 'nisha', 'aisha', 'atul']

# access list elements

print(
    student_names[0],  # first elements
    student_names[-1], # last elements 
    student_names[2]
      )


# updation
student_names[0] = 'Krishna Yadav'
student_names[-1] = 'Atul Singh'

print(student_names[0])

# remove/deletion
student_names.remove('nisha')
print(student_names, student_names.pop(0), student_names)

# add new elements using append and extends methods

student_names.append('Ankit')
print(student_names)

names2 = ['Anita', 'Lalit', 'Sonu']

student_names.extend(names2)
print(student_names)

print(student_names[0:4]) # slicing from 0 to 4 index

print(student_names[-5:-1]) # reverse slicing


# 6. Tuples

employee_names =  ('krishna', 'aman', 'karan', 'ayush', 'nisha', 'aisha', 'atul')

status_types = (
    ('passed', 'Pass'),
    ('fail', 'Failed'),
)

# 7. Dictionary

student_detail = {
    
    'name': 'krishna yadav',
    'roll': 51,
    'id': 11312334,
    'course': 'CSE',
    'university': 'Lovely Professional University'
}

# access 
name = student_detail['name']
course = student_detail['course']
id     = student_detail['id']

print(id, name, course)

# update

student_detail['name'] = 'Krishna Kumar'
student_detail['id']   = 132221
student_detail['roll'] = 75

# deletion

print(student_detail.pop('id'))


# 8. Sets 

departments = {'CSE', 'Civil', 'Mechanic'}

departments.add('Electrical')

departments.pop()

print(departments)

# 9. Complex Numbers

eqaution  = 2j  + 45