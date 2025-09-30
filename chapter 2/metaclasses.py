"""MetaClasses"""

"""It is a powerful feature of python that allows us to modify the behavior of a class when it is defined"""

class MetaClass(type):
    def __new__(cls, name, bases, attrs):
        print("Creating class:", name)
        return super().__new__(cls, name, bases, attrs)

class TestClass(metaclass=MetaClass):
    pass
