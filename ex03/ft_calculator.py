class calculator:
    """A class that is able to do calculations of a vector with a scalar"""

    def __init__(self, vector):
        """Stores the value of the vector"""
        self.vector = vector

    def __add__(self, object) -> None:
        """Adds the scalar to the vector"""
        self.vector = [nb + object for nb in self.vector]
        print(self.vector)

    def __mul__(self, object) -> None:
        """Multiplies the scalar with the vector"""
        self.vector = [nb * object for nb in self.vector]
        print(self.vector)

    def __sub__(self, object) -> None:
        """Substracts the scalar from the vector"""
        self.vector = [nb - object for nb in self.vector]
        print(self.vector)

    def __truediv__(self, object) -> None:
        """Divide the vector by the scalar"""
        try:
            assert object != 0
            self.vector = [nb / object for nb in self.vector]
            print(self.vector)
        except AssertionError:
            print("AssertionError: Division by zero")
