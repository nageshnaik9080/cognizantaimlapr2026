import sys
import os
import pytest
from datetime import date

# Add project root to Python path
project_root = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')
)

sys.path.append(project_root)
from src.models import Corporate, Customer

@pytest.fixture
def initialize_corporate():
    corporate = Corporate(
        "CU003",
        "Acme Corp",
        "789 Oak St",
        "555-9012",
        "finance@acme.com",
        "topsecret",
        company_type="LLC",
    )
    return corporate

# Test for corporate object created
def test_corporate_creation(initialize_corporate):
    corporate = initialize_corporate
    assert isinstance(corporate, Customer)
    assert corporate.company_type == "LLC"

# Parameterized test for corporate object created
@pytest.mark.parametrize("name, company_type", [
    ("Acme Corp", "LLC"),
    ("XYZ Ltd", "Ltd"),
    ("Test Corp", "Corp")
])
def test_corporate_creation_parameterized(name, company_type):
    corporate = Corporate(
        "CU004", name, "123 St", "555-0000", "info@corp.com", "pass", company_type
    )
    assert corporate.name == name
    assert corporate.company_type == company_type



def test_corporate_creation():
    corporate = Corporate(
        "CU003",
        "Acme Corp",
        "789 Oak St",
        "555-9012",
        "finance@acme.com",
        "topsecret",
        company_type="LLC",
    )
    assert isinstance(corporate, Customer)
    assert corporate.name == "Acme Corp"
    assert corporate.company_type == "LLC"


def test_corporate_properties():
    corporate = Corporate(
        "CU004", "XYZ Ltd", "123 Business Rd", "555-2222", "info@xyz.com", "secret", "Ltd"
    )
    assert corporate.company_type == "Ltd"
    assert corporate.email == "info@xyz.com"


def test_corporate_repr():
    corporate = Corporate(
        "CU005", "Test Corp", "456 Corp St", "555-3333", "test@corp.com", "pwd", "Corp"
    )
    repr_str = repr(corporate)
    assert "Test Corp" in repr_str
    assert "Corp" in repr_str

if __name__ == "__main__":
    import pytest
    pytest.main([__file__])
