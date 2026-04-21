"""Direct debit transaction model for BankingSystem."""

from datetime import date, datetime
from typing import Optional

from .transaction import Transaction


class DirectDebit(Transaction):
    """A transaction scheduled for direct debit on a payment date."""

    def __init__(self, amount: float, sender: str, receiver: str, payment_date: date, timestamp: Optional[datetime] = None):
        """Create a direct debit transaction."""
        super().__init__(amount, sender, receiver, timestamp)
        self._payment_date = payment_date

    @property
    def payment_date(self) -> date:
        """The date the direct debit will be processed."""
        return self._payment_date

    def __repr__(self) -> str:
        return (
            f"DirectDebit(amount={self.amount!r}, sender={self.sender!r}, receiver={self.receiver!r}, "
            f"payment_date={self.payment_date!r}, timestamp={self.timestamp!r})"
        )
