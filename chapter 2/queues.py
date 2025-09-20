
"""Data Structure: Queues"""

"""It is used to store a collection of elements in FIFO"""

"""Creating a Queue"""
from collections import deque

myqueue = deque()

print(type(myqueue))    # Output : <class 'collections.deque'>

"""Insertion: it is done by append() method"""
myqueue.append(1)
myqueue.append(2)
myqueue.append(3)


print(myqueue)      # Output : deque([1, 2, 3])

"""Removing elements form a queue"""
x = myqueue.popleft()
print(x)                # Output : 1
print(myqueue)          # Output : deque([2, 3])

""" Size of the queue"""

print(len(myqueue))     # Output : 2