"""Functions"""
"""It has two types of functions: Pure and Impure Functions"""


"""Pure Functions: These functions don't cause any side effects and always produce same output"""

"""Avoid modifying global state: 
   A pure function should not modify any global state or modify any variables outside of its scope.
   This includes modifying global variables or objects that are passed bu reference to the function
"""

x = 0

def impure_add_one():
    global count
    x += 1

def pure_add_one(num):
    return num + 1

""" Avoid modifying input parameters:"""

def impure_append_list(item, lst):
    lst.append(item)

def pure_append_list(item, lst):
    return lst + [item]


"""Avoid relying on external state"""

def impure_get_current_time():
    return datetime.datetime.now()

def pure_format_time(time):
    return time.strftime("%Y-%m-%d %H:%M:%S")

"""Return a value"""

def impure_print_hello(name):
    print("Hello," +name)

def pure_get_greeting(name):
    return "Hello," + name
