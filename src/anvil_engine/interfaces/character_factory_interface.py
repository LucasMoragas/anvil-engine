from abc import ABC, abstractmethod

from anvil_engine.models import Character, Race


class CharacterFactoryInterface(ABC):
    """
    Abstract interface defining the contract for character factory objects.

    This interface ensures that all character factory implementations provide
    the necessary methods to create different types of characters with
    predefined attributes and characteristics.
    """

    @abstractmethod
    def create_character(
        self, name: str, age: int, gender: str, attributes: dict[str, int], race: Race
    ) -> Character:
        """
        Create a custom character with specified attributes.

        Args:
            name (str): The character's name.
            age (int): The character's age in years.
            gender (str): The character's gender.
            attributes (dict[str, int]): Dictionary of attribute scores.
            race (Race): The character's race object.

        Returns:
            Character: A new character instance with the specified parameters.
        """
        raise NotImplementedError
