from abc import ABC, abstractmethod

from anvil_engine.models import Race


class RaceFactoryInterface(ABC):
    """
    Abstract interface defining the contract for race factory objects.
    
    This interface ensures that all race factory implementations provide
    the necessary methods to create different types of races with
    predefined attributes and characteristics.
    """
    
    @abstractmethod
    def create_race(
        self, name: str, description: str, base_attributes: dict[str, int]
    ) -> Race:
        """
        Create a custom race with specified attributes.
        
        Args:
            name (str): The race's name.
            description (str): A descriptive text about the race.
            base_attributes (dict[str, int]): Dictionary of base attribute values.
            
        Returns:
            Race: A new race instance with the specified parameters.
        """
        raise NotImplementedError
