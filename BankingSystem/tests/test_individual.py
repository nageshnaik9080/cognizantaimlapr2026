import sys
import os
import pytest
from datetime import date

# Add project root to Python path
project_root = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')
)

sys.path.append(project_root)
from datetime import date

from src.models import Individual, Customer

@pytest.fixture
def initialize_individual():
    individual = Individual(
        "CU002",
        "Bob",
        "456 Elm St",
        "555-5678",
        "bob@example.com",
        "password",
        surname="Smith",
        gender="M",
        date_of_birth=date(1990, 1, 1),
    )
    return individual

# Test for individual object created
def test_individual_creation(initialize_individual):
    individual = initialize_individual
    assert isinstance(individual, Customer)
    assert individual.surname == "Smith"

# Parameterized test for individual object created
@pytest.mark.parametrize("name, surname, gender", [
    ("Bob", "Smith", "M"),
    ("Alice", "Doe", "F"),
    ("John", "Johnson", "M")
])
def test_individual_creation_parameterized(name, surname, gender):
    individual = Individual(
        "CU003", name, "123 St", "555-0000", "test@example.com", "pass",
        surname, gender, date(1990, 1, 1)
    )
    assert individual.name == name
    assert individual.surname == surname
    assert individual.gender == gender



def test_individual_creation():
    individual = Individual(
        "CU002",
        "Bob",
        "456 Elm St",
        "555-5678",
        "bob@example.com",
        "password",
        surname="Smith",
        gender="M",
        date_of_birth=date(1990, 1, 1),
    )
    assert isinstance(individual, Customer)
    assert individual.surname == "Smith"
    assert individual.gender == "M"
    assert individual.date_of_birth == date(1990, 1, 1)


def test_individual_age():
    individual = Individual(
        "CU003", "Alice", "123 St", "555-0000", "alice@example.com", "pass",
        "Doe", "F", date(2000, 5, 15)
    )
    age = individual.work_out_age()
    assert age >= 25  # Depending on current date


def test_individual_repr():
    individual = Individual(
        "CU004", "John", "456 Ave", "555-1111", "john@example.com", "pwd",
        "Doe", "M", date(1985, 3, 10)
    )
    repr_str = repr(individual)
    assert "John" in repr_str
    assert "Doe" in repr_str

if __name__ == "__main__":
    import pytest
    pytest.main([__file__])
