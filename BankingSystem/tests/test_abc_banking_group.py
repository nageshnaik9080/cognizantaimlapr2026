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

from src.models import ABCBankingGroup, Account

@pytest.fixture
def initialize_abc_banking_group():
    group = ABCBankingGroup()
    return group

# Test for abc_banking_group object created
def test_abc_banking_group_creation(initialize_abc_banking_group):
    group = initialize_abc_banking_group
    assert len(group.accounts) == 0

# Parameterized test for abc_banking_group object created
@pytest.mark.parametrize("account_count", [0, 1, 3])
def test_abc_banking_group_creation_parameterized(account_count):
    group = ABCBankingGroup()
    for i in range(account_count):
        account = Account(f"A{i+1:03d}", date(2026, 4, 19))
        group.add_account(account)
    assert len(group.accounts) == account_count



def test_banking_group_creation():
    group = ABCBankingGroup()
    assert len(group.accounts) == 0


def test_banking_group_add_account():
    group = ABCBankingGroup()
    account = Account("A001", date(2026, 4, 19), initial_balance=100.0)
    group.add_account(account)
    assert len(group.accounts) == 1
    assert group.find_account("A001") is not None


def test_banking_group_remove_account():
    group = ABCBankingGroup()
    account = Account("A002", date(2026, 4, 19))
    group.add_account(account)
    group.remove_account("A002")
    assert group.find_account("A002") is None


def test_banking_group_find_account():
    group = ABCBankingGroup()
    account1 = Account("A003", date(2026, 4, 19))
    account2 = Account("A004", date(2026, 4, 19))
    group.add_account(account1)
    group.add_account(account2)
    assert group.find_account("A003") == account1
    assert group.find_account("A999") is None


def test_banking_group_repr():
    group = ABCBankingGroup()
    account = Account("A005", date(2026, 4, 19))
    group.add_account(account)
    repr_str = repr(group)
    assert "accounts=1" in repr_str

if __name__ == "__main__":
    import pytest
    pytest.main([__file__])
