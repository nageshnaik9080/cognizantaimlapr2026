# Cognizant AI ML Training - April 2026

Complete Python e-commerce application learning project with development environment setup, testing, linting, and documentation.

## 📁 Project Structure

```
cognizantaimlapril2026/
└── day2/                          # Main project directory
    ├── pyproject.toml             # Project metadata and dependencies
    ├── day2env/                   # Python virtual environment
    ├── docs/                      # Sphinx documentation
    ├── ecommerce.egg-info/        # Package metadata
    └── src/                       # Source code
        ├── app.py                 # Customer details display application
        ├── start.py               # OTP generation entry point
        ├── models/                # Data models
        │   ├── __init__.py
        │   └── customer.py        # Customer model
        ├── store/                 # Data storage layer
        │   ├── __init__.py
        │   └── customerstore.py   # Customer data management
        └── view/                  # Presentation layer
            ├── __init__.py
            └── customerview.py    # Customer data display
```

## 🛠️ Setup & Installation

### Prerequisites
- Python 3.8+
- pip/venv

### 1. Navigate to Project Directory
```bash
cd day2
```

### 2. Activate Virtual Environment
```bash
# On Linux/macOS
source day2env/bin/activate

# On Windows
day2env\Scripts\activate
```

### 3. Install Dependencies
```bash
# Install project and dependencies
pip install -e .

# Install development dependencies
pip install -e ".[dev]"
```

## 📦 Dependencies

### Production Dependencies
- **faker** (≥13.3.4): Generate fake customer data for testing and demonstration

### Development Dependencies
- **pytest** (≥7.2.0): Unit testing framework
- **pytest-cov** (≥3.0.0): Code coverage reporting
- **black** (≥23.3.0): Code formatter
- **isort** (≥5.10.0): Import statement organizer
- **sphinx** (≥5.0.0): Documentation generator

## 🚀 Running the Application

### Option 1: Display Customer Details
```bash
python src/app.py
```
Generates and displays 100 customer records using the Customer Store and View components.

### Option 2: Generate OTP
```bash
python src/start.py
```
Generates a random 6-digit One Time Password for authentication.

## 🧪 Testing & Code Quality

### Run Unit Tests
```bash
pytest
```

### Generate Coverage Report
```bash
pytest --cov=src
```

### Format Code with Black
```bash
black src/
```

### Organize Imports with isort
```bash
isort src/
```

### Check Code Style
```bash
flake8 src/
```

## 📚 Documentation

### Generate Sphinx Documentation
```bash
cd docs
make html
```

### View Documentation
Open `docs/build/html/index.html` in your browser

### Key Documentation Files
- `docs/source/conf.py`: Sphinx configuration
- `docs/source/index.rst`: Documentation index
- `docs/source/app.rst`: Application documentation
- `docs/source/start.rst`: Startup guide

## 📋 Project Configuration

### pyproject.toml Settings

**Black Configuration:**
- Line length: 88 characters
- Target Python version: 3.13

**Project Metadata:**
- Name: ecommerce
- Version: 1.0.0
- Description: Developing ecommerce application
- Author: Shanmuga Lingam
- Requires Python: ≥3.8

## 🏗️ Application Architecture

### Models Layer (`src/models/`)
Defines data structures for customer entities

### Store Layer (`src/store/`)
Handles customer data management and persistence
- `CustomerStore`: Manages customer data collection

### View Layer (`src/view/`)
Manages presentation and display logic
- `CustomerView`: Displays customer information

## 📝 Main Application Files

### `src/app.py`
Main application demonstrating:
- Customer store initialization with 100 customers
- Displaying customer details through the view layer
- Clean separation of concerns (MVC pattern)

### `src/start.py`
Utility application for:
- Generating secure random OTPs
- 6-digit range (100,000 - 999,999)

## 🔧 Development Workflow

1. **Write code** in `src/`
2. **Format code**: `black src/`
3. **Organize imports**: `isort src/`
4. **Run tests**: `pytest`
5. **Check coverage**: `pytest --cov=src`
6. **Generate docs**: `cd docs && make html`
7. **Review docs**: Open `docs/build/html/index.html`

## 📖 Coding Standards

- **Code formatter**: Black (line length: 88)
- **Import organizer**: isort
- **Linting**: flake8
- **Testing**: pytest with coverage requirements
- **Documentation**: Sphinx with RST format

## ✅ Verification Checklist

After setup, verify:
- [ ] Virtual environment activated
- [ ] All dependencies installed
- [ ] `python src/app.py` runs successfully
- [ ] `python src/start.py` generates OTP
- [ ] `pytest` passes all tests
- [ ] `flake8 src/` shows no errors
- [ ] Documentation builds without errors

## 🤝 Contributors

- Shanmuga Lingam (shanmugalingam2005@gmail.com)

## 📄 License

Educational project for Cognizant AI ML Training program