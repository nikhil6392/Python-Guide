"""Metaclasses"""

"""It is a class that defines the behavior of other classes."""

"""Creating a metaclass"""

class MyMeta(type):
    def __new__(cls, name, bases, attrs):
        print(f"Creating class {name} with bases {bases}and attrs {attrs}")

        return super().__new__(cls, name, bases, attrs)

"""
    Where -> cls : metaclass itself
             name : name of new class
             bases : A tuple of the base classes for the new class
             attrs : A dictionary of the attributes and methods of the new class
"""

"""Using metaclass"""

class MyClass(metaclass=MyMeta):
    x = 42
