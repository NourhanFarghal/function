#____________________________________Understand the Meaning and Applications of Functions_______________________________________________
# 1 . Problem: Write a function greet() that prints "Hello, World!". Discuss how functions help in organizing code and avoiding repetition

def greet():
    print("Hello, World!")
# Call the function
greet()

#_______________________________________________________________________________________________________________________________________

# 2 . Problem: Create a function that calculates the factorial of a number. Explain how functions help in breaking down complex problems into simpler sub-problems

def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)

# Call the function 
number = 5
print(f"factorial of {number} is {factorial(number)}")
 

#_______________________________________________________________________________________________________________________________________
# 3 . Problem: Implement a function that checks whether a number is prime. Discuss how this function could be reused in different parts of a program

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):  # Check divisibility up to the square root of n
        if num % i == 0:
            return False
    return True

# Call the function 
number = int(input('Enter the number please: '))
if is_prime(number):
    print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")


#__________________________________________________________Define Functions_____________________________________________________________
# 1 . Problem: Write a function add_numbers(a, b) that returns the sum of two numbers

def add_numbers(a, b):
    return a + b

# Call the function
number1 = 10
number2 = 20
result = add_numbers(number1, number2)
print(f"{number1} + {number2} = {result}")


#_______________________________________________________________________________________________________________________________________
# 2 . Problem: Implement a function reverse_string(s) that returns the reverse of a given string

def reverse_string(s):
    return s[::-1]  

# Call the function
string = "Hi, i am Nourhan Farghal"
reversed_string = reverse_string(string)
print(f"The reverse of '{string}' is: '{reversed_string}'")



#_______________________________________________________________________________________________________________________________________
# 3 . Problem: Create a function is_palindrome(s) that checks if a string is a palindrome

def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

# Call the function
test_string = "Hi I am Nourhan Farghal"
if is_palindrome(test_string):
    print(f"'{test_string}' is a palindrome")
else:
    print(f"'{test_string}' is not a palindrome")



#________________________________________________Understand Function Parameters_________________________________________________________
# 1 . Problem: Write a function multiply(a, b=1) that multiplies two numbers, with the second parameter having a default value of 1

def multiply(a, b=1):
    return a * b

# Call the function 
result1 = multiply(5, 3)
print(result1)
result2 = multiply(7) # b is default by 1
print(result2)


#_______________________________________________________________________________________________________________________________________
# 2 .Problem: Implement a function greet(name, message="Hello") that prints a personalized greeting message

def greet(name, message="Hello"):
    print(f"{message}, {name}!")

# Call the function
name = input('Enter the name please: ') 
greet(name , "Good morning")
greet(name) # message = Hello 


#_______________________________________________________________________________________________________________________________________
# 3 . Problem: Create a function find_max(*args) that takes a variable number of arguments and returns the maximum value

def find_max(*args):
    if not args:  
        return None
    return max(args) 

# Call the function
result1 = find_max(10, 20, 30, 5)
print(f"The maximum value is: {result1}")
result2 = find_max(3, 7, 1)
print(f"The maximum value is: {result2}")
result3 = find_max()
print(f"The maximum value is: {result3}")


#______________________________________________________Explore Default Parameter Values_________________________________________________
# 1 . Problem: Write a function power(base, exponent=2) that raises a base number to a given exponent, with a default exponent of 2

def power(base, exponent=2):
    return base ** exponent  # Use the exponentiation operator

# Call the function
result1 = power(3, 3)
print(result1)
result2 = power(5) # exponent=2 by default
print(result2)


#_______________________________________________________________________________________________________________________________________
# 2 . Problem: Implement a function create_user(username, role="user") that creates a user with a specified role, defaulting to "user"

def create_user(username, role="user"):
    return f"User '{username}' created with role: '{role}'"

# Call the function
user1 = create_user("Nourhan", "admin")
print(user1)
user2 = create_user("Ahmed")
print(user2)


#_______________________________________________________________________________________________________________________________________
# 3 . Problem: Create a function print_triangle(height=5) that prints a triangle of a given height, with a default height of 5

def print_triangle(height=5):
    for i in range(1, height + 1):
        print('*' * i) 

# Call the function
print("Triangle with default height:")
print_triangle()
print("\nTriangle with height 4:")
print_triangle(4)
print("\nTriangle with height 6:")
print_triangle(6)


#_________________________________________________________Learn About Return Values_____________________________________________________
# 1 . Problem: Write a function calculate_area(radius) that returns the area of a circle


def calculate_area(radius):
    pi = 3.14
    area = pi * (radius ** 2)  # Calculate the area 
    return area  

# Call the function 
radius_value = 5
area_result = calculate_area(radius_value)
print(f"The area of {radius_value} is: {area_result}")


#_______________________________________________________________________________________________________________________________________
# 2 . Problem: Implement a function sum_of_list(lst) that returns the sum of all elements in a list

def sum_of_list(lst):
    total = sum(lst)  
    return total 

# Call the function
numbers = [1, 2, 3, 4, 5]
result = sum_of_list(numbers)

print(f"The sum of {numbers} is: {result}")


#_______________________________________________________________________________________________________________________________________
# 3 .Problem: Create a function find_largest(a, b, c) that returns the largest of three numbers

def find_largest(a, b, c):
    if a >= b and a >= c:
        return a  
    elif b >= a and b >= c:
        return b  
    else:
        return c  

# Call the function     
num1 = 87
num2 = 92
num3 = 41
largest_number = find_largest(num1, num2, num3)
print(f"The largest number of {num1}, {num2},{num3} is: {largest_number}")



#_________________________________________________________Call Functions_________________________________________________________________
# 1 . Problem: Write a function greet_user(name) and call it from the main block of the script

def greet_user(name):
    print(f"Hello, {name}") 

if __name__ == "__main__":
    user_name = input("Enter your name: ") 
    greet_user(user_name) 


#_______________________________________________________________________________________________________________________________________
# 2 .Problem: Create a function calculate_tax(amount) and call it multiple times with different amounts to calculate the tax

def calculate_tax(amount, tax_rate):
    tax = amount * tax_rate  
    return tax  

# Call the function     
amounts = [100, 250, 500, 750, 1000]
for amount in amounts:
    tax_amount = calculate_tax(amount , 0.15)  
    print(f"The tax of ${amount} is: ${tax_amount}")


#_______________________________________________________________________________________________________________________________________
# 3 .Problem: Implement a function convert_temperature(celsius) and call it with user input to convert Celsius to Fahrenheit

def convert_temperature(celsius):
    fahrenheit = (celsius * 9/5) + 32  
    return fahrenheit  

# Call the function 
user_input = input("Enter temperature in Celsius: ")
celsius_value = float(user_input) # Convert user input to float
fahrenheit_value = convert_temperature(celsius_value)
print(f"{celsius_value}C = {fahrenheit_value}F")



#__________________________________________________________Understand Scope______________________________________________________________

# 1 .Problem: Write a program that demonstrates the difference between local and global variables by modifying a global variable inside a function

global_var = 10

def modify_global_variable():
    global global_var 
    print(f"Original: {global_var}") 
    global_var += 5 
    print(f"Modified: {global_var}")  
# Call the function 
modify_global_variable() 


#_______________________________________________________________________________________________________________________________________
# 2 . Problem: Create a function that defines a local variable and tries to access it outside the function, explaining the resulting error

def create_local_variable():
    local_var = "I am a local variable!"  # This local variable 
    print(local_var) 

## Call the function
create_local_variable()  
try:
    print(local_var)  # Attempt to access the local variable outside the function
except NameError as e:
    print(f"Error: {e}")  # Catch the error



#_______________________________________________________________________________________________________________________________________
# 3 . Problem: Implement a nested function where the inner function accesses a variable from the outer function’s scope

def outer_function():
    outer_var = "I am from the outer function!" 
    # Define an inner (nested) function
    def inner_function():
        print(outer_var)  

    # Call the inner function
    inner_function()
 # Call the outer function
outer_function()  


#_________________________________________________Explore Lambda Functions_______________________________________________________________
# 1 .Problem: Write a lambda function that adds 10 to a given number and call it with different values

add_ten = lambda x: x + 10
values = [5, 15, 25, -10, 0]  # List of values to test

# Call the lambda 
for value in values:
    result = add_ten(value)
    print(f"{value} + 10 = {result}")


#_______________________________________________________________________________________________________________________________________
# 2 .Problem: Implement a lambda function that multiplies two numbers and use it with Python’s map() function to multiply a list of numbers by a constant

constant = 3
numbers = [1, 2, 3, 4, 5]
multiplied_numbers = list(map(lambda x: x * constant, numbers))

print(f'{numbers} * {constant} = {multiplied_numbers}')



#_______________________________________________________________________________________________________________________________________
# 3 .Problem: Create a lambda function that filters out all even numbers from a list using the filter() function

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(f'{numbers} the list after filter {odd_numbers}')



#_________________________________________________Practice Recursion____________________________________________________________________
# 1 .Problem: Write a recursive function to calculate the factorial of a number

def factorial(num):
    if num == 0 or num == 1:  
        return 1
    else:
        return num * factorial(num - 1)  

test_values = [5, 0, 1, 4, 6]
for value in test_values:
    result = factorial(value)
    print(f"Factorial of {value} = {result}")


#_______________________________________________________________________________________________________________________________________
# 2 . Problem: Implement a recursive function to find the greatest common divisor (GCD) of two numbers

def gcd(a, b):
    if b == 0: 
        return a
    else:
        return gcd(b, a % b)  

test_values = [(48, 18), (56, 98), (101, 10), (100, 25)]
for a, b in test_values:
    result = gcd(a, b)
    print(f"GCD of {a} & {b} = {result}")


#_______________________________________________________________________________________________________________________________________
# 3 . Problem: Create a recursive function to solve the Fibonacci sequence and print the nth Fibonacci number

def fibonacci(n):
    if n <= 0:  
        return 0
    elif n == 1: 
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  

test_values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for value in test_values:
    result = fibonacci(value)
    print(f"Fibonacci of {value} = {result}")









