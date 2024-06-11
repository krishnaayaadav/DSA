
# Conditional Statements 
""" Conditional statements are use perform certain task based on condition if certain condition is true then we will perform the certain operations otherwise not """


class Person:

    def __init__(self, age:int, name:str):
        self.age = age
        self.name = name
    

    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
class VoterHanlder:

    def __init__(self,age:int):
        self.age = age
    

    def is_eligible_for_vote(self, age=0):
        status = False

        if not age:
            age = self.age
        
        if age >= 21:
            status = True
        
        return status





# age = int(input('Enter your age: '))
# has_voter_id = bool(input('Do you have voter id: '))

def can_give_vote(age, has_voter_id):
        
    if(age >= 21): 

        if(has_voter_id == True):

            print(f'Yes you can give the Vote')
        
        else:
            print('Please make your Vote id to give Vote')

    else:
        print('Soooory your are not eligible for Vote')



is_authenticated = False

def user_dashboard():
    print('\n Welcome to dasboard ')

def user_login():
    print('\n Please login first to visit the dashboard')



if(is_authenticated == True):
    user_dashboard()

else:
    user_login()