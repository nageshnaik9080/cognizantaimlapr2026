#create crud operations for patient
import sys 
import os

#add project root to python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(project_root)

from conf.logger_conf import setup_logger
from src.models.patient import Patient
from src.exception.patient_not_found_exception import PatientNotFoundException

logger = setup_logger()

class PatientStore:
    def __init__(self):
        self.patients = []

    def add_patient(self, patient):
        logger.info(f"Adding patient: {patient}")
        self.patients.append(patient)

    def get_all_patients(self):
        logger.info("Retrieving all patients")
        return self.patients

    def get_patient_by_id(self, id):
        logger.info(f"Retrieving patient with ID: {id}")
        for patient in self.patients:
            if patient.id == id:
                return patient
        raise PatientNotFoundException(f"Patient with ID {id} not found")
        
    def update_patient(self, id, name=None, age=None):
        logger.info(f"Updating patient with ID: {id}")
        patient = self.get_patient_by_id(id)
        if patient:
            if name:
                patient.name = name
            if age:
                patient.age = age
            return patient
        raise PatientNotFoundException(f"Patient with ID {id} not found")
    def delete_patient(self, id):
        logger.info(f"Deleting patient with ID: {id}")
        patient = self.get_patient_by_id(id)
        if patient:
            self.patients.remove(patient)
            return patient
        raise PatientNotFoundException(f"Patient with ID {id} not found")