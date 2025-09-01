from anvil_engine.interfaces import CharacterInterface
from anvil_engine.models import Race


class Character(CharacterInterface):
    def __init__(
        self, name: str, age: int, gender: str, attributes: dict[str, int], race: Race
    ):
        self.name = name
        self.age = age
        self.gender = gender
        self.attributes = attributes
        self.race = race

    def get_name(self) -> str:
        return self.name

    def get_age(self) -> int:
        return self.age

    def get_gender(self) -> str:
        return self.gender

    def get_attributes(self) -> dict[str, int]:
        return self.attributes

    def get_race(self) -> Race:
        return self.race
