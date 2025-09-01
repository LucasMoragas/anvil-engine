from abc import ABC, abstractmethod

from anvil_engine.models import Race


class CharacterInterface(ABC):
    @abstractmethod
    def get_name(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def get_age(self) -> int:
        raise NotImplementedError

    @abstractmethod
    def get_gender(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def get_attributes(self) -> dict[str, int]:
        raise NotImplementedError

    @abstractmethod
    def get_race(self) -> Race:
        raise NotImplementedError
