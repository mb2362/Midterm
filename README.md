# Advanced Python Calculator

## Overview
This project is an **Advanced Python-based Calculator** designed for a software engineering graduate course midterm. It follows professional software development practices, including clean code structure, modular design, comprehensive test coverage.

## Features
- **Basic Arithmetic Operations**: Addition, Subtraction, Multiplication, Division
- **Advanced Calculation Management**: Tracks calculations using a structured approach
- **Test Coverage**: 95%+ test coverage using **Pytest**
- **Error Handling**: Graceful handling of exceptions like division by zero
- **Modular Design**: Separated concerns using `operations.py`, `calculation.py`, and `calculations.py`

## Project Structure
```
MIDTERM
│── .github/                # GitHub workflows (if applicable)
│── .pytest_cache/          # Pytest cache files
│── app/                    # Application logic
│   ├── __pycache__/
│   ├── __init__.py
│   ├── commands/           # CLI commands
│   │   ├── __pycache__/
│   │   ├── add/
│   │   ├── divide/
│   │   ├── exit/
│   │   ├── menu/
│   │   ├── multiply/
│   │   ├── subtract/
│   │   ├── __init__.py
│── calculator/             # Core calculator logic
│   ├── __pycache__/
│   ├── __init__.py
│   ├── calculation.py      # Main calculation logic
│   ├── calculations.py     # Handles multiple calculations
│   ├── operations.py       # Functions for arithmetic operations
│── tests/                  # Unit tests
│   ├── __pycache__/
│   ├── __init__.py
│   ├── test_calculation.py  # Tests for single calculation logic
│   ├── test_calculations.py # Tests for multiple calculations handling
│   ├── test_calculator.py   # Tests for overall calculator
│   ├── test_command.py      # Tests for CLI commands
│   ├── test_operations.py   # Tests for operations functions
│── venv/                   # Virtual environment
│── .coverage               # Coverage report file
│── .gitignore              # Git ignored files
│── .pylintrc               # Pylint configuration for code linting
│── main.py                 # Main entry point
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
You can run the calculator in interactive mode via the command line:
```sh
python -m calculator
```

### Running Tests
Run the test suite to ensure the calculator functionality is working as expected:
```sh
pytest --cov=calculator tests/
```

## Testing and Coverage
- **Pytest** is used for unit testing in the `tests/` folder.
- **Code coverage** is tracked using `pytest-cov`.
- To check the coverage and generate reports:
  ```sh
  pytest --cov=calculator
  ```
- The **`.coverage`** file stores coverage reports and can be used for further analysis.

## Exception Handling
This project implements **"Look Before You Leap" (LBYL)** and **"Easier to Ask for Forgiveness than Permission" (EAFP)** exception-handling strategies:
- **LBYL**: Checks before division by zero.
- **EAFP**: Uses try-except blocks to handle errors dynamically.

## License
This project is for academic purposes only.

## Author
**Monil Baxi**