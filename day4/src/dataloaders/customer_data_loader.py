#create customer data loader abstract class
from abc import ABC, abstractmethod
from src.stores.customer_store_implementation import CustomerStoreImp
class CustomerDataLoader(ABC):
    @abstractmethod
    def load_data(self, file_path, customer_store: CustomerStoreImp):
        pass