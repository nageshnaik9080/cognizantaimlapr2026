#ctreate class staff inherit from person class and add staffid and department as attributes
from typing import TYPE_CHECKING
from src.models.person import Person

if TYPE_CHECKING:
    from src.models.role import Role

class Staff(Person): #inherit from person class
    def __init__(self, aadharno: int, mobileno: int, role: 'Role'):
        super().__init__(aadharno, mobileno)
        self.__role = role #association with role class

    @property
    def role(self) -> 'Role':
        return self.__role

    @role.setter
    def role(self, value : 'Role'):
        self.__role = value