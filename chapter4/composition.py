"""Composition over inheritance"""

"""Inheritance and composition are two common approaches to designing object-oriented systems. Inheritance involves creating a subclass that inherits the behavior of its superclass. Composition involves creating objects that contain other objects."""

"""Benefits of Using Composition"""

"""Code reuse: It provides greater flexibility in designing objects. Objects can be composed of different objects to achieve a specific behavior"""

"""Flexibility: It provides greater flexibility in designing objects. Objects can be composed of different objects to achieve a specific behavior."""

"""Simplified class hierarchies: It can simplify class hierarchies by avoiding deep inheritance chains."""

"""Using Composition in Python"""

class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower
    
    def start(self):
        print("Engine Started")
    
    def stop(self):
        print("Engine Stopped")
    
class Transmission:
    def __init__(self, num_gears):
        self.num_gears = num_gears
    
    def shift_up(self):
        print("Shifted up")
    
    def shift_down(self):
        print("Shifted down")


class Car:
    def __init__(self, engine, transmission):
        self.engine = engine
        self.transmission = transmission
    
    def start(self):
        self.engine.start()
    
    def stop(self):
        self.engine.stop()
    
    def shift_up(self):
        self.transmission.shift_up()
    
    def shift_down(self):
        self.transmission.shift_down()
    

