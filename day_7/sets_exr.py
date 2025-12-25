# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Find the length of the set it_companies
print(len(it_companies))

# Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(it_companies)

# Insert multiple IT companies at once to the set it_companies
more_itcom = {'Netflix', 'N8N', 'Zoom'}
it_companies.update(more_itcom)
print(it_companies)

# Remove one of the companies from the set it_companies
it_companies.pop() 
print(it_companies)

# What is the difference between remove and discard


# Join A and B
print(A.union(B))

# Find A intersection B
print(A.intersection(B))

# Is A subset of B
print(A.issubset(B))

# Are A and B disjoint sets
print(A.isdisjoint(B))

# Join A with B and B with A
print(f"this is a join : {A.isdisjoint(B)}")
print(f"this is a join :  {B.isdisjoint(A)}")

# What is the symmetric difference between A and B
print(A.difference(B))

# Delete the sets completely
del A


# Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age_set = set(age)
print(age_set)
print (len(age) > len(age_set))

#I am a teacher and I love to inspire and teach people. 
#How many unique words have been used in the sentence? Use the split methods and set to get the unique words.

sentence = 'I am a teacher and I love to inspire and teach people'
sentence = sentence.split()
print(sentence)

sentence = set(sentence)
print(sentence)
print(len(sentence))

