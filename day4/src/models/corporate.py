#create cororate class inheritr from customer class using pydantic
from pydantic import BaseModel, Field
from models.customer import Customer
from models.company_type import CompanyType
class Corporate(Customer):
    company_type: CompanyType
    registration_number: str = Field(..., description="Registration number of the company")