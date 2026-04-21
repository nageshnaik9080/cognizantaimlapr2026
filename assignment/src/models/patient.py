from faker import Faker
import random
from typing import List

fake = Faker()

class Patient:
    DISEASES: List[str] = [
        "Heart Attack",
        "Diabetes",
        "Fever",
        "Skin Allergy",
        "Cancer"  # No doctor mapping
    ]

    def __init__(self, name: str, disease: str) -> None:
        self.name: str = name
        self.disease: str = disease

    @staticmethod
    def generate_fake_patient() -> "Patient":
        name: str = fake.name()
        disease: str = random.choice(Patient.DISEASES)
        return Patient(name, disease)

    @staticmethod
    def generate_fake_patients(n: int = 10) -> List["Patient"]:
        return [Patient.generate_fake_patient() for _ in range(n)]