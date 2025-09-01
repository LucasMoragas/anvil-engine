from anvil_engine.interfaces import RaceFactoryInterface
from anvil_engine.models import Race


class RaceFactory(RaceFactoryInterface):
    """
    Factory class for creating different types of races in the RPG system.
    
    This factory implements the Factory pattern to create races with
    predefined attribute sets and characteristics. It provides both
    generic race creation and specialized methods for common races
    like humans and elves.
    """
    
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
        return Race(name, description, base_attributes)

    def create_human(self) -> Race:
        """
        Create a human race with balanced attributes.
        
        Humans are known for their adaptability and versatility,
        providing balanced attribute bonuses that make them suitable
        for any character class or playstyle.
        
        Returns:
            Race: A new human race with balanced base attributes.
        """
        return self.create_race(
            name="Human",
            description="Adaptable and ambitious, standard for all races",
            base_attributes={
                "strength": 10,
                "agility": 10,
                "intelligence": 10,
                "wisdom": 10,
                "dexterity": 10,
                "constitution": 10,
                "charisma": 10,
            },
        )

    def create_elf(self) -> Race:
        """
        Create an elf race with agility and intelligence focus.
        
        Elves are known for their grace, intelligence, and connection
        to nature. They excel in agility, intelligence, and dexterity,
        making them ideal for classes that rely on these attributes.
        
        Returns:
            Race: A new elf race with agility and intelligence focus.
        """
        return self.create_race(
            name="Elf",
            description="Intelligent and graceful, with a deep connection to nature",
            base_attributes={
                "strength": 8,
                "agility": 12,
                "intelligence": 12,
                "wisdom": 10,
                "dexterity": 12,
                "constitution": 8,
                "charisma": 8,
            },
        )
