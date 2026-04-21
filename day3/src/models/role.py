#role model definition
class Role:
    def __init__(self, name: str, description: str = None, permissions: list = None):
        self.__name = name
        self.__description = description
        self.__permissions = permissions if permissions else []

    #getter for role
    @property
    def name(self):
        return self.__name

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description):
        self.__description = description

    @property
    def permissions(self):
        return self.__permissions

    @permissions.setter
    def permissions(self, permissions):
        self.__permissions = permissions            

    