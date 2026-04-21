import sys
import os
import pytest
from datetime import date

# Add project root to Python path
project_root = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')
)

sys.path.append(project_root)
from src.models import ExternalTransaction, Transaction

@pytest.fixture
def initialize_external_transaction():
    external = ExternalTransaction(
        150.0,
        "Alice",
        "Bank XYZ",
        branch_name="Branch A",
        branch_address="1 Bank Plaza",
        branch_postcode="12345",
        branch_code="B001",
    )
    return external

# Test for external_transaction object created
def test_external_transaction_creation(initialize_external_transaction):
    external = initialize_external_transaction
    assert isinstance(external, Transaction)
    assert external.branch_code == "B001"

# Parameterized test for external_transaction object created
@pytest.mark.parametrize("amount, branch_name, branch_code", [
    (150.0, "Branch A", "B001"),
    (200.0, "Branch B", "B002"),
    (75.0, "Branch C", "B003")
])
def test_external_transaction_creation_parameterized(amount, branch_name, branch_code):
    external = ExternalTransaction(
        amount, "A", "B", branch_name, "Address", "12345", branch_code
    )
    assert external.amount == amount
    assert external.branch_name == branch_name
    assert external.branch_code == branch_code



def test_external_transaction_creation():
    external = ExternalTransaction(
        150.0,
        "Alice",
        "Bank XYZ",
        branch_name="Branch A",
        branch_address="1 Bank Plaza",
        branch_postcode="12345",
        branch_code="B001",
    )
    assert isinstance(external, Transaction)
    assert external.amount == 150.0
    assert external.branch_name == "Branch A"
    assert external.branch_code == "B001"


def test_external_transaction_properties():
    external = ExternalTransaction(
        200.0, "A", "B",
        "Branch B", "2 Plaza St", "67890", "B002"
    )
    assert external.branch_address == "2 Plaza St"
    assert external.branch_postcode == "67890"


def test_external_transaction_repr():
    external = ExternalTransaction(
        75.0, "X", "Y",
        "Branch C", "3 St", "11111", "B003"
    )
    repr_str = repr(external)
    assert "Branch C" in repr_str
    assert "B003" in repr_str

if __name__ == "__main__":
    import pytest
    pytest.main([__file__])
