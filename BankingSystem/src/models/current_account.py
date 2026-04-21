"""Current account model for BankingSystem."""

from datetime import date

from .account import Account


class CurrentAccount(Account):
    """A current account that supports overdraft."""

    def __init__(self, account_number: str, open_date: date, overdraft_limit: float = 0.0, initial_balance: float = 0.0):
        """Create a current account."""
        super().__init__(account_number, open_date, initial_balance)
        self._overdraft_limit = overdraft_limit

    @property
    def overdraft_limit(self) -> float:
        """The allowed overdraft limit for the account."""
        return self._overdraft_limit

    def can_withdraw(self, amount: float) -> bool:
        """Return whether the requested withdrawal is allowed."""
        return self.running_totals + self.overdraft_limit >= amount

    def __repr__(self) -> str:
        return (
            f"CurrentAccount(account_number={self.account_number!r}, open_date={self.open_date!r}, "
            f"running_totals={self.running_totals!r}, overdraft_limit={self.overdraft_limit!r})"
        )
