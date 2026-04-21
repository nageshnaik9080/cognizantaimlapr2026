"""
person model definition
"""
 
import re
 
 
class Person:
    def __init__(self, aadharno: int, mobileno: int):
        self.__aadharno = aadharno
        self.__mobileno = mobileno
   
 
    #getters for aadharno and mobileno
    def get_aadharno(self):
        return self.__aadharno
 
    def get_mobileno(self):
        return self.__mobileno
 
    #create setter for mobile number
    def set_mobileno(self, mobileno):
        self.__mobileno = mobileno
 
 
    def mobileno(self,value):
        if not re.match(r'^\d{10}$', str(value)):
            raise ValueError("Invalid mobile number. It should be a 10-digit number starting with 6, 7, 8, or 9.")
 
 