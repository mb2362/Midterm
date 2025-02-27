# Basic Python Calculator

## Overview
This project is an Basic Python-based calculator designed for a software engineering graduate course midterm. It follows professional software development practices, including clean code structure.

## Features
- **Basic Arithmetic Operations:** Addition, Subtraction, Multiplication, Division.
- **Test Coverage:** 90%+ test coverage with Pytest.

## Project Structure
```
MIDTERM
│── calculator/             # Core calculator logic
│   ├── __init__.py
│── tests/                  # Unit tests
│   ├── __init__.py
│   ├── test_calculator.py  # Test cases for calculator
│── venv/                   # Virtual environment
│── .coverage               # Coverage report file
│── .gitignore              # Git ignored files
│── .pylintrc               # Pylint configuration
│── pytest.ini              # Pytest configuration
│── README.md               # Project documentation
│── requirements.txt        # Project dependencies
```

## Installation

### 1. Clone the Repository
```sh
git clone https://github.com/mb2362/Midterm.git
cd MIDTERM
```

### 2. Create a Virtual Environment
```sh
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

## Usage
### Running the Calculator
```sh
python -m calculator
```

### Running Tests
```sh
pytest --cov=calculator tests/
```

## Testing and Coverage
- Pytest is used for testing (`tests/` folder).
- Code coverage is tracked using `pytest-cov`.
- To check coverage:
  ```sh
  pytest --cov=calculator
  ```
- The `.coverage` file stores coverage reports.

## License
This project is for academic purposes only.  

## Author
Monil Baxi
