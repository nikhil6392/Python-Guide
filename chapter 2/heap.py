"""Data Structure : Heap"""


"""Creation of heap"""

import heapq as heap

myheap = [3, 1, 4, 1, 5, 9, 2, 6, 5]

heap.heapify(myheap)

print(myheap)       # Output : [1, 1, 2, 3, 5, 9, 4, 6, 5]

"""Minimum element from a heap"""

print(heap.heappop(myheap))     # Output : 1

""" Insertion in a heap"""

heap.heappush(myheap, 10)

print(myheap)   # Output : [1, 3, 2, 5, 5, 9, 4, 6, 10]

"""Size of a heap"""

print(len(myheap))  # Output : 9





