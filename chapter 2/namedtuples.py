"""Features of Python"""

""" Named Tuples"""

"""It is a convenient and efficient way of creating lightweight, immutable objects with named fields"""

from collections import namedtuple

Car = namedtuple('Car', ['name', 'model', 'speed'])

car1 = Car(name='Austin Martin', model="Valhalla",speed="217MPH" )

print(f"{car1.name} , {car1.model}, {car1.speed}")

"""Output : Austin Martin , Valhalla, 217MPH"""

"""Reusability and Readability is prime here"""
""" Let's take another example of point"""

Point = namedtuple('Point', ['x', 'y'])

"""Calculate distance between two points"""

def distance(p1, p2):
    dx = p1.x - p2.x
    dy = p1.y - p2.y
    
    return (dx**2 + dy**2) ** 0.5

# take two random point

point1 = Point(x = 3, y = 3)
point2 = Point(x = 6, y = 8)

# Calculate the distance

d = distance(point1, point2)

print(f"The distance between {point1} and {point2} is {d:.2f}.")

"""Output: The distance between Point(x=3, y=3) and Point(x=6, y=8) is 5.83."""