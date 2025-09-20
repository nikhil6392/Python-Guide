"""
    Data Structure: Array
    An array is a collection of elements of the same data type,
    arranged in contiguous memory locs.
"""

# Creating an array
# Arrays can be created using the array() function from the array module

import array as arr

myarr = arr.array('i', [1, 2, 3, 4, 5])
print(myarr[0])     # Output : 1

# Modifying array elements
# Array elements can be modified by assigning new values to their corresponding indices

myarr[0] = 10

print(myarr)        # Output : array('i', [10, 2, 3, 4, 5])

import numpy as np