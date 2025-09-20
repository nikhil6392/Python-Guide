""" Data Structure : Stack"""
""" It is an LIFO data structure"""

""" Creating a stack """
myStack = []

"""Insertion in stack"""
myStack.append(1)
myStack.append(2)
myStack.append(3)
myStack.append(4)

print(myStack)      # Output : [1, 2, 3, 4]

"""Removing element from a stack"""
myStack.pop()
print(myStack)      # Output : [1, 2, 3]


"""Size of an stack"""

print(len(myStack))   # Output : 3