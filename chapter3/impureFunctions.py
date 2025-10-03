"""Impure Functions"""

"""mutable arguments are those that can be modified in
place, such as lists, dictionaries, and sets. When we pass a mutable
argument to a function, the function can modify it and these
modifications persist outside of the function's scope. However,
modifying mutable arguments can introduce unexpected behavior and
make code hard to maintain.
"""

"""Modify arguments in place"""

"""To modify arguments in a function is to modify the in place"""

def add_item_to_list(item, lst):
    lst.append(item)

lst = [1, 3, 5]
add_item_to_list(4, lst)
print(lst)

"""Output : [1, 3, 5, 4]"""

"""Return a new object"""

def reverse_list(lst):
    return lst[::-1]

mylst= [10, 30, 40]
reversed_list = reverse_list(mylst)
print(reversed_list)

"""Output : [40, 30, 10]"""


"""Combine both"""

def remove_duplicates(lst):
    unique_lst = list(set(lst))
    lst.clear()
    lst.extend(unique_lst)

mylist = [1, 3, 5, 3, 5, 242, 1, 242]
remove_duplicates(mylist)
print(mylist)

"""Output : [1, 242, 3, 5]"""