"""Closures"""

def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

obj = outer_function(10)

result = obj(5)
print(result)       # Output: 15

"""Closures are one of the powerful tool that a python developer should have."""