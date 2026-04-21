import sys
import os

# Add project root to Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(project_root)

from faker import Faker
from src.configurations.conf import Config
from src.dataloaders.customer_csv_data_loader import CustomerCSVDataLoader
from src.dataloaders.customer_txt_data_loader import CustomerTXTDataLoader
from src.dataloaders.customer_json_data_loader import CustomerJSONDataLoader
from src.stores.customer_store_implementation import CustomerStoreImp
from src.utils.pipilineRunner import pipelineRunner

def load_customers(customer_store):
    config = Config()
    env = config.app_env

    if env == "Production":
        data_loader = CustomerJSONDataLoader()
    elif env == "Development":
        data_loader = CustomerCSVDataLoader()
    elif env == "Testing":
        data_loader = CustomerTXTDataLoader()
    else:
        raise ValueError(f"Unknown environment: {env}")

    data_loader.load_data(config.resource_path, customer_store)
    return customer_store

def display_customers(customer_store):
    for customer in customer_store.get_all_customers():
        print(f"customer_id: {customer.customer_id}")
        print(f"name: {customer.name.first_name} {customer.name.last_name}")
        print(f"email: {customer.email}")
        print(f"phone_number: {customer.phone_no}")
        print("-------------")
def update_customer(customer_store, customer_id):
   customer=customer_store.get_customer(customer_id)
   fake=Faker()
   customer.name.first_name=fake.first_name()
   customer.name.last_name=fake.last_name()
   customer.email=fake.email()
   customer.phone_no=fake.random_int(min=1000000000, max=9999999999)
   customer_store.update_customer(customer_id, customer)
   return customer_store
def get_customer_by_id(customer_store, customer_id):
    customer = customer_store.get_customer(customer_id)
    print(f"customer_id: {customer.customer_id}")
    print(f"name: {customer.name.first_name} {customer.name.last_name}")
    print(f"email: {customer.email}")
    print(f"phone_number: {customer.phone_no}")
    print("-------------")

if __name__ == "__main__":
    customer_store = CustomerStoreImp()
    pipeline_runner = pipelineRunner()
    pipeline_runner.add_stage(load_customers(customer_store))
    pipeline_runner.add_stage(display_customers(customer_store))
    pipeline_runner.add_stage(update_customer(customer_store, 2001))
    pipeline_runner.add_stage(get_customer_by_id(customer_store, 2001))
    pipeline_runner.run()
