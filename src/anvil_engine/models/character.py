from typing import Any

from pydantic import BaseModel, Field

from anvil_engine.interfaces import CharacterInterface
from anvil_engine.models import Race


class Character(CharacterInterface, BaseModel):
    """
    Concrete implementation of a character in the RPG system.

    A character represents a playable entity with specific attributes,
    personal information, and racial characteristics. Characters can
    be of different classes and races, each affecting their abilities
    and gameplay experience.
    """

    name: str = Field(
        ..., min_length=3, max_length=50, description="The character's name."
    )
    age: int = Field(..., description="The character's age in years.")
    gender: str = Field(..., description="The character's gender.")
    attributes: dict[str, int] = Field(
        ..., description="Dictionary of attribute scores."
    )
    race: Race = Field(..., description="The character's race object.")

    def __init__(self, **data: Any):
        super().__init__(**data)

    def get_name(self) -> str:
        """
        Get the character's name.

        Returns:
            str: The character's name.
        """
        return self.name

    def get_age(self) -> int:
        """
        Get the character's age.

        Returns:
            int: The character's age in years.
        """
        return self.age

    def get_gender(self) -> str:
        """
        Get the character's gender.

        Returns:
            str: The character's gender.
        """
        return self.gender

    def get_attributes(self) -> dict[str, int]:
        """
        Get the character's attribute scores.

        Returns:
            dict[str, int]: Dictionary mapping attribute names to their values.
        """
        return self.attributes

    def get_race(self) -> Race:
        """
        Get the character's race.

        Returns:
            Race: The race object associated with this character.
        """
        return self.race
