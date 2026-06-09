from abc import ABC, abstractmethod


class Character(ABC):
    """A class that represents a character"""
    @abstractmethod
    def __init__(self, first_name: str, is_alive: bool = True):
        """The constructor for the Character class"""
        self.first_name = first_name 
        self.is_alive = is_alive


    def die(self):
        """A method that makes the character die"""
        self.is_alive = False





class Stark(Character):
    """A class for the Starks family members"""
    def __init__(self, first_name: str, is_alive: bool = True):
        """The constructor for the Stark class"""
        self.first_name = first_name 
        self.is_alive = is_alive
        self.family_name = "Stark"
        self.eyes = "green"
        self.hairs = "brown"


    def __str__(self):
        """
        Depiction of the character
        """
        return f"Vector: ({self.family_name}, {self.eyes}, {self.hairs})"


    def __repr__(self):
        """
        Returns the string depicting the character.
        """
        return self.__str__()

                                                                                                                 