from anvil_engine.interfaces import CharacterFactoryInterface
from anvil_engine.models import Character, Race


class CharacterFactory(CharacterFactoryInterface):
    """
    Factory class for creating different types of characters in the RPG system.

    This factory implements the Factory pattern to create characters with
    predefined attribute sets for different character classes. It provides
    both generic character creation and specialized methods for common
    character types like archers and warriors.
    """

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
        try:
            return Character(name, age, gender, attributes, race)
        except Exception as e:
            raise ValueError(f"Error creating character: {e}") from e

    def create_archer(self, name: str, age: int, gender: str, race: Race) -> Character:
        """
        Create an archer character with optimized attributes for ranged combat.

        Archers are specialized in agility, dexterity, and intelligence,
        making them effective at long-range attacks and tactical positioning.

        Args:
            name (str): The character's name.
            age (int): The character's age in years.
            gender (str): The character's gender.
            race (Race): The character's race object.

        Returns:
            Character: A new archer character with optimized attributes.
        """
        try:
            return self.create_character(
                name,
                age,
                gender,
                attributes={
                    "strength": 7,
                    "agility": 10,
                    "intelligence": 13,
                    "wisdom": 10,
                    "dexterity": 10,
                    "constitution": 6,
                    "charisma": 14,
                },
                race=race,
            )
        except Exception as e:
            raise ValueError(f"Error creating archer: {e}") from e

    def create_warrior(self, name: str, age: int, gender: str, race: Race) -> Character:
        """
        Create a warrior character with optimized attributes for melee combat.

        Warriors excel in strength and constitution, making them durable
        frontline fighters capable of withstanding heavy damage while
        dealing significant melee damage.

        Args:
            name (str): The character's name.
            age (int): The character's age in years.
            gender (str): The character's gender.
            race (Race): The character's race object.

        Returns:
            Character: A new warrior character with optimized attributes.
        """
        try:
            return self.create_character(
                name,
                age,
                gender,
                attributes={
                    "strength": 15,
                    "agility": 9,
                    "intelligence": 8,
                    "wisdom": 9,
                    "dexterity": 11,
                    "constitution": 14,
                    "charisma": 4,
                },
                race=race,
            )
        except Exception as e:
            raise ValueError(f"Error creating warrior: {e}") from e
