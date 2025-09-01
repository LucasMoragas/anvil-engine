from anvil_engine.interfaces import RaceFactoryInterface
from anvil_engine.models import Race


class RaceFactory(RaceFactoryInterface):
    def create_race(
        self, name: str, description: str, base_attributes: dict[str, int]
    ) -> Race:
        return Race(name, description, base_attributes)

    def create_human(self) -> Race:
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
