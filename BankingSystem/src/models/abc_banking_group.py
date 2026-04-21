"""ABCBankingGroup model for BankingSystem."""

from typing import List, Optional

from .account import Account


class ABCBankingGroup:
    """A banking group that manages multiple accounts."""

    def __init__(self):
        """Create a new banking group."""
        self._accounts: List[Account] = []

    @property
    def accounts(self) -> List[Account]:
        """Return a copy of the managed accounts."""
        return list(self._accounts)

    def add_account(self, account: Account) -> None:
        """Add an account to the banking group."""
        self._accounts.append(account)

    def remove_account(self, account_number: str) -> None:
        """Remove an account by its number."""
        self._accounts = [account for account in self._accounts if account.account_number != account_number]

    def find_account(self, account_number: str) -> Optional[Account]:
        """Find an account by number."""
        for account in self._accounts:
            if account.account_number == account_number:
                return account
        return None

    def __repr__(self) -> str:
        return f"ABCBankingGroup(accounts={len(self._accounts)})"
