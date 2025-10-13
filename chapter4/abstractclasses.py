"""Abstract Base classes"""

"""An abstract base class is a class that cannot be instantiated and is meant to serve as a blueprint for other classes."""

"""Creating an Abstract Base Class"""

import abc

class Shape(metaclass = abc.ABCMeta):
    @abc.abstractmethod
    def area(self):
        pass

    @abc.abstractmethod
    def perimeter(self):
        pass


"""Creating a Concrete Subclass"""

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2*(self.length + self.width)


"""Using ABC"""

def print_shape_info(shape):
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")

rectangle = Rectangle(3,5)
print_shape_info(rectangle)