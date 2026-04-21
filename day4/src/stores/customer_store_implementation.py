#create customer store implementation from customer store abstract class
 
from .customer_store import CustomerStore
from ..exceptions.customer_not_found import CustomerNotFound
class CustomerStoreImp(CustomerStore):
   
    def __init__(self):
        self.customers = []
 
    def add_customer(self, customer):
        self.customers.append(customer)
    def get_all_customers(self):
        return self.customers

    def get_customer(self, customer_id):
        for customer in self.customers:
            if customer.customer_id == customer_id:
                return customer 
        raise CustomerNotFound(customer_id)
 
 
    def update_customer(self, customer_id, customer):
        for i in range(len(self.customers)):
            if self.customers[i].customer_id == customer_id:
                self.customers[i] = customer
                return
        raise CustomerNotFound(customer_id)
 
    def delete_customer(self, customer_id):
        for i in range(len(self.customers)):
            if self.customers[i].customer_id == customer_id:
                del self.customers[i]
                return True
        raise CustomerNotFound(customer_id)
 