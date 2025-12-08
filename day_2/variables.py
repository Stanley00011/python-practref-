# Day2 30 days of python programming

#Declare a first name variable and assign a value to it
frist_name = 'blake'
last_name = 'stiner'
full_name = frist_name + ' ' + last_name
country = 'USA'
city = 'New York'
age = 25
year = 2024
is_married = False 
is_true = True
is_light_on = True
multiple_declarations = frist_name, last_name, country, age = 'blake', 'stiner', 'USA', 25

print(type(frist_name))          # str
print(type(last_name))           # str  
print(type(full_name))           # str
print(type(country))             # str
print(type(city))                # str
print(type(age))                 # int
print(type(year))                # int
print(type(is_married))         # bool
print(type(is_true))            # bool
print(type(is_light_on))        # bool
print(type(multiple_declarations))  # tuple


print(len(frist_name))

#Compare the length of your first name and your last name
print(len(frist_name) == len(last_name))

#Declare 5 as num_one and 4 as num_two
num_one = 5
num_two = 4 

#Add num_one and num_two and assign the value to a variable total
total_num  = num_one + num_two
print(total_num)
#Subtract num_two from num_one and assign the value to a variable difference
difference = num_one - num_two
print(difference)
#Multiply num_two and num_one and assign the value to a variable product
product = num_one * num_two
print(product)
#Divide num_one by num_two and assign the value to a variable division
division = num_one / num_two
print(division)     
#Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
remainder = num_two % num_one
print(remainder)
#Calculate num_one to the power of num_two and assign the value to a variable exp   onential
exponential = num_one ** num_two
print(exponential)
#Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division = num_one // num_two
print(floor_division)
#The radius of a circle is 30 meters.       
radius = 30
#Calculate the area of a circle and assign the value to a variable area_of_circle
area_of_circle = 3.14 * radius ** 2
print(area_of_circle)
#Calculate the circumference of a circle and assign the value to a variable circum_of_circle
circum_of_circle = 2 * 3.14 * radius
print(circum_of_circle)

#Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
circum_of_circle = 2 * 3.14 * radius
print(circum_of_circle) 

#Take radius as user input and calculate the area.
radius = float(input('Enter radius: '))
area_of_circle = 3.14 * radius ** 2
print('Area of circle:', area_of_circle)

#Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
first_name = input('Enter your first name: ')
last_name = input('Enter your last name: ')
country = input('Enter your country: ')
age = input('Enter your age: ')
print('First Name:', first_name)
print('Last Name:', last_name)
print('Country:', country)
print('Age:', age)
