import sys
import os
import pytest
from datetime import date

# Add project root to Python path
project_root = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')
)

sys.path.append(project_root)
from src.models import DirectDebit, Transaction


@pytest.fixture
def initialize_direct_debit():
    direct = DirectDebit(75.0, "Alice", "Bob", payment_date=date(2026, 4, 20))
    return direct



# Test for direct debit object created
def test_direct_debit_creation(initialize_direct_debit):
    direct = initialize_direct_debit
    assert isinstance(direct, Transaction)
    assert direct.amount == 75.0


# Parameterized test for direct debit object created
@pytest.mark.parametrize("amount, sender, receiver, payment_date", [
    (75.0, "Alice", "Bob", date(2026, 4, 20)),
    (100.0, "A", "B", date(2026, 5, 1)),
    (50.0, "X", "Y", date(2026, 4, 25))
])
def test_direct_debit_creation_parameterized(amount, sender, receiver, payment_date):
    direct = DirectDebit(amount=amount, sender=sender, receiver=receiver, payment_date=payment_date)
    assert direct.amount == amount
    assert direct.payment_date == payment_date


if __name__ == "__main__":
    import pytest
    pytest.main([__file__])
