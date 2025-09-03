from abc import ABC, abstractmethod

from anvil_engine.models import Race


class CharacterInterface(ABC):
    """
    Abstract interface defining the contract for character objects in the RPG system.

    This interface ensures that all character implementations provide the necessary
    methods to retrieve character information including basic details, attributes,
    and race information.
    """

    @abstractmethod
    def get_name(self) -> str:
        """
        Get the character's name.

        Returns:
            str: The character's name.
        """
        raise NotImplementedError

    @abstractmethod
    def get_age(self) -> int:
        """
        Get the character's age.

        Returns:
            int: The character's age in years.
        """
        raise NotImplementedError

    @abstractmethod
    def get_gender(self) -> str:
        """
        Get the character's gender.

        Returns:
            str: The character's gender (e.g., 'male', 'female', 'non-binary').
        """
        raise NotImplementedError

    @abstractmethod
    def get_attributes(self) -> dict[str, int]:
        """
        Get the character's attribute scores.

        Returns:
            dict[str, int]: Dictionary mapping attribute names to their values.
                           Keys include: strength, agility, intelligence, wisdom,
                           dexterity, constitution, charisma.
        """
        raise NotImplementedError

    @abstractmethod
    def get_race(self) -> Race:
        """
        Get the character's race.

        Returns:
            Race: The race object associated with this character.
        """
        raise NotImplementedError
