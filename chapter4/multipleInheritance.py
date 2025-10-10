"""Multiple Inheritance"""

"""It is the process of creating a new class that inherits properties from multiple parent classes"""


class Parent1:
    def parent1_method(self):
        print("Parent 1 method called")

class Parent2:
    def parent2_method(self):
        print("Parent 2 class method")

class Child(Parent1, Parent2):
    pass

obj = Child()
print(obj.parent1_method())

"""Output : Parent 1 method called
            None
"""

print(obj.parent2_method())

"""
    Output: Parent 2 method called
            None
"""

"""Method Resolution Order(MRO)"""

print(Child.mro())

"""Output : [<class '__main__.Child'>, <class '__main__.Parent1'>, <class '__main__.Parent2'>, <class 'object'>]"""

"""Diamond Inheritance"""

"""Case: It is possible that a class inherits two class , which inherits same Parent class. This is called Diamond Inheritance"""

class GrandParent:
    def grand_parent_method(self):
        print("Grand Parent method called")

class Parent1(GrandParent):
    pass

class Parent2(GrandParent):
    pass

class Child(Parent1, Parent2):
    pass

obj1 = Child()
obj1.grand_parent_method()

"""Output : Grand Parent method called"""