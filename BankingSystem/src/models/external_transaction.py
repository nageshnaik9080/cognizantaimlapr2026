"""External transaction model for BankingSystem."""

from .transaction import Transaction


class ExternalTransaction(Transaction):
    """A transaction executed through an external branch."""

    def __init__(self, amount: float, sender: str, receiver: str, branch_name: str, branch_address: str, branch_postcode: str, branch_code: str, timestamp=None):
        """Create an external branch transaction."""
        super().__init__(amount, sender, receiver, timestamp)
        self._branch_name = branch_name
        self._branch_address = branch_address
        self._branch_postcode = branch_postcode
        self._branch_code = branch_code

    @property
    def branch_name(self) -> str:
        """The name of the external branch."""
        return self._branch_name

    @property
    def branch_address(self) -> str:
        """The address of the external branch."""
        return self._branch_address

    @property
    def branch_postcode(self) -> str:
        """The postcode of the external branch."""
        return self._branch_postcode

    @property
    def branch_code(self) -> str:
        """The branch code for the external transaction."""
        return self._branch_code

    def __repr__(self) -> str:
        return (
            f"ExternalTransaction(amount={self.amount!r}, sender={self.sender!r}, receiver={self.receiver!r}, "
            f"branch_name={self.branch_name!r}, branch_address={self.branch_address!r}, "
            f"branch_postcode={self.branch_postcode!r}, branch_code={self.branch_code!r}, "
            f"timestamp={self.timestamp!r})"
        )
