#creat doctor crud operations
import sys 
import os

#add project root to python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(project_root)

from conf.logger_conf import setup_logger
from src.models.doctor import Doctor
from src.exception.doctor_not_found_exception import DoctorNotFoundException

logger = setup_logger()

class DoctorStore:
    def __init__(self):
        
        self.doctors = []

    def add_doctor(self, doctor : Doctor):
        logger.info(f"Adding doctor: {doctor}")
        self.doctors.append(doctor)

    def get_all_doctors(self):
        logger.info("Retrieving all doctors")
        return self.doctors      

    def get_doctor_by_id(self, id : int):
        logger.info(f"Retrieving doctor with ID: {id}")
        for doctor in self.doctors:
            if doctor.id == id:
                return doctor
        raise DoctorNotFoundException(f"Doctor with ID {id} not found")
        
    def update_doctor(self, id : int, name : str = None, specialization : str = None):
        logger.info(f"Updating doctor with ID: {id}")
        doctor = self.get_doctor_by_id(id)
        if doctor:
            if name:
                doctor.name = name
            if specialization:
                doctor.specialization = specialization
            return doctor
        raise DoctorNotFoundException(f"Doctor with ID {id} not found")
    def delete_doctor(self, id : int):
        logger.info(f"Deleting doctor with ID: {id}")
        doctor = self.get_doctor_by_id(id)
        if doctor:
            self.doctors.remove(doctor)
            return doctor
        raise DoctorNotFoundException(f"Doctor with ID {id} not found")    
      