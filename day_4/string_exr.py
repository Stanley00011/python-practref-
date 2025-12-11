#Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
first_part = 'Thirty'
second_part = 'Days'
third_part = 'Of'
fourth_part = 'Python'
full_string = first_part + ' ' + second_part + ' ' + third_part + ' ' + fourth_part
print(full_string)

# Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
first_str = 'Coding'
second_str= 'For'
third_str = 'All'
full_str = first_str + ' ' + second_str + ' ' + third_str
print(full_str) 

# Declare a variable named company and assign it to an initial value "Coding For All".
company = 'Coding For All'
print(company)

# Print the length of the company string using len() method and print().
print(len(company))

#Change all the characters to uppercase letters using upper() method.
print(company.upper())

# Change all the characters to uppercase letters using upper() method.
print(company.lower())

#Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())
print(company.title())
print(company.swapcase())

#Cut(slice) out the first word of Coding For All string.
first_word = company[0:6]
print(first_word)

#Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(company.index('Coding'))
print(company.find('Coding'))

#Replace the word coding in the string 'Coding For All' to Python.
new_company = company.replace('Coding', 'Python')
print(new_company)

#Change Python for Everyone to Python for All using the replace method or other methods.
for_all_string = 'Python for Everyone'
new_for_all_string = for_all_string.replace('Everyone', 'All')
print(new_for_all_string)   

# Split the string 'Coding For All' using space as the separator (split()) .
split_company = company.split(' ')
print(split_company)

#"Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
big_tech = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(big_tech)
split_big_tech = big_tech.split(', ')
print(split_big_tech)

#What is the character at index 0 in the string Coding For All.
print(company[0])

#What is the last index of the string Coding For All.
last_index = len(company) - 1 #company[-1] 
print(last_index)

# What character is at index 10 in "Coding For All" string.
print(company[10])
print(company)

# Create an acronym or an abbreviation for the name 'Python For Everyone'.
phrase = 'Python For Everyone'
acronym = phrase[0] + phrase[7] + phrase[11]
print(acronym)

#Create an acronym or an abbreviation for the name 'Coding For All'.
company_acronym = company[0] + company[7] + company[11]
print(company_acronym)

#Use index to determine the position of the first occurrence of C in Coding For All.
index_of_C = company.index('C')
print(index_of_C)

#Use index to determine the position of the first occurrence of F in Coding For All.
index_of_F = company.index('F')
print(index_of_F)

#Use rfind to determine the position of the last occurrence of l in Coding For All People.
last_index_of_l = company.rfind('l')
print(last_index_of_l)

#Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
occurence_sentence = 'You cannot end a sentence with because because because is a conjunction'
first_occurrence_because = occurence_sentence.index('because')
print(first_occurrence_because)

#Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
first_position_because = occurence_sentence.rindex('because')
print(first_position_because)

# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

slice_sentece = 'You cannot end a sentence with because because because is a conjunction'
sliced_phrase = slice_sentece[31:54]
print(sliced_phrase)

#Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
first_sliced_phrase = slice_sentece.index('because')
print(f'this is: {first_sliced_phrase}')

#Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
to_slice = slice_sentece[31:54]
print(to_slice)

#Does ''Coding For All' start with a substring Coding?
sub_string = company.startswith('Coding')
print(sub_string)

# Does 'Coding For All' end with a substring coding?
sub_string_end = company.endswith('Coding')
print(sub_string_end)

# '   Coding For All      '  , remove the left and right trailing spaces in the given string.
c_for_all = '   Coding For All      '

# 1. Remove ALL leading and trailing whitespace
clean_string = c_for_all.strip() # Correct way

# 2. Only remove leading (left) whitespace
trim_c_for_lall = c_for_all.lstrip()

# 3. Only remove trailing (right) whitespace
trim_c_for_rall = c_for_all.rstrip()

print(f"Original:   '{c_for_all}'")
print(f"Cleaned:    '{clean_string}'")
print(f"L-Trimmed:  '{trim_c_for_lall}'")
print(f"R-Trimmed:  '{trim_c_for_rall}'")

# Which one of the following variables return True when we use the method isidentifier():
# 30DaysOfPython
# thirty_days_of_python

thirty =  '30DaysOfPython'
thirty_days = 'thirty_days_of_python'

thirty_i = thirty.isidentifier()
thirty_days_i =  thirty_days.isidentifier()

print(thirty_i)
print(thirty_days_i)

# The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
python_libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
Join_ython_libraries = '# '.join(python_libraries)
print(Join_ython_libraries)

# Use a tab escape sequence to write the following lines.
# Name      Age     Country   City
# Asabeneh  250     Finland   Helsinki
print(
    'Name\tAge\tCountry\tCity\n'
    'Asabeneh\t250\tFinland\tHelsinki'
)

# Use the string formatting method to display the following:
# radius = 10
# area = 3.14 * radius ** 2
# The area of a circle with radius 10 is 314 meters square.

radius = 10
area = 3.14 * radius ** 2

# Use an f-string to embed the calculated values
print(f"The area of a circle with radius {radius} is {area} meters square.")


a = 8
b = 6

print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
# Use formatting inside the placeholder to round the float result to two decimal places
print('{} / {} = {:.2f}'.format(a, b, a / b))
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))
