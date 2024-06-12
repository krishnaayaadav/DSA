
# person class 
class Person:

    # constructor here 
    def __init__(self, name, age, address):
        # properties here
        self.name  = name
        self.age   = age
        self.address = address
    

    # get-details method
    def get_details(self):

        return {
            'name': self.name,
            'age': self.age,
            'address': self.address
        }

p1 = Person(name='Krishna', age=24, address='Jalandhar, Punjab')

# access properties here

name = p1.name
age  = p1.age
address = p1.address


details= p1.get_details()

print(details)


#  student class  inheritance here

class Student(Person):

    def __init__(self, name, age, address, course, university):
        # calling the parent constructor
        super().__init__(name, age, address)

        self.course  = course
        self.university = university
    
    # method overrding
    def get_details(self):
        return {
            'name': self.name,
            'age': self.age,
            'address': self.address,
            'course': self.course,
            'university': self.university
        }
    

s1 = Student(name='Krishna yadav', age=24, address='Jalandhar, Punjab', course='B.Tech', university='Lovely Professional University')

print(s1.get_details())
