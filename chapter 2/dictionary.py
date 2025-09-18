# Data Structure : Dictionary
# it is an unordered collection of key-value pairs
# key is unique

# Creating Dictionary
# Dictionary can be created using {}.

mydict = {'apple': 1, 'banana': 2, 'orange': 3}
print(mydict)       # Output : {'apple': 1, 'banana': 2, 'orange': 3}

# using dict()
dict1 = dict(apple=1, banana=2, orange=3)
print(dict1)     # Output : {'apple': 1, 'banana': 2, 'orange': 3}

# Accessing dictionary elements
# It can be done by using key
print(dict1['apple'])   # Output: 1  # Output: Error

# Modifying dictionary elements
# Dictionaries are mutable
mydict['orange'] = 4
print(mydict)        # Output: {'apple': 1, 'banana': 2, 'orange': 4}


# Insertion 
newdict = {'apple': 1, 'banana': 2}

newdict['orange'] = 3

print(newdict)      # Output : {'apple': 1, 'banana': 2, 'orange': 3}

# Deletion 
# It can be performed using del key word
del newdict['orange']
print(newdict)   # Output : {'apple': 1, 'banana': 2}

# Or it can by done via pop()

newdict.pop('banana')
print(newdict)      # Output : 

# Checking if a key exists a dictionary or not
dict2 = {'apple': 1, 'banana': 2, 'orange': 3}
print('orange' in dict2)            # Output : True
print('watermelon' in dict2)        # Output : False

# Iteration over a dictionary
# item() method to get the key-value pair

dict3 = {'BMW': 1, 'Audi': 2, 'Range Rover': 3}


# for getting key and value items
for key, value in dict3.items():
    print(key, value)

# Output : 
"""BMW 1
Audi 2
Range Rover 3"""

# for getting just keys
for key in dict3.keys():
    print(key)

""" Output: 
BMW
Audi
Range Rover
"""

# for getting values
for val in dict3.values():
    print(val)

    """
 Output:    1
            2
            3
    """ 