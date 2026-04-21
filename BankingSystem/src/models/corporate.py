"""Corporate customer model for BankingSystem."""

from .customer import Customer


class Corporate(Customer):
    """A corporate customer with a company type."""

    def __init__(self, account_number: str, name: str, address: str, contact_number: str, email: str, password: str, company_type: str):
        """Create a corporate customer."""
        super().__init__(account_number, name, address, contact_number, email, password)
        self._company_type = company_type

    @property
    def company_type(self) -> str:
        """The legal company type for the corporate customer."""
        return self._company_type

    def __repr__(self) -> str:
        return (
            f"Corporate(account_number={self.account_number!r}, name={self.name!r}, "
            f"company_type={self.company_type!r})"
        )
