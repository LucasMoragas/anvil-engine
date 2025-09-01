"""
Interfaces module for the Anvil Engine RPG system.

This module contains all the abstract interfaces that define the contracts
for characters, races, and their factories. These interfaces ensure that
all implementations provide the necessary methods and maintain consistency
across the system.
"""

from .character_factory_interface import CharacterFactoryInterface
from .character_interface import CharacterInterface
from .race_factory_interface import RaceFactoryInterface
from .race_interface import RaceInterface

__all__ = [
    "CharacterFactoryInterface",
    "CharacterInterface",
    "RaceFactoryInterface",
    "RaceInterface",
]
