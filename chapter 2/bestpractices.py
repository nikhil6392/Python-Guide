"""Writing clean and concise code."""

"""Loops In pythonic Way"""

"""Looping through a list"""

lst = [10, 20, 30, 40, 50]

for i in range(len(lst)):
    print(lst[i])

"""Output: 10
           20
           30
           40
           50
"""

"""This is not a pythonic way"""

for item in lst:
    print(item)

"""Output: 10
           20
           30
           40
           50
"""

"""This is a pythonic way"""


"""Looping through a dictionary"""

my_dict = {'a': 1, 'b': 2, 'c': 3}

for key in my_dict:
    value = my_dict[key]
    print(key, value)

"""
   Output: a 1
           b 2
           c 3
"""

"""It works but it is not pythonic """

for key, value in my_dict.items():
    print(key, value)

"""
   Output: a 1
           b 2
           c 3
"""
"""This is the pythonic way to iterate way over dict"""


"""Looping with a condition"""

lst1 = [1, 2, 3, 4, 5]
for i in range(len(lst1)):
    if lst1[i] > 2:
        print(lst1[i])

"""
    Output: 3
            4
            5
"""

"""This works but it is not pythonic"""

lst2 = [1, 2, 3, 4, 5]
for item in lst2:
    if item > 2:
        print(item)


"""
    Output: 3
            4
            5
"""