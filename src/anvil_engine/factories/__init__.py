"""
Factories module for the Anvil Engine RPG system.

This module contains factory classes that implement the Factory pattern
for creating characters and races. These factories provide both generic
creation methods and specialized methods for common character types
and races with predefined attributes.
"""

from .character_factory import CharacterFactory
from .race_factory import RaceFactory

__all__ = [
    "CharacterFactory",
    "RaceFactory",
]