import sys
import os
import pytest

# Add project root to Python path
project_root = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')
)

sys.path.append(project_root)
from src.models import Customer


@pytest.fixture
def initialize_customer():
    customer = Customer("CU001", "Alice", "123 Main St", "555-1234", "alice@example.com", "secret")
    return customer



# Test for customer object created
def test_customer_creation(initialize_customer):
    customer = initialize_customer
    assert customer.account_number == "CU001"
    assert customer.name == "Alice"


# Parameterized test for customer object created
@pytest.mark.parametrize("account_number, name, address, contact_number, email, password", [
    ("CU001", "Alice", "123 Main St", "555-1234", "alice@example.com", "secret"),
    ("CU002", "Bob", "456 Elm", "555-5678", "bob@example.com", "pass"),
    ("CU003", "Charlie", "789 Oak", "555-9012", "charlie@example.com", "pwd")
])
def test_customer_creation_parameterized(account_number, name, address, contact_number, email, password):
    customer = Customer(account_number=account_number, name=name, address=address, contact_number=contact_number, email=email, password=password)
    assert customer.account_number == account_number
    assert customer.name == name



if __name__ == "__main__":
    import pytest
    pytest.main([__file__])
