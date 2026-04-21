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

from src.models import Menu, Account, Customer, Transaction

@pytest.fixture
def initialize_menu():
    menu = Menu()
    return menu

# Test for menu object created
def test_menu_creation(initialize_menu):
    menu = initialize_menu
    assert len(menu.transaction_list) == 0
    assert len(menu.customer_list) == 0

# Parameterized test for menu object created
@pytest.mark.parametrize("customer_count, account_count", [
    (0, 0),
    (1, 1),
    (2, 3)
])
def test_menu_creation_parameterized(customer_count, account_count):
    menu = Menu()
    for i in range(customer_count):
        customer = Customer(f"CU{i+1:03d}", f"Customer{i+1}", "Address", "555-0000", "test@example.com", "pass")
        menu.add_customer(customer)
    for i in range(account_count):
        account = Account(f"A{i+1:03d}", date(2026, 4, 19))
        menu.open_account(account)
    assert len(menu.customer_list) == customer_count
    assert len(menu.customer_account_list) == account_count



def test_menu_creation():
    menu = Menu()
    assert len(menu.transaction_list) == 0
    assert len(menu.customer_account_list) == 0
    assert len(menu.customer_list) == 0


def test_menu_add_customer():
    menu = Menu()
    customer = Customer("CU001", "Alice", "123 St", "555-1234", "alice@example.com", "pass")
    menu.add_customer(customer)
    assert len(menu.customer_list) == 1


def test_menu_delete_customer():
    menu = Menu()
    customer = Customer("CU002", "Bob", "456 St", "555-5678", "bob@example.com", "pass")
    menu.add_customer(customer)
    menu.delete_customer("CU002")
    assert len(menu.customer_list) == 0


def test_menu_open_close_account():
    menu = Menu()
    account = Account("A001", date(2026, 4, 19), initial_balance=100.0)
    menu.open_account(account)
    assert len(menu.customer_account_list) == 1
    menu.close_account("A001")
    assert len(menu.customer_account_list) == 0


def test_menu_edit_customer():
    menu = Menu()
    customer = Customer("CU003", "Charlie", "789 St", "555-9012", "charlie@example.com", "pass")
    menu.add_customer(customer)
    menu.edit_customer_details("CU003", name="Charles", email="charles@example.com")
    updated = menu.customer_list[0]
    assert updated.name == "Charles"
    assert updated.email == "charles@example.com"


def test_menu_initiate_transaction():
    menu = Menu()
    txn = Transaction(50.0, "A", "B")
    menu.initiate_transaction(txn)
    assert len(menu.transaction_list) == 1


def test_menu_login():
    menu = Menu()
    customer = Customer("CU004", "Diana", "321 St", "555-1111", "diana@example.com", "secret")
    menu.add_customer(customer)
    assert menu.login("CU004", "secret") is True
    assert menu.login("CU004", "wrong") is False


def test_menu_repr():
    menu = Menu()
    repr_str = repr(menu)
    assert "customers=0" in repr_str
    assert "accounts=0" in repr_str
    assert "transactions=0" in repr_str

if __name__ == "__main__":
    import pytest
    pytest.main([__file__])
