#create appointment
from datetime import datetime
from .doctor import Doctor
from .patient import Patient

class Appointment:
    def __init__(self, id : int, date, time, doctor : Doctor, patient : Patient):
        self.id = id
        self.date = date
        self.time = time
        self.doctor = doctor
        self.patient = patient
        

    def __str__(self):
        return f"Appointment(id={self.id}, doctor={self.doctor}, patient={self.patient}, date={self.date}, time={self.time})"