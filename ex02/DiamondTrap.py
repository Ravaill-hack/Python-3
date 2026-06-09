from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """A class for the king"""
    def __init__(self, first_name: str, is_alive: bool = True):
        """The constructor for the Baratheon class"""
        super().__init__(first_name, is_alive)

    def set_eyes(self, eyes: str):
        """Redefine the color of the eyes"""
        self.eyes = eyes

    def set_hairs(self, hairs: str):
        """Redefine the color of the hair"""
        self.hairs = hairs

    def get_eyes(self) -> str:
        """Return the colour of the eyes"""
        return (self.eyes)

    def get_hairs(self) -> str:
        """Return the colour of the hair"""
        return (self.hairs)
