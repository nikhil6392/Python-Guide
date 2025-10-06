"""Partial Functions"""

"""It is way of fixing a certain number of args to a function"""

"""Creating a partial function"""

from functools import partial


def sum(x, y):
    return x + y

double = partial(sum, 2)
print(double(5))

"""Output : 7"""

"""Passing additional arguments"""

def multiplication(x, y, z):
    return x * y * z

double = partial(multiplication, 2)
triple = partial(multiplication, z = 5)

print(double(5, 2))
"""Output: 20"""
print(triple(5, 2))
"""Output : 50"""


"""using partial function with lambda"""

double = partial(lambda x, y: x * y, 2)
print(double(5))

"""Output : 10"""

