#generate 100 customer
import faker
import typing
from models.customer import Customer
class CustomerStore:
    def __init__(self, num_customers: int):
        self.customers = []
        self.generate_customers(num_customers)

    def generate_customers(self, num_customers: int):
        fake = faker.Faker()
        for _ in range(num_customers):
            name = fake.name()
            email = fake.email()
            date_of_birth = fake.date_of_birth()
            customer = Customer(name, email, date_of_birth)
            self.customers.append(customer)

    def get_customers(self) -> typing.List[Customer]:
        return self.customers


