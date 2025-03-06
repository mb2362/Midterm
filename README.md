
# Intermediate Python Calculator

## Overview
This project is a **Intermediate Python-based Calculator** designed for a software engineering graduate course midterm. It follows professional software development practices, including clean code structure, modular design, and comprehensive test coverage.

## Features
- **Basic Arithmetic Operations**: Addition, Subtraction, Multiplication, Division
- **Test Coverage**: 95%+ test coverage using **Pytest**
- **Error Handling**: Graceful handling of edge cases like division by zero.

## Project Structure
```
MIDTERM
│── calculator/             # Core calculator logic
│   ├── __init__.py
│   ├── operations.py      # Functions for arithmetic operations
│   ├── calculation.py     # Main calculation logic (new file)
│── tests/                  # Unit tests
│   ├── __init__.py
│   ├── test_calculator.py  # Test cases for the calculator
│   ├── test_operations.py      # Test cases for operations (new file)
│── venv/                   # Virtual environment
│── .coverage               # Coverage report file
│── .gitignore              # Git ignored files
│── .pylintrc               # Pylint configuration for code linting
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

## License
This project is for academic purposes only.

## Author
**Monil Baxi**
