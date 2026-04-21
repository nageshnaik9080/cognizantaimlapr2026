from typing import List, Tuple, Optional, Dict
from models.doctor import Doctor
from models.patient import Patient

class HealthcareStore:

    def __init__(self) -> None:
        self.doctors: List[Doctor] = []
        self.patients: List[Patient] = []

        self.disease_map: Dict[str, str] = {
            "Heart Attack": "Cardiologist",
            "Diabetes": "Endocrinologist",
            "Fever": "General Physician",
            "Skin Allergy": "Dermatologist"
        }

    def add_doctor(self, doctor: Doctor) -> None:
        self.doctors.append(doctor)

    def add_patient(self, patient: Patient) -> None:
        self.patients.append(patient)

    def assign_doctor(self, patient: Patient) -> Optional[Doctor]:
        required_specialization = self.disease_map.get(patient.disease)

        for doc in self.doctors:
            if doc.specialty == required_specialization:
                return doc

        return None

    def get_all_mappings(self) -> List[Tuple[Patient, Optional[Doctor]]]:
        return [
            (patient, self.assign_doctor(patient))
            for patient in self.patients
        ]