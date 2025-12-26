#Create an empty dictionary called dog
dog = {}

#Add name, color, breed, legs, age to the dog dictionary
dog = {
    'name': 'Buddy',
    'color': 'Brown',
    'breed': 'Golden Retriever',
    'legs': 4,
    'age': 5
}

#Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {
    'first_name': 'William',
    'last_name': 'Sonal',
    'gender': 'Male',
    'age': 24,
    'marital_status': 'Single',
    'skills': ['Python', 'Data Analysis', 'Machine Learning'],
    'country': 'USA',
    'city': 'New York',
    'address': '123 Main St'
}

#Get the length of the student dictionary
print(len(student))

#Get the value of skills and check the data type, it should be a list
skills = student['skills']
print(type(skills))

skills.append('Statistics')
skills.append('Deep Learning')
print(student['skills'])
print(student)

#Get the dictionary keys as a list
print(student.keys())

#Get the dictionary values as a list
print(student.values())

#Change the dictionary to a list of tuples using items() method
student_items = student.items()
student_list = list(student.items())
student_tuples = tuple(student.items())
print(student_items)
print(student_list)
print(student_tuples)

#Delete one of the items in the dictionary
del student['marital_status']
print(student)

#Delete one of the dictionaries
del dog
