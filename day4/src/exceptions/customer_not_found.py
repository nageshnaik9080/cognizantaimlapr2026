#create CustomerNotFound exception class
class CustomerNotFound(Exception):
    def __init__(self, customer_id):
        self.customer_id = customer_id
        self.message = f"Customer with id {customer_id} not found"
        super().__init__(self.message)