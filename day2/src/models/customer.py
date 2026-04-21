#define customer model
import typing
import datetime
class Customer:
    def __init__(self, name: str, email: str, date_of_birth: datetime.date):
        self.name = name
        self.email = email
        self.date_of_birth = date_of_birth

    def __str__(self):
        return f"Customer(name={self.name}, email={self.email}, date_of_birth={self.date_of_birth})"