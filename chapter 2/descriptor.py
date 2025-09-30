"""Descriptors"""

"""They are a powerful feature that allows for the creation of objects that behave like variables"""

class Descriptor:
    def __get__(self, instance, owner):
        print("getting the attribute")
        return instance._value

    def __set__(self, instance, value):
        print("setting the value")
        instance._value = value
    
class Book:
    def __init__(self, name):
        self._value = name
    
    x = Descriptor()

obj = Book("The voice of people")
print(obj.x)