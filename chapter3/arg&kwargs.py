""" *args and **kwargs to define functions
    that can accept an arbitrary number of arguments and keyword arguments respectively.
"""

def my_function(*args):
    for arg in args:
        print(arg)
my_function(1,2,3)
my_function('a', 'b', 'c', 'd')

"""**kwargs is used to pass a variable number of keyword
   arguments to a function.
   When you use it in a function definition, it tell python to collect any remaining keyword arguments into a dictionary.
"""

def my_function(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

my_function(name="Nikhil", age=23)
my_function()


"""We can create *args and **kwargs to create
   functions that can accept both positional and
   keyword arguments
"""

def positional_keywords(*args, **kwargs):

    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(f"{key}: {value}")

positional_keywords(1,2,3, name="Nikhil", age=23)

