
#test for doctor

import sys
import os
import pytest
import csv

# Add project root to Python path
project_root = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', '..')
)

sys.path.append(project_root)
from src.models.doctor import Doctor

@pytest.fixture
def initialize_doctor():
    doctor = Doctor(id=1, name="Dr. Smith", specialization="Cardiology")
    return doctor

def read_doctor_data_from_csv():
    #read doctor data from csv file and return as list of tuples
    doctor_data = []
    with open('tests/doctors.csv', mode='r', newline="", encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            doctor_data.append((int(row['id']), row['name'], row['specialization']))
    return doctor_data


# Test for doctor object created
def test_doctor_creation(initialize_doctor):
    doctor = initialize_doctor
    assert doctor.id == 1
    assert doctor.name == "Dr. Smith"
    assert doctor.specialization == "Cardiology"

  #parameterized test for doctor object created
@pytest.mark.parametrize("id, name, specialization", [
    (1, "Dr. Smith", "Cardiology"),
    (2, "Dr. Johnson", "Neurology"),
    (3, "Dr. Williams", "Pediatrics")
])
def test_doctor_creation_parameterized(id, name, specialization):
    doctor = Doctor(id=id, name=name, specialization=specialization)
    assert doctor.id == id
    assert doctor.name == name
    assert doctor.specialization == specialization

@pytest.mark.parametrize("id, name, specialization", read_doctor_data_from_csv())
def test_doctor_creation_csv_parameterized(id, name, specialization):
    doctor = Doctor(id=id, name=name, specialization=specialization)
    assert doctor.id == id
    assert doctor.name == name
    assert doctor.specialization == specialization    
    