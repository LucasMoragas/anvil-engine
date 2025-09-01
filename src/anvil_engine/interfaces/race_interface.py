from abc import ABC, abstractmethod


class RaceInterface(ABC):
    @abstractmethod
    def get_name(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def get_description(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def get_base_attributes(self) -> dict[str, int]:
        raise NotImplementedError
