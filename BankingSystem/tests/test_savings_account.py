import sys
import os
import pytest
from datetime import date

# Add project root to Python path
project_root = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')
)

sys.path.append(project_root)
from src.models import SavingsAccount, Account


@pytest.fixture
def initialize_savings_account():
    savings = SavingsAccount("S001", date(2026, 4, 19), interest_rate=0.05, initial_balance=200.0)
    return savings



# Test for savings account object created
def test_savings_account_creation(initialize_savings_account):
    savings = initialize_savings_account
    assert isinstance(savings, Account)
    assert savings.account_number == "S001"


# Parameterized test for savings account object created
@pytest.mark.parametrize("account_number, open_date, interest_rate, initial_balance", [
    ("S001", date(2026, 4, 19), 0.05, 200.0),
    ("S002", date(2026, 4, 20), 0.10, 1000.0),
    ("S003", date(2026, 4, 21), 0.02, 500.0)
])
def test_savings_account_creation_parameterized(account_number, open_date, interest_rate, initial_balance):
    savings = SavingsAccount(account_number=account_number, open_date=open_date, interest_rate=interest_rate, initial_balance=initial_balance)
    assert savings.account_number == account_number
    assert savings.interest_rate == interest_rate



if __name__ == "__main__":
    import pytest
    pytest.main([__file__])
