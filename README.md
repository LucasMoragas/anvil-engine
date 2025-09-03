# 🛡️ Anvil Engine

[![Python](https://img.shields.io/badge/Python-3.13+-blue.svg)](https://python.org)
[![Poetry](https://img.shields.io/badge/Poetry-1.0+-green.svg)](https://python-poetry.org)
[![Ruff](https://img.shields.io/badge/Ruff-0.12+-orange.svg)](https://github.com/astral-sh/ruff)
[![Pydantic](https://img.shields.io/badge/Pydantic-2.0+-red.svg)](https://pydantic.dev)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.116+-teal.svg)](https://fastapi.tiangolo.com)

> A backend service demonstrating the Factory pattern for RPG character creation and management. Focuses on software architecture and design patterns implementation.

## 📋 Table of Contents

- [Features](#-features)
- [Architecture](#-architecture)
- [Installation](#-installation)
- [Quick Start](#-quick-start)
- [Usage Examples](#-usage-examples)
- [Testing](#-testing)
- [Development](#-development)
- [API Reference](#-api-reference)
- [Contributing](#-contributing)
- [License](#-license)

## ✨ Features

- **🏭 Factory Pattern Implementation**: Clean separation of object creation logic
- **🔒 Type Safety**: Full type hints with Pydantic validation
- **🧪 Comprehensive Testing**: Unit and integration tests with pytest
- **📚 Clean Architecture**: Interfaces, models, and factories separation
- **⚡ Fast Development**: Ruff linting and formatting
- **🎮 RPG System**: Character and race management with attributes
- **🔧 Extensible Design**: Easy to add new races and character classes

## 🏗️ Architecture

The project follows a clean architecture pattern with clear separation of concerns:

```
anvil-engine/
├── src/anvil_engine/
│   ├── interfaces/          # Abstract contracts
│   │   ├── character_interface.py
│   │   ├── race_interface.py
│   │   ├── character_factory_interface.py
│   │   └── race_factory_interface.py
│   ├── models/              # Concrete implementations
│   │   ├── character.py
│   │   └── race.py
│   ├── factories/           # Factory pattern implementation
│   │   ├── character_factory.py
│   │   └── race_factory.py
│   └── __init__.py
├── tests/                   # Test suite
│   ├── unit/               # Unit tests
│   ├── integration/        # Integration tests
│   └── conftest.py         # Shared fixtures
├── pyproject.toml          # Project configuration
└── README.md
```

### Design Patterns Used

- **Factory Pattern**: Centralized object creation
- **Interface Segregation**: Clean contracts for implementations
- **Dependency Inversion**: High-level modules don't depend on low-level modules

## 🚀 Installation

### Prerequisites

- Python 3.13+
- Poetry 1.0+

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/anvil-engine.git
   cd anvil-engine
   ```

2. **Install dependencies**
   ```bash
   poetry install
   ```

3. **Activate the virtual environment**
   ```bash
   poetry shell
   ```

## 🎯 Quick Start

```python
from anvil_engine.factories import CharacterFactory, RaceFactory

# Create factories
race_factory = RaceFactory()
char_factory = CharacterFactory()

# Create a race
human = race_factory.create_human()

# Create a character
warrior = char_factory.create_warrior("Aragorn", 87, "male", human)

print(f"Created {warrior.get_name()}, a {warrior.get_race().get_name()} warrior")
```

## 📖 Usage Examples

### Creating Races

```python
from anvil_engine.factories import RaceFactory

factory = RaceFactory()

# Create predefined races
human = factory.create_human()
elf = factory.create_elf()

# Create custom race
custom_race = factory.create_race(
    name="Dragonborn",
    description="Descendants of dragons with natural magical abilities",
    base_attributes={
        "strength": 12,
        "agility": 8,
        "intelligence": 10,
        "wisdom": 10,
        "dexterity": 8,
        "constitution": 12,
        "charisma": 12,
    }
)
```

### Creating Characters

```python
from anvil_engine.factories import CharacterFactory, RaceFactory

race_factory = RaceFactory()
char_factory = CharacterFactory()

# Create a race
elf = race_factory.create_elf()

# Create different character classes
archer = char_factory.create_archer("Legolas", 2931, "male", elf)
warrior = char_factory.create_warrior("Gimli", 139, "male", elf)

# Create custom character
custom_char = char_factory.create_character(
    name="Gandalf",
    age=2019,
    gender="male",
    attributes={
        "strength": 8,
        "agility": 10,
        "intelligence": 18,
        "wisdom": 18,
        "dexterity": 12,
        "constitution": 14,
        "charisma": 16,
    },
    race=elf
)
```

### Working with Models

```python
from anvil_engine.models import Character, Race

# Direct model creation (with validation)
race = Race(
    name="Halfling",
    description="Small, brave folk known for their courage",
    base_attributes={
        "strength": 8,
        "agility": 12,
        "intelligence": 10,
        "wisdom": 10,
        "dexterity": 12,
        "constitution": 10,
        "charisma": 10,
    }
)

character = Character(
    name="Bilbo",
    age=50,
    gender="male",
    attributes={
        "strength": 8,
        "agility": 12,
        "intelligence": 12,
        "wisdom": 10,
        "dexterity": 12,
        "constitution": 10,
        "charisma": 14,
    },
    race=race
)

# Access character information
print(f"Name: {character.get_name()}")
print(f"Age: {character.get_age()}")
print(f"Race: {character.get_race().get_name()}")
print(f"Attributes: {character.get_attributes()}")
```

## 🧪 Testing

### Run All Tests

```bash
poetry run pytest
```

### Run Specific Test Types

```bash
# Unit tests only
poetry run pytest tests/unit/

# Integration tests only
poetry run pytest tests/integration/

# With coverage
poetry run pytest --cov=anvil_engine

# With verbose output
poetry run pytest -v
```

### Test Structure

- **Unit Tests**: Test individual components in isolation
- **Integration Tests**: Test component interactions
- **Fixtures**: Shared test data and setup

## 🛠️ Development

### Code Quality

```bash
# Lint code
poetry run ruff check .

# Format code
poetry run ruff format .

# Fix auto-fixable issues
poetry run ruff check --fix .

# Check and format in one command
poetry run ruff check --fix . && poetry run ruff format .
```

### Development Workflow

1. **Create a feature branch**
   ```bash
   git checkout -b feature/new-race
   ```

2. **Make changes and test**
   ```bash
   poetry run ruff check --fix .
   poetry run pytest
   ```

3. **Commit changes**
   ```bash
   git add .
   git commit -m "feat: add new race type"
   ```

4. **Push and create PR**
   ```bash
   git push origin feature/new-race
   ```

## 📚 API Reference

### RaceFactory

#### Methods

- `create_race(name, description, base_attributes)` - Create custom race
- `create_human()` - Create human race with balanced attributes
- `create_elf()` - Create elf race with agility/intelligence focus

### CharacterFactory

#### Methods

- `create_character(name, age, gender, attributes, race)` - Create custom character
- `create_archer(name, age, gender, race)` - Create archer with optimized attributes
- `create_warrior(name, age, gender, race)` - Create warrior with strength focus

### Models

#### Race

- `get_name()` - Get race name
- `get_description()` - Get race description
- `get_base_attributes()` - Get base attribute modifiers

#### Character

- `get_name()` - Get character name
- `get_age()` - Get character age
- `get_gender()` - Get character gender
- `get_attributes()` - Get character attributes
- `get_race()` - Get character's race

## 🎮 RPG System Details

### Attributes

All characters and races use the following attribute system:

- **Strength**: Physical power and melee damage
- **Agility**: Speed and evasion
- **Intelligence**: Magical ability and problem solving
- **Wisdom**: Perception and magical resistance
- **Dexterity**: Accuracy and finesse
- **Constitution**: Health and endurance
- **Charisma**: Leadership and social interaction

### Race Bonuses

- **Human**: Balanced (+0 to all attributes)
- **Elf**: Agility (+2), Intelligence (+2), Dexterity (+2), Strength (-2), Constitution (-2), Charisma (-2)

### Character Classes

- **Archer**: High Intelligence (13), Charisma (14), low Constitution (6)
- **Warrior**: High Strength (15), Constitution (14), low Charisma (4)

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

### Development Setup

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Ensure all tests pass
6. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Authors

- **Lucas Moragas Melo Oliveira** - *Initial work* - [moragaslucas08@gmail.com](mailto:moragaslucas08@gmail.com)

## 🙏 Acknowledgments

- Inspired by classic RPG systems
- Built with modern Python best practices
- Uses the Factory pattern for clean architecture

---

**Made with ❤️ for the RPG community**
