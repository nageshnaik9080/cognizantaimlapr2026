"""Savings account model for BankingSystem."""

from datetime import date

from .account import Account


class SavingsAccount(Account):
    """A savings account with an interest rate."""

    def __init__(self, account_number: str, open_date: date, interest_rate: float = 0.0, initial_balance: float = 0.0):
        """Create a savings account."""
        super().__init__(account_number, open_date, initial_balance)
        self._interest_rate = interest_rate

    @property
    def interest_rate(self) -> float:
        """The interest rate applied to the account balance."""
        return self._interest_rate

    def calculate_interest(self) -> float:
        """Calculate interest based on the current balance."""
        return self.running_totals * self.interest_rate

    def __repr__(self) -> str:
        return (
            f"SavingsAccount(account_number={self.account_number!r}, open_date={self.open_date!r}, "
            f"running_totals={self.running_totals!r}, interest_rate={self.interest_rate!r})"
        )
