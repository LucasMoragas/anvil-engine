# Contributing to Anvil Engine

Thank you for your interest in contributing to Anvil Engine! This document provides guidelines and information for contributors.

## 🚀 Getting Started

### Prerequisites

- Python 3.13+
- Poetry 1.0+
- Git

### Development Setup

1. **Fork and clone the repository**
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

4. **Run tests to ensure everything works**
   ```bash
   poetry run pytest
   ```

## 📝 Development Guidelines

### Code Style

We use **Ruff** for linting and formatting. Please ensure your code follows these standards:

```bash
# Check code style
poetry run ruff check .

# Format code
poetry run ruff format .

# Fix auto-fixable issues
poetry run ruff check --fix .
```

### Type Hints

All functions and methods should have proper type hints:

```python
def create_character(
    self, 
    name: str, 
    age: int, 
    gender: str, 
    attributes: dict[str, int], 
    race: Race
) -> Character:
    """Create a custom character with specified attributes."""
    pass
```

### Documentation

- Use docstrings for all public methods and classes
- Follow Google-style docstrings
- Include type information in docstrings

```python
def create_race(
    self, 
    name: str, 
    description: str, 
    base_attributes: dict[str, int]
) -> Race:
    """
    Create a custom race with specified attributes.
    
    Args:
        name: The race's name.
        description: A descriptive text about the race.
        base_attributes: Dictionary of base attribute values.
        
    Returns:
        Race: A new race instance with the specified parameters.
        
    Raises:
        ValueError: If validation fails.
    """
    pass
```

## 🧪 Testing

### Writing Tests

- Write tests for all new functionality
- Use descriptive test names
- Follow the AAA pattern (Arrange, Act, Assert)
- Use fixtures for common test data

```python
def test_create_race_with_valid_data(sample_race_data):
    """Test creating a race with valid data."""
    # Arrange
    factory = RaceFactory()
    
    # Act
    race = factory.create_race(**sample_race_data)
    
    # Assert
    assert race.name == sample_race_data["name"]
    assert race.description == sample_race_data["description"]
```

### Running Tests

```bash
# Run all tests
poetry run pytest

# Run with coverage
poetry run pytest --cov=anvil_engine

# Run specific test file
poetry run pytest tests/unit/models/test_race.py

# Run with verbose output
poetry run pytest -v
```

## 🏗️ Architecture Guidelines

### Factory Pattern

When adding new factories:

1. Create an interface in `interfaces/`
2. Implement the interface in `factories/`
3. Add tests for the factory
4. Update the main `__init__.py`

### Models

When adding new models:

1. Create an interface in `interfaces/`
2. Implement with Pydantic in `models/`
3. Add validation rules
4. Add comprehensive tests

### Validation

Use Pydantic for all validation:

```python
class Race(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)
    description: str = Field(..., min_length=10, max_length=500)
    base_attributes: dict[str, int] = Field(..., min_items=1)
    
    @field_validator('name')
    @classmethod
    def validate_name(cls, v: str) -> str:
        if not v.strip():
            raise ValueError('Race name cannot be empty')
        return v.strip().title()
```

## 📋 Pull Request Process

### Before Submitting

1. **Ensure tests pass**
   ```bash
   poetry run pytest
   ```

2. **Check code style**
   ```bash
   poetry run ruff check .
   poetry run ruff format .
   ```

3. **Update documentation** if needed

4. **Add tests** for new functionality

### PR Description

Include the following in your PR description:

- **What**: Brief description of changes
- **Why**: Reason for the changes
- **How**: Implementation details
- **Testing**: How you tested the changes

### Example PR Description

```markdown
## What
Add Dwarf race to the RaceFactory

## Why
Players requested more race options for character creation

## How
- Added `create_dwarf()` method to RaceFactory
- Implemented dwarf attributes (high strength/constitution, low agility)
- Added comprehensive tests

## Testing
- Added unit tests for dwarf creation
- Verified attribute values are correct
- All existing tests still pass
```

## 🐛 Bug Reports

When reporting bugs, please include:

1. **Environment details** (Python version, OS)
2. **Steps to reproduce**
3. **Expected behavior**
4. **Actual behavior**
5. **Error messages** (if any)

## 💡 Feature Requests

When requesting features:

1. **Describe the feature** clearly
2. **Explain the use case**
3. **Consider the impact** on existing code
4. **Suggest implementation** if you have ideas

## 📚 Resources

- [Python Type Hints](https://docs.python.org/3/library/typing.html)
- [Pydantic Documentation](https://pydantic.dev/)
- [Pytest Documentation](https://docs.pytest.org/)
- [Ruff Documentation](https://docs.astral.sh/ruff/)

## 🤝 Code of Conduct

Please be respectful and constructive in all interactions. We aim to create a welcoming environment for all contributors.

## 📞 Getting Help

- Open an issue for questions
- Join our discussions for general chat
- Check existing issues before creating new ones

Thank you for contributing to Anvil Engine! 🎮
