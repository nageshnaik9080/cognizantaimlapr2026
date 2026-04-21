from typing import List, Tuple, Optional
from models.patient import Patient
from models.doctor import Doctor

def display_mappings(
    mappings: List[Tuple[Patient, Optional[Doctor]]]
) -> None:
    print("\n~~~~ Patient → Doctor Mapping ~~~~\n")

    for patient, doctor in mappings:
        if doctor:
            print(f"{patient.name} ({patient.disease}) → {doctor.name} [{doctor.specialty}]")
        else:
            print(f"{patient.name} ({patient.disease}) →  No Doctor Available")