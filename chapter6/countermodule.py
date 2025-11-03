""" Counter """

from collections import Counter

pens = ['blue', 'black', 'blue', 'black', 'red', 'red', 'green', 'blue', 'black', 'blue']

pen_count = Counter(pens)

print(pen_count)

"""Output : Counter({'blue': 4, 'black': 3, 'red': 2, 'green': 1})"""

print(pen_count.most_common(1))

"""Output : [('blue' , 4)]"""

print(list(pen_count.elements()))

"""Output : ['blue', 'blue', 'blue', 'blue', 'black', 'black', 'black', 'red', 'red', 'green']"""

