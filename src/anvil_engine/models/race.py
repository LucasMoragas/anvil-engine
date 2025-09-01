from anvil_engine.interfaces import RaceInterface


class Race(RaceInterface):
    """
    Concrete implementation of a race in the RPG system.
    
    A race represents a species or ethnic group that provides
    base attributes and characteristics to characters. Different
    races offer various bonuses and penalties to character
    attributes, affecting gameplay and character development.
    """
    
    def __init__(self, name: str, description: str, base_attributes: dict[str, int]):
        """
        Initialize a new race.
        
        Args:
            name (str): The race's name.
            description (str): A descriptive text about the race.
            base_attributes (dict[str, int]): Dictionary of base attribute values.
        """
        self.name = name
        self.description = description
        self.base_attributes = base_attributes

    def get_name(self) -> str:
        """
        Get the race's name.
        
        Returns:
            str: The race's name.
        """
        return self.name

    def get_description(self) -> str:
        """
        Get the race's description.
        
        Returns:
            str: A descriptive text about the race.
        """
        return self.description

    def get_base_attributes(self) -> dict[str, int]:
        """
        Get the race's base attribute values.
        
        Returns:
            dict[str, int]: Dictionary mapping attribute names to their base values.
        """
        return self.base_attributes
