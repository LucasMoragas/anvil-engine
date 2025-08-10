from abc import ABC, abstractmethod


class RaceInterface(ABC):
  @abstractmethod
  def get_name(self) -> str:
    pass

  @abstractmethod
  def get_description(self) -> str:
    pass

  @abstractmethod
  def get_base_attributes(self) -> dict[str, int]:
    pass

