# METHODS
# A method is a function that is called on an object


# myList is an object and the append() method is called on it to find the index of 'python'
myList = ['hello', 'world', 'python', 'is', 'awesome']
myList.index('python') # 2
print(myList)

# myList.index('missing') # ValueError: 'missing' is not in list

# ADDING AND INSERTING VALUES TO A LIST
# append() and insert() methods modify the list in place

# myList.append('missing') # This appends 'missing' to the end of the list

# myList.insert(2, 'inserted') # This inserts 'inserted' at index 2

# REMOVING VALUES FROM A LIST
# remove() and pop() methods modify the list in place
# remove() removes the first occurrence of a value

# myList.remove('missing') # This removes 'missing' from the list
# myList.pop(2) # This removes 'inserted' from the list


# SORTING VALUES IN A LIST
# sort() and reverse() methods modify the list in place
# Sorting doesn't work with multiple data types
# Capital letters come before lowercase letters (ASCII values)

myList.sort() # This sorts the list in ascending order
print(myList)
myList.reverse() # This reverses the order of the list
print(myList)


