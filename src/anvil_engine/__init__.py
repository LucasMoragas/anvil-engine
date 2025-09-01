"""
Anvil Engine - A backend service demonstrating the Factory pattern for RPG character creation and management.

This package provides a complete implementation of the Factory pattern for creating
RPG characters and races with predefined attributes and characteristics. It focuses
on software architecture and design patterns implementation.

Main Components:
- Interfaces: Abstract contracts for characters, races, and factories
- Models: Concrete implementations of characters and races
- Factories: Factory classes for creating different types of entities

Example Usage:
    from anvil_engine.factories import CharacterFactory, RaceFactory
    from anvil_engine.models import Character, Race
    
    # Create factories
    char_factory = CharacterFactory()
    race_factory = RaceFactory()
    
    # Create a race
    human = race_factory.create_human()
    
    # Create a character
    warrior = char_factory.create_warrior("Aragorn", 87, "male", human)
"""

from .interfaces import (
    CharacterInterface,
    RaceInterface,
    CharacterFactoryInterface,
    RaceFactoryInterface,
)
from .models import Character, Race
from .factories import CharacterFactory, RaceFactory

__version__ = "0.1.0"
__author__ = "Lucas Moragas"

__all__ = [
    # Interfaces
    "CharacterInterface",
    "RaceInterface", 
    "CharacterFactoryInterface",
    "RaceFactoryInterface",
    # Models
    "Character",
    "Race",
    # Factories
    "CharacterFactory",
    "RaceFactory",
]
