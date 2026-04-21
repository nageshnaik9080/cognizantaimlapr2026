"""Customer model for BankingSystem."""

from typing import ClassVar, List


class Customer:
    """A customer with accounts and contact information."""

    _customer_counter: ClassVar[int] = 0

    def __init__(self, account_number: str, name: str, address: str, contact_number: str, email: str, password: str):
        """Create a new customer record."""
        self._account_number = account_number
        self._name = name
        self._address = address
        self._contact_number = contact_number
        self._email = email
        self._password = password
        self._accounts: List[str] = []
        Customer._customer_counter += 1

    @property
    def account_number(self) -> str:
        """The customer account identifier."""
        return self._account_number

    @property
    def name(self) -> str:
        """The customer full name."""
        return self._name

    @property
    def address(self) -> str:
        """The customer address."""
        return self._address

    @property
    def contact_number(self) -> str:
        """The customer's contact phone number."""
        return self._contact_number

    @property
    def email(self) -> str:
        """The customer's email address."""
        return self._email

    def add_account(self, account_number: str) -> None:
        """Link an account to this customer."""
        self._accounts.append(account_number)

    def remove_account(self, account_number: str) -> None:
        """Unlink an account from this customer."""
        self._accounts = [value for value in self._accounts if value != account_number]

    @classmethod
    def total_number_of_customers(cls) -> int:
        """Return the total number of created customers."""
        return cls._customer_counter

    def __repr__(self) -> str:
        return (
            f"Customer(account_number={self.account_number!r}, name={self.name!r}, "
            f"address={self.address!r}, contact_number={self.contact_number!r}, email={self.email!r})"
        )
