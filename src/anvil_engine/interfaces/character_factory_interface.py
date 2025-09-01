from abc import ABC, abstractmethod

from anvil_engine.models import Character, Race


class CharacterFactoryInterface(ABC):
    @abstractmethod
    def create_character(
        self, name: str, age: int, gender: str, attributes: dict[str, int], race: Race
    ) -> Character:
        raise NotImplementedError
