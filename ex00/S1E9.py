from abc import ABC, abstractmethod


class Character(ABC):
    """
    A class that represents a character
    """
    @abstractmethod
    

    def __init__(self, _first_name: str, _is_alive: Optional[bool] = True):
        """
        The constructor for the Character class
        """
        self.first_name = _first_name 
        self.is_alive = _is_alive


    def die(self)
        """
        A method that makes the character die
        """
        self.is_alive = False


class Stark(Character):
    """
    A class for the Starks family members
    """
    def __init__(self, _first_name: str, _is_alive: bool):
        """
        The constructor for the Stark class
        """
        self = Character(_first_name, _is_alive)

