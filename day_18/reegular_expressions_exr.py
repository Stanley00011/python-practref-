import re
from collections import Counter

paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
# 1. Extract all words using your regex
words = re.findall(r'\b\w+\b', paragraph)
# 2. Count the occurrences
counts = Counter(words)
# 3. Format into [(count, word), ...] and Sort
# We use a list comprehension to swap the order from (word, count) to (count, word)
result = [(count, word) for word, count in counts.items()]
# 4. Sort the list by the count (the first element of the tuple) in descending order
result.sort(key=lambda x: x[0], reverse=True)
# Print the result
import pprint
pprint.pprint(result)


# The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in
# the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles.
text = "The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction."

# 1. Extract strings that look like numbers
extracted_strings = re.findall(r'-?\d+', text)

# 2. Convert them to actual integers
points = [int(i) for i in extracted_strings]

# 3. Sort them to find the extremes
sorted_points = sorted(points)

# 4. Calculate distance between the first and last item
min_pt = sorted_points[0]
max_pt = sorted_points[-1]
distance = max_pt - min_pt

print(f"Points: {points}")
print(f"Sorted Points: {sorted_points}")
print(f"Distance between {max_pt} and {min_pt} is: {distance}")

# Write a pattern which identifies if a string is a valid python variable
def is_valid_variable(variable_name):
    # Define the pattern
    pattern = r'^[a-zA-Z_][a-zA-Z0-9_]*$'
    
    # re.match returns a match object if valid, None if invalid
    if re.match(pattern, variable_name):
        return True
    return False

# Test Cases
print(is_valid_variable('first_name'))  # True
print(is_valid_variable('first-name'))  # False (Contains a hyphen)
print(is_valid_variable('1first_name')) # False (Starts with a number)
print(is_valid_variable('firstname'))   # True

# Clean the following text. After cleaning, count three most frequent words in the string.
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

# 1. Clean the text: Remove anything that isn't a letter or a space
# We replace special chars with nothing ''
cleaned_text = re.sub(r'[^a-zA-Z ]', '', sentence)

# 2. Remove extra spaces that might have been left behind
cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()

print(f"Cleaned Text:\n{cleaned_text}\n")


def most_frequent_words(text):
    # Split text into a list of words
    words = text.split()
    
    # Count them
    counts = Counter(words)
    
    # Get the 3 most common, but they come as ('word', count)
    top_three = counts.most_common(3)
    
    # Swap them to match your (count, 'word') format
    return [(count, word) for word, count in top_three]

print("Top 3 Most Frequent:")
print(most_frequent_words(cleaned_text))
# I am a teacher and I love teaching There is nothing as more rewarding as educating and empowering people I found teaching more interesting than any other jobs Does this motivate you to be a teacher
# print(most_frequent_words(cleaned_text)) # [(3, 'I'), (2, 'teaching'), (2, 'teacher')]

