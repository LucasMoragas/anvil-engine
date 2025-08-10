from abc import ABC, abstractmethod

from anvil_engine.models import Race


class RaceFactoryInterface(ABC):
  @abstractmethod
  def create_race(self, name: str, description: str, base_attributes: dict[str, int]) -> Race:
    pass
