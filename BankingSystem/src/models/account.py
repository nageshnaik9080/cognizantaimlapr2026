"""Account model for BankingSystem."""

from datetime import date
from typing import List

from .transaction import Transaction


class Account:
    """A bank account with running totals and transaction history."""

    def __init__(self, account_number: str, open_date: date, initial_balance: float = 0.0):
        """Create a new account."""
        self._account_number = account_number
        self._open_date = open_date
        self._running_totals = initial_balance
        self._transactions: List[Transaction] = []

    @property
    def account_number(self) -> str:
        """The unique account identifier."""
        return self._account_number

    @property
    def open_date(self) -> date:
        """The date the account was opened."""
        return self._open_date

    @property
    def running_totals(self) -> float:
        """The current balance of the account."""
        return self._running_totals

    def show_customer_transactions(self) -> List[Transaction]:
        """Return the list of transactions for this account."""
        return list(self._transactions)

    def add_transaction(self, transaction: Transaction) -> None:
        """Add a transaction and update the account balance."""
        self._transactions.append(transaction)
        self._running_totals += transaction.amount

    def __repr__(self) -> str:
        return (
            f"Account(account_number={self.account_number!r}, open_date={self.open_date!r}, "
            f"running_totals={self.running_totals!r})"
        )
