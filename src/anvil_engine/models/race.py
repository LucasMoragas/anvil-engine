from anvil_engine.interfaces import RaceInterface


class Race(RaceInterface):
  def __init__(self, name: str, description: str, base_attributes: dict[str, int]):
    self.name = name
    self.description = description
    self.base_attributes = base_attributes

  def get_name(self) -> str:
    return self.name

  def get_description(self) -> str:
    return self.description

  def get_base_attributes(self) -> dict[str, int]:
    return self.base_attributes
