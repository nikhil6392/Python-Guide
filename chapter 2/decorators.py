"""Decorators"""

"""A decorator is a callable object that takes another
   function or class as its argument and returns a new function or class.
"""

import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()

        print(f"{func.__name__} took {end_time - start_time} seconds to run.")

        return result
    return wrapper

@timing_decorator
def long_running_function():
    time.sleep(2)

long_running_function()

"""Output : long_running_function took 2.000133514404297 seconds to run."""

"""the time_decorator function takes a function as an argument, creates a new function called wrapper, returns it. the wrapper function uses the time module to measure the time takes by the original function to execute and prints it to the console"""


""" Decorators can be used to add functionality to a class."""

def add_logging(cls):
    def log(self, message):
        print(f"{cls.__name__}: {message}")
    cls.log = log
    return cls

@add_logging
class MyClass:
    pass


obj = MyClass()
obj.log("Hello, World!")

"""Output : MyClass: Hello, World!"""