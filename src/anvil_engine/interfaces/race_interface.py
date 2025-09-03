from abc import ABC, abstractmethod


class RaceInterface(ABC):
    """
    Abstract interface defining the contract for race objects in the RPG system.

    This interface ensures that all race implementations provide the necessary
    methods to retrieve race information including name, description, and
    base attribute modifiers.
    """

    @abstractmethod
    def get_name(self) -> str:
        """
        Get the race's name.

        Returns:
            str: The race's name (e.g., 'Human', 'Elf', 'Dwarf').
        """
        raise NotImplementedError

    @abstractmethod
    def get_description(self) -> str:
        """
        Get the race's description.

        Returns:
            str: A descriptive text explaining the race's characteristics,
                 lore, and general traits.
        """
        raise NotImplementedError

    @abstractmethod
    def get_base_attributes(self) -> dict[str, int]:
        """
        Get the race's base attribute modifiers.

        Returns:
            dict[str, int]: Dictionary mapping attribute names to their base values.
                           These values represent the racial bonuses or penalties
                           applied to character attributes.
        """
        raise NotImplementedError
