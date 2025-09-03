from typing import Any

from pydantic import BaseModel, Field

from anvil_engine.interfaces import RaceInterface


class Race(RaceInterface, BaseModel):
    """
    Concrete implementation of a race in the RPG system.

    A race represents a species or ethnic group that provides
    base attributes and characteristics to characters. Different
    races offer various bonuses and penalties to character
    attributes, affecting gameplay and character development.
    """

    name: str = Field(..., min_length=3, max_length=50, description="The race's name.")
    description: str = Field(
        ...,
        min_length=3,
        max_length=500,
        description="A descriptive text about the race.",
    )
    base_attributes: dict[str, int] = Field(
        ..., description="Dictionary of base attribute values."
    )

    def __init__(self, **data: Any):
        super().__init__(**data)

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
