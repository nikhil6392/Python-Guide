"""Inheritance"""

"""Class inheritance is the process of creating a new class that inherits properties from and existing class"""

"""The existing class is called `Parent Class` or the super class and the new class is called `Child Class` or `sub class` ."""

class Parent:
    def __init__(self):
        self.x = 1
    
    def parent_method(self):
        print("Parent method called")

class Child(Parent):
    pass

c = Child()
print(c.x)
print(c.parent_method())


"""Output: 1
          Parent method called
          None
"""

"""Overriding Parent Methods"""

class Child1(Parent):
    def parent_method(self):
        print("Child method called")

obj1 = Child1()
print(obj1.parent_method())

"""Output : Child Method Called 
            None
"""

"""Multiple Inheritance"""

class Parent1:
    def __init__(self):
        self.x = 1
    
    def parent1_method(self):
        print("Parent1 method Called")

class Parent2:
    def __init__(self):
        self.y = 2
    
    def parent2_method(self):
        print("Parent2 method called")

class Child2(Parent1, Parent2):
    pass

obj = Child2()
print(obj.parent1_method())
print(obj.parent2_method())

"""
    Output: Parent1 method called
            None
            Parent2 method called 
            None
"""