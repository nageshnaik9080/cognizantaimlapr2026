# 🏥 Healthcare Management System - Day 3

A comprehensive Healthcare Management Application demonstrating Object-Oriented Programming (OOP) principles, MVC pattern, CRUD operations, exception handling, and logging.

## 📋 Table of Contents

- [Project Overview](#project-overview)
- [Architecture](#architecture)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Data Models](#data-models)
- [Data Storage Layer](#data-storage-layer)
- [Exception Handling](#exception-handling)
- [Logging System](#logging-system)
- [Example Execution](#example-execution)
- [Key Design Patterns](#key-design-patterns)
- [Features](#features)
- [Extending the Project](#extending-the-project)

## 🎯 Project Overview

This Healthcare Management System demonstrates professional software development practices including:

- ✅ **Object-Oriented Design** - Classes, encapsulation, inheritance
- ✅ **MVC Architecture** - Models, Stores (Controllers), Logging (Views)
- ✅ **CRUD Operations** - Complete data manipulation
- ✅ **Exception Handling** - Custom exceptions for error management
- ✅ **Logging System** - Comprehensive activity tracking
- ✅ **Data Generation** - Realistic test data using Faker
- ✅ **Type Hints** - Professional Python code standards

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    app.py (Main Entry Point)                 │
└─────────────────────────────────────────────────────────────┘
                              │
        ┌─────────────────────┼─────────────────────┐
        │                     │                     │
        ▼                     ▼                     ▼
   ┌─────────────┐      ┌──────────────┐      ┌────────────────┐
   │ doctor_app()│      │ patient_app()│      │appointment_app()│
   └─────────────┘      └──────────────┘      └────────────────┘
        │                     │                     │
        ▼                     ▼                     ▼
   ┌─────────────────┐  ┌──────────────────┐  ┌─────────────────────┐
   │ DoctorStore     │  │ PatientStore     │  │ AppointmentStore    │
   │ .add_doctor()   │  │ .add_patient()   │  │ .add_appointment()  │
   │ .get_doctor_by_ │  │ .get_patient_by_ │  │ .get_appointment_by_│
   │  id()           │  │  id()            │  │  id()               │
   └─────────────────┘  └──────────────────┘  └─────────────────────┘
        │                     │                     │
        └─────────────────────┼─────────────────────┘
                              │
                    ┌─────────▼──────────┐
                    │  Logger (logger)   │
                    │ .info() methods    │
                    │ Write to:          │
                    │ healthcare.log     │
                    └────────────────────┘
```

## 📁 Project Structure

```
day3/
├── pyproject.toml              # Project configuration & dependencies
├── healthcare.log              # Application logs (generated)
├── conf/
│   └── logger_conf.py          # Logging configuration
└── src/
    ├── models/                 # Data models (Business Objects)
    │   ├── __init__.py
    │   ├── doctor.py           # Doctor entity
    │   ├── patient.py          # Patient entity
    │   └── appointment.py      # Appointment entity
    ├── stores/                 # Data storage & CRUD operations
    │   ├── __init__.py
    │   ├── doctorstore.py      # Doctor CRUD operations
    │   ├── patientstore.py     # Patient CRUD operations
    │   └── appointmentstore.py # Appointment CRUD operations
    ├── exception/              # Custom exceptions
    │   ├── __init__.py
    │   ├── doctor_not_found_exception.py
    │   └── patient_not_found_exception.py
    └── utils/
        └── app.py              # Main entry point
```

## 🚀 Installation

### Prerequisites
- Python 3.8+
- pip package manager

### Setup Steps

1. **Navigate to the project directory:**
   ```bash
   cd day3
   ```

2. **Install dependencies:**
   ```bash
   pip install -e .
   ```

3. **Run the application:**
   ```bash
   python src/utils/app.py
   ```

## 💻 Usage

### Running the Application

```bash
cd day3
python src/utils/app.py
```

### What Happens When You Run It

The application executes three sequential operations:

1. **Doctor Creation** - Generates a random doctor with fake data
2. **Patient Creation** - Generates a random patient with fake data
3. **Appointment Creation** - Links the doctor and patient in an appointment

All operations are logged to `healthcare.log` with timestamps and detailed information.

### Viewing Logs

```bash
tail -20 healthcare.log
```

## 📊 Data Models

### 1. Doctor Model (`src/models/doctor.py`)

```python
class Doctor:
    def __init__(self, id: int, name: str, specialization: str):
        self.id = id
        self.name = name
        self.specialization = specialization

    def __str__(self):
        return f"Doctor(id={self.id}, name='{self.name}', specialization='{self.specialization}')"
```

**Attributes:**
- `id`: Unique identifier for each doctor
- `name`: Doctor's full name
- `specialization`: Medical specialization (Cardiology, Surgery, etc.)

**Example Output:**
```
Doctor(id=2049, name='Helen Bray', specialization='Dietitian')
```

### 2. Patient Model (`src/models/patient.py`)

```python
class Patient:
    def __init__(self, id: int, name: str, dob: date, ailment: str):
        self.id = id
        self.name = name
        self.dob = dob
        self.ailment = ailment

    def __str__(self):
        return f"Patient(id={self.id}, name='{self.name}', dob={self.dob}, ailment='{self.ailment}')"
```

**Attributes:**
- `id`: Unique identifier
- `name`: Patient's full name
- `dob`: Date of birth
- `ailment`: Medical condition/ailment

**Example Output:**
```
Patient(id=8679, name='Nicholas Young', dob=1958-07-27, ailment='Door risk method...')
```

### 3. Appointment Model (`src/models/appointment.py`)

```python
class Appointment:
    def __init__(self, id: int, date, time, doctor: Doctor, patient: Patient):
        self.id = id
        self.date = date
        self.time = time
        self.doctor = doctor
        self.patient = patient

    def __str__(self):
        return f"Appointment(id={self.id}, doctor={self.doctor}, patient={self.patient}, date={self.date}, time={self.time})"
```

**Attributes:**
- `id`: Unique appointment ID
- `date`: Appointment date
- `time`: Appointment time
- `doctor`: Reference to Doctor object
- `patient`: Reference to Patient object

**Example Output:**
```
Appointment(id=4447, doctor=Doctor(...), patient=Patient(...), date=2024-09-15, time=14:13:59)
```

## 🗄️ Data Storage Layer

### Repository Pattern Implementation

Each entity has a corresponding Store class that handles CRUD operations.

### 1. DoctorStore (`src/stores/doctorstore.py`)

**CRUD Operations:**

| Method | Purpose | Type |
|--------|---------|------|
| `add_doctor(doctor)` | Add a new doctor to storage | **CREATE** |
| `get_all_doctors()` | Retrieve all doctors | **READ** |
| `get_doctor_by_id(id)` | Find doctor by ID | **READ** |
| `update_doctor(id, name, specialization)` | Modify doctor details | **UPDATE** |
| `delete_doctor(id)` | Remove a doctor from storage | **DELETE** |

**Error Handling:** Raises `DoctorNotFoundException` when doctor doesn't exist

### 2. PatientStore (`src/stores/patientstore.py`)

**CRUD Operations:** Same as DoctorStore
- `add_patient(patient)` - **CREATE**
- `get_all_patients()` - **READ all**
- `get_patient_by_id(id)` - **READ single**
- `update_patient(id, name, age)` - **UPDATE**
- `delete_patient(id)` - **DELETE**

**Error Handling:** Raises `PatientNotFoundException` when patient doesn't exist

### 3. AppointmentStore (`src/stores/appointmentstore.py`)

**CRUD Operations:**
- `add_appointment(appointment)` - **CREATE**
- `get_all_appointments()` - **READ all**
- `get_appointment_by_id(appointment_id)` - **READ single**
- `update_appointment(appointment_id, doctor_id, patient_name, date)` - **UPDATE**
- `delete_appointment(appointment_id)` - **DELETE**

## ⚠️ Exception Handling

### Custom Exceptions

#### DoctorNotFoundException (`src/exception/doctor_not_found_exception.py`)
```python
class DoctorNotFoundException(Exception):
    def __init__(self, message="Doctor not found"):
        self.message = message
        super().__init__(self.message)
```

#### PatientNotFoundException (`src/exception/patient_not_found_exception.py`)
```python
class PatientNotFoundException(Exception):
    def __init__(self, message="Patient not found"):
        self.message = message
        super().__init__(self.message)
```

**Usage:**
```python
# In stores when entity not found
if doctor not found:
    raise DoctorNotFoundException(f"Doctor with ID {id} not found")
```

## 📝 Logging System

### Configuration (`conf/logger_conf.py`)

```python
def setup_logger():
    # Create logger for healthcare application
    logger = logging.getLogger('healthcare_logger')
    logger.setLevel(logging.DEBUG)

    # File handler
    file_handler = logging.FileHandler('healthcare.log')
    logger.setLevel(logging.DEBUG)

    # Formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger
```

**Log Format:**
```
2026-04-17 06:42:06,883 - healthcare_logger - INFO - Doctor added: Doctor(...)
```

**Benefits:**
- ✅ Tracks all operations
- ✅ Debugging information
- ✅ Activity audit trail
- ✅ Performance monitoring

## 🔄 Example Execution

When you run `python src/utils/app.py`, here's what happens:

### Step 1: Doctor Creation
```
Logger: "app doctor agent is running..."
Faker: Generates random doctor
  - ID: 2049
  - Name: Helen Bray
  - Specialization: Dietitian

DoctorStore: Saves doctor
Logger: "Adding doctor: Doctor(id=2049, name='Helen Bray', specialization='Dietitian')"
Logger: "Doctor added: Doctor(id=2049, name='Helen Bray', specialization='Dietitian')"
```

### Step 2: Patient Creation
```
Logger: "app patient agent is running..."
Faker: Generates random patient
  - ID: 8679
  - Name: Nicholas Young
  - DOB: 1958-07-27
  - Ailment: Door risk method total beyond should carry.

Logger: "Patient added: Patient(id=8679, name='Nicholas Young', dob=1958-07-27, ailment='...')"
```

### Step 3: Appointment Creation
```
Logger: "app appointment agent is running..."
Faker: Generates random appointment details
  - ID: 4447
  - Date: 2024-09-15
  - Time: 14:13:59

Logger: "Appointment added: Appointment(id=4447, doctor=Doctor(...), patient=Patient(...), date=2024-09-15, time=14:13:59)"
```

## 🎨 Key Design Patterns

### 1. Repository Pattern (Stores)
- Abstracts data storage logic
- Provides CRUD operations
- Easy to swap storage (in-memory → database)

### 2. Model-View-Controller (MVC)
- **Models**: Doctor, Patient, Appointment (data)
- **Stores**: DoctorStore, PatientStore, AppointmentStore (business logic)
- **View**: Logger output (presentation)

### 3. Singleton Pattern (Logger)
- Only one logger instance throughout the application
- Consistent logging across all modules

### 4. Exception Handling
- Custom exceptions for specific error scenarios
- Prevents application crashes
- Provides meaningful error messages

### 5. Dependency Injection
- Store instances are passed to functions
- Makes testing easier
- Loose coupling between components

## ✨ Features

| Feature | Location | Purpose |
|---------|----------|---------|
| **Object-Oriented Design** | models/*.py | Encapsulation, classes, attributes |
| **CRUD Operations** | stores/*.py | Create, Read, Update, Delete |
| **Exception Handling** | exception/*.py | Graceful error management |
| **Logging System** | conf/logger_conf.py | Activity tracking |
| **Data Generation** | app.py + Faker | Realistic test data |
| **In-Memory Storage** | stores/*.py | Lists as data containers |
| **Relationships** | Appointment model | Doctor-Patient linking |
| **Type Hints** | All files | Code clarity, IDE support |

## 🚀 Extending the Project

### Option 1: Add Database
```python
# Replace in-memory lists with SQL database
# SQLAlchemy ORM
# PostgreSQL / MySQL
```

### Option 2: Add REST API
```python
# FastAPI / Flask
# GET /doctors
# POST /appointments
# PUT /patients/{id}
```

### Option 3: Add Authentication
```python
# User roles (Doctor, Patient, Admin)
# JWT tokens
# Password hashing
```

### Option 4: Add Unit Tests
```python
# pytest
# Test each store's CRUD operations
# Mock data generation
```

## 📋 Dependencies

### Production Dependencies
- `faker>=13.3.4` - For generating fake data

### Development Dependencies
- `pytest>=7.2.0` - For unit testing
- `pytest-cov>=3.0.0` - For test coverage
- `black>=23.3.0` - Code formatting
- `isort>=5.10.0` - Import sorting
- `sphinx>=5.0.0` - Documentation

## 📄 License

This project is part of the Cognizant AI/ML April 2026 training program.

## 👨‍💻 Author

**Shanmuga Lingam**
- Email: shanmugalingam2005@gmail.com

---

## 📊 Sample Log Output

```
2026-04-17 06:42:06,882 - healthcare_logger - INFO - app doctor agent is running...
2026-04-17 06:42:06,882 - healthcare_logger - INFO - Adding doctor: Doctor(id=2049, name='Helen Bray', specialization='Dietitian')
2026-04-17 06:42:06,882 - healthcare_logger - INFO - Retrieving doctor with ID: 2049
2026-04-17 06:42:06,882 - healthcare_logger - INFO - Doctor added: Doctor(id=2049, name='Helen Bray', specialization='Dietitian')
2026-04-17 06:42:06,882 - healthcare_logger - INFO - app patient agent is running...
2026-04-17 06:42:06,883 - healthcare_logger - INFO - Adding patient: Patient(id=8679, name='Nicholas Young', dob=1958-07-27, ailment='Door risk method total beyond should carry.')
2026-04-17 06:42:06,883 - healthcare_logger - INFO - Retrieving patient with ID: 8679
2026-04-17 06:42:06,883 - healthcare_logger - INFO - Patient added: Patient(id=8679, name='Nicholas Young', dob=1958-07-27, ailment='Door risk method total beyond should carry.')
2026-04-17 06:42:06,883 - healthcare_logger - INFO - app appointment agent is running...
2026-04-17 06:42:06,883 - healthcare_logger - INFO - Retrieving doctor with ID: 2049
2026-04-17 06:42:06,883 - - Retrieving patient with ID: 8679
2026-04-17 06:42:06,883 - healthcare_logger - INFO - Adding appointment: Appointment(id=4447, doctor=Doctor(id=2049, name='Helen Bray', specialization='Dietitian'), patient=Patient(id=8679, name='Nicholas Young', dob=1958-07-27, ailment='Door risk method total beyond should carry.'), date=2024-09-15, time=14:13:59)
2026-04-17 06:42:06,883 - healthcare_logger - INFO - Fetching appointment with ID: 4447
2026-04-17 06:42:06,883 - healthcare_logger - INFO - Appointment added: Appointment(id=4447, doctor=Doctor(id=2049, name='Helen Bray', specialization='Dietitian'), patient=Patient(id=8679, name='Nicholas Young', dob=1958-07-27, ailment='Door risk method total beyond should carry.'), date=2024-09-15, time=14:13:59)
```

---

**🏆 This is a professional-grade Healthcare Management System demonstrating enterprise-level software development practices!**</content>
<parameter name="filePath">/workspaces/cognizantaimlapril2026/day3/README.md