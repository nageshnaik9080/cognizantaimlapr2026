import sys
import os
import pytest
from datetime import date

# Add project root to Python path
project_root = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')
)

sys.path.append(project_root)
from src.models import Account, Transaction


@pytest.fixture
def initialize_account():
    account = Account("A001", date(2026, 4, 19), initial_balance=100.0)
    return account



# Test for account object created
def test_account_creation(initialize_account):
    account = initialize_account
    assert account.account_number == "A001"
    assert account.running_totals == 100.0


# Parameterized test for account object created
@pytest.mark.parametrize("account_number, open_date, initial_balance", [
    ("A001", date(2026, 4, 19), 100.0),
    ("A002", date(2026, 4, 20), 200.0),
    ("A003", date(2026, 4, 21), 0.0)
])
def test_account_creation_parameterized(account_number, open_date, initial_balance):
    account = Account(account_number=account_number, open_date=open_date, initial_balance=initial_balance)
    assert account.account_number == account_number
    assert account.running_totals == initial_balance



if __name__ == "__main__":
    import pytest
    pytest.main([__file__])
