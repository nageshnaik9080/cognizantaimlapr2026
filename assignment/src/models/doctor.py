from faker import Faker
import random
from typing import List

fake = Faker()

class Doctor:
    SPECIALIZATIONS: List[str] = [
        "Cardiologist",
        "Endocrinologist",
        "General Physician",
        "Dermatologist"
    ]

    def __init__(self, name: str, specialty: str) -> None:
        self.name: str = name
        self.specialty: str = specialty

    @staticmethod
    def generate_fake_doctor() -> "Doctor":
        name: str = fake.name()
        specialty: str = random.choice(Doctor.SPECIALIZATIONS)
        return Doctor(name, specialty)

    @staticmethod
    def generate_fake_doctors(n: int = 5) -> List["Doctor"]:
        doctors: List[Doctor] = []

        # Ensure one doctor per specialization
        for spec in Doctor.SPECIALIZATIONS:
            doctors.append(Doctor(fake.name(), spec))

        # Add remaining randomly
        if n > len(doctors):
            for _ in range(n - len(doctors)):
                doctors.append(Doctor.generate_fake_doctor())

        return doctors[:n]