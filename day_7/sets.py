# sets example 
fruits = {'banana', 'orange', 'mango', 'lemon'}
print(len(fruits))

# Accessing Items in a Set
# We use loops to access items. We will see this in loop section
# Checking an Item
# To check if an item exist in a list we use in membership operator.
fruits = {'banana', 'orange', 'mango', 'lemon'}
print('mango' in fruits ) # True

# Adding Items to a Set
# Once a set is created we cannot change any items and we can also add additional items.
# Add one item using add()

fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.add('lime')


#Add multiple items using update() The update() allows to add multiple items to a set. The update() takes a list argument.
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = ('tomato', 'potato', 'cabbage','onion', 'carrot')
fruits.update(vegetables)

#Removing Items from a Set
#We can remove an item from a set using remove() method. If the item is not found remove() method will raise errors, so it is good to check if the item exist in the given set. However, discard() method doesn't raise any errors.

#The pop() methods remove a random item from a list and it returns the removed item.
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.pop()  # removes a random item from the set

fruits = {'banana', 'orange', 'mango', 'lemon'}
removed_item = fruits.pop() 

#learing Items in a Set: If we want to clear or empty the set we use clear method.
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.clear()
print(fruits) # set()

# Deleting a Set: If we want to delete the set itself we use del operator.
fruits = {'banana', 'orange', 'mango', 'lemon'}
del fruits

#Converting List to Set
# We can convert list to set and set to list. Converting list to set removes duplicates and only unique items will be reserved.
fruits = ['banana', 'orange', 'mango', 'lemon','orange', 'banana']
fruits = set(fruits) # {'mango', 'lemon', 'banana', 'orange'}

# Joining Sets: We can join two sets using the union() or update() method.
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
print(fruits.union(vegetables)) # {'lemon', 'carrot', 'tomato', 'banana', 'mango', 'orange', 'cabbage', 'potato', 'onion'}

#Update This method inserts a set into a given set
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
fruits.update(vegetables)
print(fruits) # {'lemon', 'carrot', 'tomato', 'banana', 'mango', 'orange', 'cabbage', 'potato', 'onion'}

# Finding Intersection Items
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.intersection(even_numbers) # {0, 2, 4, 6, 8, 10}


python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.intersection(dragon)     # {'o', 'n'}

#Checking Subset and Super Set
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.issubset(even_numbers) # False, because it is a super set
print(whole_numbers.issuperset(even_numbers)) # True

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.issubset(dragon)    # False

#Checking the Difference Between Two Sets It returns the difference between two sets.
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
print(whole_numbers.difference(even_numbers)) # {1, 3, 5, 7, 9}

python = {'p', 'y', 't', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
print(python.difference(dragon))     # {'p', 'y', 't'}  - the result is unordered (characteristic of sets)
print(dragon.difference(python))     # {'d', 'r', 'a', 'g'}

# Finding Symmetric Difference Between Two Sets
# It returns the symmetric difference between two sets. It means that it returns a set that contains 
# all items from both sets, except items that are present in both sets, mathematically: (A\B) ∪ (B\A)
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
some_numbers = {1, 2, 3, 4, 5}
whole_numbers.symmetric_difference(some_numbers) # {0, 6, 7, 8, 9, 10}

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.symmetric_difference(dragon)  # {'r', 't', 'p', 'y', 'g', 'a', 'd', 'h'}


# #Joining Sets
# If two sets do not have a common item or items we call them disjoint sets.
# We can check if two sets are joint or disjoint using isdisjoint() method.
even_numbers = {0, 2, 4 ,6, 8}
odd_numbers = {1, 3, 5, 7, 9}
even_numbers.isdisjoint(odd_numbers) # True, because no common item

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.isdisjoint(dragon)  # False, there are common items {'o', 'n'}

print (len())