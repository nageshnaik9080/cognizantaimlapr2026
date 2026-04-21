import sys
import os
from faker import Faker

# Add project root to Python path
project_root = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', '..')
)

sys.path.append(project_root)

from conf.logger_conf import setup_logger
from src.models.doctor import Doctor
from src.models.patient import Patient
from src.models.appointment import Appointment
from src.stores.patientstore import PatientStore
from src.stores.doctorstore import DoctorStore
from src.stores.appointmentstore import AppointmentStore
"""
Entry point for the application. This module initializes the application and starts the main process.
"""

logger = setup_logger()
faker=Faker()
doctorstore = DoctorStore()
patientstore = PatientStore()
appointmentstore = AppointmentStore()

doctor_id=0
patient_id=0


def doctor_app():
    """
    create doctor agent and run the main process
    """
    logger.info("app doctor agent is running...")
    doctor = Doctor(id=faker.random_int(), name=faker.name(), specialization=faker.job())
    doctorstore.add_doctor(doctor)
    logger.info(f"Doctor added: {doctorstore.get_doctor_by_id(doctor.id)}")
    global doctor_id
    doctor_id=doctor.id

def patient_app():
    """
    create patient agent and run the main process
    """
    logger.info("app patient agent is running...")
    # Implement patient agent logic here
    patient = Patient(id=faker.random_int(), name=faker.name(), dob=faker.date_of_birth(), ailment=faker.sentence())
    patientstore.add_patient(patient)
    logger.info(f"Patient added: {patientstore.get_patient_by_id(patient.id)}")
    global patient_id
    patient_id=patient.id
def appointment_app():
    """
    create appointment agent and run the main process
    """
    logger.info("app appointment agent is running...")
    # Implement appointment agent logic here
    appointment = Appointment(id=faker.random_int(), date=faker.date(), time=faker.time(), doctor=doctorstore.get_doctor_by_id(doctor_id), patient=patientstore.get_patient_by_id(patient_id))
    appointmentstore.add_appointment(appointment)
    logger.info(f"Appointment added: {appointmentstore.get_appointment_by_id(appointment.id)}") 

""" handle entry point """
if __name__ == "__main__":
    doctor_app()
    patient_app()
    appointment_app()
