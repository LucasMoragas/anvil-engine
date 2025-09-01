from anvil_engine.interfaces import CharacterFactoryInterface
from anvil_engine.models import Character, Race


class CharacterFactory(CharacterFactoryInterface):
  def create_character(self, name: str, age: int, gender: str, attributes: dict[str, int], race: Race) -> Character:
    return Character(name, age, gender, attributes, race)

  def create_archer(self, name: str, age: int, gender: str, race: Race) -> Character:
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
      race=race
    )
    
  def create_warrior(self, name: str, age: int, gender: str, race: Race) -> Character:
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
      race=race
    )
