import sys
import os
import pytest
from datetime import datetime

# Add project root to Python path
project_root = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')
)

sys.path.append(project_root)
from src.models import Transaction


@pytest.fixture
def initialize_transaction():
    txn = Transaction(50.0, "Alice", "Bob", datetime(2026, 4, 19, 10, 0))
    return txn



# Test for transaction object created
def test_transaction_creation(initialize_transaction):
    txn = initialize_transaction
    assert txn.amount == 50.0
    assert txn.sender == "Alice"


# Parameterized test for transaction object created
@pytest.mark.parametrize("amount, sender, receiver", [
    (50.0, "Alice", "Bob"),
    (100.0, "Bob", "Charlie"),
    (-25.0, "Charlie", "ATM")
])
def test_transaction_creation_parameterized(amount, sender, receiver):
    txn = Transaction(amount=amount, sender=sender, receiver=receiver)
    assert txn.amount == amount
    assert txn.sender == sender



if __name__ == "__main__":
    import pytest
    pytest.main([__file__])
