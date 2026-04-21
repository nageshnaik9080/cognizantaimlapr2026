#test for patient

import sys
import os
import pytest
import csv

# Add project root to Python path
project_root = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', '..')
)

sys.path.append(project_root)
from src.models.patient import Patient

#fixture to initialize patient object
@pytest.fixture
def initialize_patient():
    patient = Patient(id=1, name="John Doe", dob="1990-01-01", ailment="Flu")
    return patient

#function to read patient data from csv file and return as list of tuples    
def read_patient_data_from_csv():
    #read patient data from csv file and return as list of tuples
    patient_data = []
    with open('tests/patients.csv', mode='r', newline="", encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            patient_data.append((int(row['id']), row['name'], row['dob'], row['ailment']))
    return patient_data

# Test for patient object created
def test_patient_creation(initialize_patient):
    patient = initialize_patient
    assert patient.id == 1
    assert patient.name == "John Doe"
    assert patient.dob == "1990-01-01"
    assert patient.ailment == "Flu"

#parameterized test for patient object created
@pytest.mark.parametrize("id, name, dob, ailment", [
    (1, "John Doe", "1990-01-01", "Flu"),
    (2, "Jane Smith", "1985-05-15", "Diabetes"),
    (3, "Bob Johnson", "1992-12-10", "Hypertension")
])
def test_patient_creation_parameterized(id, name, dob, ailment):
    patient = Patient(id=id, name=name, dob=dob, ailment=ailment)
    assert patient.id == id
    assert patient.name == name
    assert patient.dob == dob
    assert patient.ailment == ailment

#parameterized test for patient object created using csv file
@pytest.mark.parametrize("id, name, dob, ailment", read_patient_data_from_csv())
def test_patient_creation_csv_parameterized(id, name, dob, ailment):
    patient = Patient(id=id, name=name, dob=dob, ailment=ailment)
    assert patient.id == id
    assert patient.name == name
    assert patient.dob == dob
    assert patient.ailment == ailment