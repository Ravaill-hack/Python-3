from S1E9 import Character


class Baratheon(Character):
    """A class for the Baratheon family members"""
    def __init__(self, first_name: str, is_alive: bool = True):
        """The constructor for the Baratheon class"""
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self):
        """Depiction of the character"""
        return f"Vector: ({self.family_name}, {self.eyes}, {self.hairs})"

    def __repr__(self):
        """Returns the string depicting the character."""
        return self.__str__()


class Lannister(Character):
    """A class for the Lannister family members"""
    def __init__(self, first_name: str, is_alive: bool = True):
        """The constructor for the Lannister class"""
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def __str__(self):
        """Depiction of the character"""
        return f"Vector: ({self.family_name}, {self.eyes}, {self.hairs})"

    def __repr__(self):
        """Returns the string depicting the character."""
        return self.__str__()

    @classmethod
    def create_lannister(cls, first_name: str, is_alive: bool = True):
        new_character = cls(first_name, is_alive)
        return (new_character)
