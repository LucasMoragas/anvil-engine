"""
Models module for the Anvil Engine RPG system.

This module contains the concrete implementations of characters and races
that implement the interfaces defined in the interfaces module. These
models represent the actual game entities with their attributes and
characteristics.
"""

from .character import Character
from .race import Race

__all__ = [
    "Character",
    "Race",
]
