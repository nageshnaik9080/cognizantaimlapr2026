from src.dataloaders.customer_data_loader import CustomerDataLoader
from src.stores.customer_store_implementation import CustomerStoreImp
from src.models.customer import Customer
from src.models.full_name import FullName


class CustomerTXTDataLoader(CustomerDataLoader):

    def load_data(self, file_path, customer_store: CustomerStoreImp):
        with open(file_path, 'r') as f:
            content = f.read()

        # Split records by blank lines
        records = content.strip().split("\n\n")

        for record in records:
            lines = record.strip().split("\n")
            data = {}
            for line in lines:
                key, value = line.split(":", 1)
                data[key.strip()] = value.strip()

            customer_id = int(data['customer_id'])
            first_name = data['first_name']
            last_name = data['last_name']
            email = data['email']
            phone_no = data['phone_no']

            full_name = FullName(first_name=first_name, last_name=last_name)
            customer = Customer(
                customer_id=customer_id,
                name=full_name,
                email=email,
                phone_no=phone_no
            )
            customer_store.add_customer(customer)
