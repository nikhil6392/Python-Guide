"""Class Design"""

"""Clean, readable classes"""

class Car:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def get_name(self):
        return self.name
    
    def get_price(self):
        return self.price
    

"""Single Responsibility Principle (SRP)"""

"""A class should have only one responsibility."""

class Calculator:
    def add(self, a, b):
        return a + b
    
    def sub(self, a, b):
        return a - b


x = Calculator()

print(x.add(2, 6))  # Output : 8


"""Follow PEP 8 guide"""

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width
    
    