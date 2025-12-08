#variables

# snake_case variable naming convention
first_name = 'John', 'will'
print(first_name)

print(len(first_name))

first_name, last_name, country, age, is_married = 'Asabeneh', 'Yetayeh', 'Helsink', 250, True

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)

frist_name, last_name, country = 'John' , 'Doe', 'USA'
age = 30
is_married = False  

print(first_name, last_name, country, age, is_married)

# input_functions 
# frist_name = input('What is your first name? ')
# last_name = input('What is your last name? ')

# print('Your first name is ', frist_name)
# print('Your last name is ', last_name)


# Different python data types
# Let's declare variables with various data types

first_name = 'Asabeneh'     # str
last_name = 'Yetayeh'       # str
country = 'Finland'         # str
city= 'Helsinki'            # str
age = 250                   # int, it is not my real age, don't worry about it
date_of_birth = 1970        # int

print(type(first_name))   # str
print(type(last_name))    # str
print(type(country))      # str
print(type(city))         # str
print(type(age))          # int 
print(type(date_of_birth)) #int

#Casting: Converting one data type to another data type
# int to float
num_int = 10
print('num_int',num_int)         # 10
num_float = float(num_int)
print('num_float:', num_float)   # 10.0

# float to int
gravity = 9.81
print(int(gravity))             # 9

# int to str
num_int = 10
print(num_int)                  # 10
num_str = str(num_int)
print(num_str)                  # '10'

# str to int or float
num_str = '10.6'
num_float = float(num_str)
print('num_float', float(num_str))  # 10.6
num_int = int(num_float)
print('num_int', int(num_int))      # 10

# str to list
first_name = 'Asabeneh'
print(first_name)               # 'Asabeneh'
first_name_to_list = list(first_name)
print(first_name_to_list)            # ['A', 's', 'a', 'b', 'e', 'n', 'e', 'h']

# str to list
company_name = 'Coding For All'
print(company_name)               # 'Coding For All'
company_name_to_list = list(company_name)
print(company_name_to_list)            # ['C', 'o', 'd', 'in', 'g', ' ', 'F', 'o', 'r', ' ', 'A

#number to complex number
num_int = 10
print('num_int:', num_int)         # 10

num_float = 10.6
print('num_float:', num_float)     # 10.6

num_complex = 2 + 3j
print('num_complex:', num_complex) # (2+3j)

