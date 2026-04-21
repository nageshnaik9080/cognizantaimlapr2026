"""Transaction model for BankingSystem."""

from datetime import datetime
from typing import Optional


class Transaction:
    """A financial transaction between sender and receiver."""

    def __init__(self, amount: float, sender: str, receiver: str, timestamp: Optional[datetime] = None):
        """Create a transaction record."""
        self.amount = amount
        self.sender = sender
        self.receiver = receiver
        self.timestamp = timestamp or datetime.now()

    @classmethod
    def deposit_money(cls, amount: float, sender: str, receiver: str) -> "Transaction":
        """Create a deposit transaction."""
        return cls(abs(amount), sender, receiver)

    @classmethod
    def withdraw_money(cls, amount: float, sender: str, receiver: str) -> "Transaction":
        """Create a withdrawal transaction."""
        return cls(-abs(amount), sender, receiver)

    def __repr__(self) -> str:
        return (
            f"Transaction(amount={self.amount!r}, sender={self.sender!r}, receiver={self.receiver!r}, "
            f"timestamp={self.timestamp!r})"
        )
