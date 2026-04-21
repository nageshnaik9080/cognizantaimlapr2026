"""Menu service model for BankingSystem."""

from typing import List, Optional

from .account import Account
from .customer import Customer
from .transaction import Transaction


class Menu:
    """A service layer for managing customers, accounts, and transactions."""

    def __init__(self):
        """Create a new menu service instance."""
        self._transaction_list: List[Transaction] = []
        self._customer_account_list: List[Account] = []
        self._customer_list: List[Customer] = []

    @property
    def transaction_list(self) -> List[Transaction]:
        """All recorded transactions."""
        return list(self._transaction_list)

    @property
    def customer_account_list(self) -> List[Account]:
        """Open customer accounts."""
        return list(self._customer_account_list)

    @property
    def customer_list(self) -> List[Customer]:
        """Registered customers."""
        return list(self._customer_list)

    def initiate_transaction(self, transaction: Transaction) -> None:
        """Record a transaction in the system."""
        self._transaction_list.append(transaction)

    def add_customer(self, customer: Customer) -> None:
        """Add a new customer to the system."""
        self._customer_list.append(customer)

    def delete_customer(self, account_number: str) -> None:
        """Remove a customer by account number."""
        self._customer_list = [customer for customer in self._customer_list if customer.account_number != account_number]

    def open_account(self, account: Account) -> None:
        """Open a customer account."""
        self._customer_account_list.append(account)

    def close_account(self, account_number: str) -> None:
        """Close an account by account number."""
        self._customer_account_list = [account for account in self._customer_account_list if account.account_number != account_number]

    def edit_customer_details(self, account_number: str, *, name: Optional[str] = None, address: Optional[str] = None, contact_number: Optional[str] = None, email: Optional[str] = None) -> None:
        """Update customer contact information."""
        for customer in self._customer_list:
            if customer.account_number == account_number:
                if name is not None:
                    customer._name = name
                if address is not None:
                    customer._address = address
                if contact_number is not None:
                    customer._contact_number = contact_number
                if email is not None:
                    customer._email = email
                break

    def login(self, account_number: str, password: str) -> bool:
        """Check whether customer credentials are valid."""
        for customer in self._customer_list:
            if customer.account_number == account_number and getattr(customer, '_password', None) == password:
                return True
        return False

    def logout(self) -> None:
        """Placeholder for logout behavior."""
        pass

    def __repr__(self) -> str:
        return (
            f"Menu(customers={len(self._customer_list)}, accounts={len(self._customer_account_list)}, "
            f"transactions={len(self._transaction_list)})"
        )
