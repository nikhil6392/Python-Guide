"""Class"""

"""It is a blueprint for creating objects with a set of attributes and methods"""

"""Creating a Class"""

class Person:
    pass

"""Attributes"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


"""Methods"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old")


"""Using a class"""

person1 = Person("Alice", 25)

person1.greet()


"""Output : Hello, my name is Alice and I am 25 years old"""

