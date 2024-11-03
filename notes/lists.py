# LISTS ARE MUTABLE AND ORDERED OBJECTS
# Lists can be lists of lists
# Lists can have duplicate values




spam = ['cat', 'bat', 'rat', 'elephant']
print(spam)
print('original Object: ' + spam[1])

# Replace Individual Values in a List with Indexes
spam[1] = 'aardvark'
print(spam)
print('Single Replace Object: ' + spam[1])

# Replace Range of Values in a List with Indexes (SLICE)
# Slice (a,b) a is inclusive, b is exclusive
spam[1:4] = ['bird'] # Replaces ['aardvark', 'rat', 'elephant'] with ['bird']
print(spam)
print('Range Replace Object: ' + spam[1])


nestedList = [['cat', 'bat'], [10, 20, 30, 40, 50, 50]]
print(nestedList)

nestedList[0][1] = 'dog'
print(nestedList)


# DELETE VALUES IN A LIST
delList = ['cat', 'bat', 'rat', 'elephant']
print(delList)
del