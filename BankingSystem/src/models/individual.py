"""Individual customer model for BankingSystem."""

from datetime import date

from .customer import Customer


class Individual(Customer):
    """A customer who is an individual person."""

    def __init__(self, account_number: str, name: str, address: str, contact_number: str, email: str, password: str, surname: str, gender: str, date_of_birth: date):
        """Create an individual customer."""
        super().__init__(account_number, name, address, contact_number, email, password)
        self._surname = surname
        self._gender = gender
        self._date_of_birth = date_of_birth

    @property
    def surname(self) -> str:
        """The customer's surname."""
        return self._surname

    @property
    def gender(self) -> str:
        """The customer's gender."""
        return self._gender

    @property
    def date_of_birth(self) -> date:
        """The customer's date of birth."""
        return self._date_of_birth

    def work_out_age(self) -> int:
        """Calculate the customer's age from date of birth."""
        today = date.today()
        years = today.year - self.date_of_birth.year
        if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            years -= 1
        return years

    def __repr__(self) -> str:
        return (
            f"Individual(account_number={self.account_number!r}, name={self.name!r}, surname={self.surname!r}, "
            f"gender={self.gender!r}, date_of_birth={self.date_of_birth!r})"
        )
