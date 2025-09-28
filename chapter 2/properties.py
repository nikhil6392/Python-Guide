"""Properties"""

"""Properties can be used to validate or
   sanitize input, calculate derived values, or trigger side effects, all while providing a clean and intuitive interface for accessing and modifying object state.
"""

class Square:
    def __init__(self, width):
        self.width = width

    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError("Width must be positive")
        self._width = value
    
    @property
    def area(self):
        return self._width * self._width
    
