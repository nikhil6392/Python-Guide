"""The OrderedDict is a class provided by the collections module in Python that is similar to a regular dictionary. But with the added feature of preserving the order in which the items were inserted.
This can be particularly useful in cases where the order of items in a dictionary matters.

TO use OrderedDict, first, we need to import it from the collections module.
"""

from collections import OrderedDict

"""Creating an OrderedDict"""

od = OrderedDict()

"""Adding an element to an OrderedDict"""

"""Add an element to an OrderedDict, we can use the update() method."""

od.update({'a': 1})
od.update({'b': 2})
od.update({'c': 3})

"""     or         """

od['d'] = 4

"""Removing element from an OrderedDict"""

"""We can use pop() method ."""

od.pop('a')

"""          or        """

del od['b']


""" Iterating over an OrderedDict """

for key, value in od.items():
    print(key, value)


""" Reversing the order of an OrderedDict """

for key, value in reversed(od.items()):
    print(key, value)


"""  Example  """

text = "I am a software developer"

words = text.split()

word_count = OrderedDict()

for word in words:
    if word in word_count:
        word_count[word] += 1
    
    else:
        word_count[word] = 1

for key, value in word_count.items():
    print(key, value)
