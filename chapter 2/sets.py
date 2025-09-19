"""
    Data Structure: Set
    It is an unordered collection of unique elements
    sets are mutable.
"""

# Creating a set
# Set be created using curly braces or set() function
mySet = {1, 2, 3, 4}
print(type(mySet))  # Output : <class 'set'>
print(mySet)        # Output : {1, 2, 3, 4}

mySet2 = set([1, 2, 3, 4])
print(type(mySet2))     # Output : <class 'set'>
print(mySet2)           # Output : {1, 2, 3, 4}

# Accessing set elements
# Set elements can be accessed using a for loop or the in keyword

for element in mySet:
    print(element)

"""
    Output: 1
            2
            3
            4
"""
print(1 in mySet)   # Output : True
print(5 in mySet)   # Output : False


# Modifying set elements
# Since sets are mutable data structure they can be modified

mySet.add(5)
print(mySet)        # Output : {1, 2, 3, 4, 5}

mySet.remove(4)
print(mySet)        # Output : {1, 2, 3, 5}


# Combining sets
# Sets can be combined using union(), intersection(), and difference() methods.

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
 
setU = set1.union(set2)
print(setU)         # Output : {1, 2, 3, 4, 5, 6}

setI = set1.intersection(set2)
print(setI)         # Output : {3, 4}

setD = set1.difference(set2)
print(setD)         # Output: {1, 2}

# Checking if set is a subset or superset

# issubset()-> for checking subset
# issuperset()-> for checking superset

set3 = {1, 2, 3}
set4 = {1, 2, 3, 4, 5}

print(set3.issubset(set4))      # Output : True
print(set4.issuperset(set3))    # Output : True
print(set3.issuperset(set3))    # Output : True
print(set3.issuperset(set4))    # Output : False


# Removing Duplicate elements
# Sets can be used to remove duplicate elements form a list

lst = [1, 3, 2, 2, 3, 1, 2]
print(set(lst))     # Output : {1, 2, 3}

