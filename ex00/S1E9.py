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
    """A class for the Stark family members"""
    def __init__(self, first_name: str, is_alive: bool = True):
        """The constructor for the Stark class"""
        super().__init__(first_name, is_alive)
        self.family_name = "Stark"
