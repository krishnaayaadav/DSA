

#  functions in python

"""Function is block of code whie use to perform certain task/actions.
   functions provide a functionality to write once and use as many times you want for different inputs or same

   To create a function we use def keywork

   example: 

    def function_name(parmas):
        body_of_the_function
  """


def say_hello():
    print('Hello ')


say_hello()
auth_status = False


def login(username, password):
    global auth_status
    if(username and password):
        print('You are logged in successfully')
        auth_status = True
    
    else:
        print('login failed')


login('krishna', 'password123')


def user_dashboard():
    print('Welcome to the dashboard') if auth_status == True else print('Logged in failed please login again...')

user_dashboard()

