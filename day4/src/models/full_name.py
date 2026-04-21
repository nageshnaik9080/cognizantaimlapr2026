#design data validation for full name
from pydantic import BaseModel, validator, Field

class FullName(BaseModel):
    first_name: str = Field(..., pattern=r"^[a-zA-Z]+$", description="First name of the person")
    last_name: str = Field(..., pattern=r"^[a-zA-Z]+$", description="Last name of the person")
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def __repr__(self):
        return f"{self.first_name} {self.last_name}"