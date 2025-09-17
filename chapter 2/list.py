# Data Structure : List

# list is one of the most used data structure in python

# Creating a list
# Lists can be created using square brackets [] or the list() function.

# using square brackets
mylist1 = [1, 2, 3, 4, 5]

print(type(mylist1)) # Output: <class 'list'>

# using list() function.
mylist2 = list([1, 2, 3, 4, 5])

print(type(mylist2)) # Output : <class 'list'>

# Accessing list elements
# list can be accessed using indexing, indexing start from 0 for the first element

print(mylist2[0])      # Output: 1

# Slicing a list
# Lists can be sliced using the syntax start:end.
# slicing a list returns a new list containing the selected elements

print(mylist2[2:4])  # Output: [3, 4]

# Modifying lists elements

print(mylist2)    # Output : [1, 2, 3, 4, 5]
mylist2[2] = 19

print(mylist2)   # Output: [1, 2, 19, 4, 5]


# Adding elements to a list

# single element

mylist2.append(6)
print(mylist2)     # Output : [1, 2, 19, 4, 5, 6]

# Multiple elements

mylist2.extend([10, 13, 15])
print(mylist2) # Output : [1, 2, 19, 4, 5, 6, 10, 13, 15]


# Removing elements from a list
# Elements can be removed from a list using the remove()
# or the pop() method to remove and element at a specific index

# remove() method removes the element 19

mylist2.remove(19)
print(mylist2)     # Output : [1, 2, 4, 5, 6, 10, 13, 15]

# pop() method removes the element from a given index

mylist2.pop(2)
print(mylist2)     # Output : [1, 2, 5, 6, 10, 13, 15]

# Sorting a list 
# Lists can be sorted using the sort() method or the sorted() function

# sort method
newlist = [4, 5, 3, 93, 2]
newlist.sort()
print(newlist)   # Output : [2, 3, 4, 5, 93]

# sorted function
newlist1 = [23, 4,292, 4, 29]
lst = sorted(newlist1)
print(lst)  # Output : [4, 4, 23, 29, 292]


# we can reverse the lists to by using newlist.sort(reverse=True)

# we can reverse the lists to by using lst = sorted( newlist1,reverse=True)