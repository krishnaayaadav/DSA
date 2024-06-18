
# Write a program to print numbers from 1 to 10.

def print_1_to_10(n=10):

    for i in range(0, n+1):
        print(i, end=' ')
    
    print()
    
print_1_to_10()

# Write a program to calculate the sum of first 10 natural number.
# natural numbers start from 1 to so ...

def sum_of_first_10_natural_number(n=10):
    total_sum = 0

    for i in range(1, n+1):
        total_sum += i
    
    print(total_sum)
    return total_sum

sum_of_first_10_natural_number()


# Write a program that prompts the user to input a positive integer. It should then print the multiplication table of that number. 


def print_table_of_user_input():

    # taking input from the user
    number = int(input('Enter number here: '))


    # print table
    for i in range(1, 11):

        print(f'{number}*{i} = {number*i}')


# print_table_of_user_input()


# Write a program to find the factorial value of any number entered through the keyboard. 

def print_factorial_of_user_input_number():

    number = int(input('Enter number here: '))

    factorial = 1

    for num in range(number, 0, -1):
        factorial *= num
    
    print(factorial)
    return factorial



# print_factorial_of_user_input_number()


# 5. Two numbers are entered through the keyboard. Write a program to find the value of one number raised to the power of another. (Do not use Java built-in method)


def raise_to_power():

    number = int(input('Enter number: '))
    power  = int(input('Enter raise to power: '))

    # n to p

    result = 1

    for i in range(1, power+1):
        result *= number
    
    return result

# print(raise_to_power())

# 6. Write a program that prompts the user to input an integer and then outputs the number with the digits reversed. For example, if the input is 12345, the output should be 54321.


def find_reverse_of_num():
    number = int(input('Enter number: '))
    reverse  = 0

    while number != 0:

        rem = number % 10
        reverse = reverse * 10 + rem
        number = number // 10
    
    return reverse

# print(find_reverse_of_num())


# 7. Write a program that reads a set of integers, and then prints the sum of the even and odd integers.


def sum_of_add_even():

    user_inputs = []

    take_input = True

    # take user inputs
    while take_input == True:
        try:
            number  = int(input('Enter number: '))
        
        except:
            print('Kindly Enter valid number only')
        
        else:
            user_inputs.append(number)
        
        finally:
            input_text = input('Enter yes for add another input or no for ending inputs: ')

            if(input_text == 'yes'):
                pass

            if input_text == 'no':
                take_input = False

    sum_of_even_num = 0
    sum_of_odd_num  = 0
    odd_nums = []
    even_nums = []

    
    for i in range(0, len(user_inputs)):
        num = user_inputs[i]

        if(num%2 == 0 ):
            sum_of_even_num += num
            even_nums.append(num)
        
        else:
            sum_of_odd_num += num
            odd_nums.append(num)
    
    return{
        'user_inputs': len(user_inputs),
        'sum_of_even': {f'{sum_of_even_num}': even_nums},
        'sum_of_odd': {f'{sum_of_odd_num}': odd_nums}
    }

result = sum_of_add_even()
print(result)







