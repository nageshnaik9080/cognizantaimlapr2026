"""

call the customer view and customer store to generate and display customer details.
"""
import faker 
from store.customerstore import CustomerStore
from view.customerview import CustomerView


def check():
    """
    this function to display the customer details invoke the customer view and customer store to generate and display customer details.
    """
    customer_store = CustomerStore(num_customers=100)
    customer_view = CustomerView(customer_store)
    customer_view.display_customers()
if __name__ == "__main__":
    check()


