# Tuples
# It is an ordered collection of elements that can be any type
# But it is immutable

# Creating a tuple using parentheses
mytuple =(1, 2, 3, 4, 5)

# Creating a tuple using tuple() function
mytuple1 = tuple([1, 2, 3, 4, 5])

# accessing tuples element

print(mytuple[0]) # Output: 1

print(mytuple1)  # Output: (1, 2, 3, 4, 5)


# Slicing a tuple

print(mytuple[1:3])  # Output: (2, 3)

# Unpacking a tuple

tuple1 = (1, 2, 3)

a, b, c = tuple1

print(a)  # Output : 
print(b)  # Output: 2
print(c)  # Output: 3

# Concatenation Tuples
# It can be done by using + operator

tuple2 = (10, 33,39)
tuple3 = (30, 20, 20)

newTuple = tuple2 + tuple3

print(newTuple)   # Output : (10, 33, 39, 30, 20, 20)


# We can also use tuples as keys in dictionaries

mydict = {(1,2): 'value 1', (3, 4): 'value 2'}

print(mydict[(1,2)])       # Output: value 1