"""Python has two built-in decorators @staticmethod and @classmethod to create static and class methods."""

"""Static Method"""

"""It belongs to class rather than instance, this means we can call the method in the class itself without needing an instance of the class"""

"""class MyClass:
    @staticmethod
    def my_static_method(arg1, arg2, arg3):
    
"""

class Add:
    @staticmethod
    def sum(x, y):
        return x + y

print(Add.sum(2,3))

"""Output : 5"""


"""Class Method"""

"""A class method is a method that belongs to a class rather than an instance of the class, but unlike a static method, it can access and modify the class methods"""


"""
class MyClass:
    @classmethod
    def my_class_method(cls, arg1, arg2):
        #function body

Note: It tokes any number of arguments including cls parameter, which refers to the class itself
"""

import datetime 
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    
    @classmethod
    def from_birth_year(cls, name, birth_year):
        age = datetime.date.today().year - birth_year
        return cls(name, age)


person = Person.from_birth_year('Alice', 1995)

print(person.age)

"""Output : 30"""

