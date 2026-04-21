import sys
import os
import pytest
from datetime import date

# Add project root to Python path
project_root = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')
)

sys.path.append(project_root)
from src.models import CurrentAccount, Account


@pytest.fixture
def initialize_current_account():
    current = CurrentAccount("C001", date(2026, 4, 19), overdraft_limit=50.0, initial_balance=10.0)
    return current



# Test for current account object created
def test_current_account_creation(initialize_current_account):
    current = initialize_current_account
    assert isinstance(current, Account)
    assert current.account_number == "C001"


# Parameterized test for current account object created
@pytest.mark.parametrize("account_number, open_date, overdraft_limit, initial_balance", [
    ("C001", date(2026, 4, 19), 50.0, 10.0),
    ("C002", date(2026, 4, 20), 100.0, 20.0),
    ("C003", date(2026, 4, 21), 25.0, 5.0)
])
def test_current_account_creation_parameterized(account_number, open_date, overdraft_limit, initial_balance):
    current = CurrentAccount(account_number=account_number, open_date=open_date, overdraft_limit=overdraft_limit, initial_balance=initial_balance)
    assert current.account_number == account_number
    assert current.overdraft_limit == overdraft_limit


if __name__ == "__main__":
    import pytest
    pytest.main([__file__])
