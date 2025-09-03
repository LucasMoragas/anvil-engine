"""
Shared fixtures for Anvil Engine tests.

This module contains pytest fixtures that can be used across
all test modules in the project.
"""

import pytest

from anvil_engine.factories import CharacterFactory, RaceFactory


@pytest.fixture
def race_factory():
    """Provide a RaceFactory instance for testing."""
    return RaceFactory()


@pytest.fixture
def character_factory():
    """Provide a CharacterFactory instance for testing."""
    return CharacterFactory()


@pytest.fixture
def human_race(race_factory):
    """Provide a human race for testing."""
    return race_factory.create_human()


@pytest.fixture
def elf_race(race_factory):
    """Provide an elf race for testing."""
    return race_factory.create_elf()


@pytest.fixture
def sample_attributes():
    """Provide sample character attributes for testing."""
    return {
        "strength": 10,
        "agility": 10,
        "intelligence": 10,
        "wisdom": 10,
        "dexterity": 10,
        "constitution": 10,
        "charisma": 10,
    }


@pytest.fixture
def sample_character_data(sample_attributes):
    """Provide sample character data for testing."""
    return {
        "name": "Test Character",
        "age": 25,
        "gender": "male",
        "attributes": sample_attributes,
    }


@pytest.fixture
def sample_race_data():
    """Provide sample race data for testing."""
    return {
        "name": "Test Race",
        "description": "A test race for unit testing purposes",
        "base_attributes": {
            "strength": 8,
            "agility": 12,
            "intelligence": 10,
            "wisdom": 10,
            "dexterity": 10,
            "constitution": 10,
            "charisma": 10,
        },
    }
