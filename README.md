# Advanced Python Calculator  

## Overview  
This project is an **Advanced Python-based Calculator** designed for a software engineering graduate course midterm. It follows professional software development practices, including clean code structure, modular design, comprehensive test coverage, and logging.  

## Features  
- **Basic Arithmetic Operations**: Addition, Subtraction, Multiplication, Division  
- **Advanced Calculation Management**: Tracks calculations using a structured approach  
- **Test Coverage**: 95%+ test coverage using **Pytest**  
- **Error Handling**: Graceful handling of exceptions like division by zero  
- **Logging**: Implements structured logging for debugging and tracking calculations  
- **Dynamically Loaded Logging Configuration**: Automatically ensures logging setup  
- **Modular Design**: Separated concerns using `operations.py`, `calculation.py`, and `calculations.py`  

## Project Structure  
```
MIDTERM  
├── .github/workflows/          # GitHub Actions for CI/CD  
│   ├── python-app.yml          # Workflow configuration for automated testing  
├── .pytest_cache/              # Pytest cache directory  
├── app/                        # Main application directory  
│   ├── commands/               # Command-related modules  
│   │   ├── __init__.py  
│   ├── plugins/                # Plugins for arithmetic operations  
│   │   ├── add/  
│   │   │   ├── __init__.py  
│   │   ├── divide/  
│   │   │   ├── __init__.py  
│   │   ├── exit/  
│   │   │   ├── __init__.py  
│   │   ├── menu/  
│   │   │   ├── __init__.py  
│   │   ├── multiply/  
│   │   │   ├── __init__.py  
│   │   ├── subtract/  
│   │   │   ├── __init__.py  
│   │   ├── plugins_manager.py  # Manages plugins  
│   │   ├── __init__.py  
│   ├── calculator/             # Core calculation logic  
│   │   ├── __init__.py  
│   │   ├── calculation.py  
│   │   ├── calculations.py  
│   │   ├── operations.py  
├── logs/                       # Logging directory  
│   ├── app.log                 # Log file for application events  
├── tests/                      # Unit tests  
│   ├── __init__.py  
│   ├── test_calculation.py  
│   ├── test_calculations.py  
│   ├── test_calculator.py  
│   ├── test_command.py  
│   ├── test_operations.py  
│   ├── test_plugins.py  
├── venv/                       # Virtual environment directory  
├── .coverage                   # Code coverage report  
├── .gitignore                  # Git ignore file  
├── .pylintrc                   # Pylint configuration  
├── logging.conf                 # Logging configuration  
├── main.py                      # Entry point of the application  
├── pytest.ini                   # Pytest configuration  
├── README.md                    # Project documentation (this file)  
├── requirements.txt              # Python dependencies  
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
python main.py 
```  

### Running Tests  
Run the test suite to ensure the calculator functionality is working as expected:  
```sh  
pytest --cov=calculator tests/  
```  

## Logging  

This project implements structured logging to track operations, debug issues, and ensure smooth execution. Logs are recorded in both the console and a dedicated log file(logs/app.log):  

- **INFO Logs**: Tracks operations performed (e.g., additions, subtractions).  
- **WARNING Logs**: Captures potential issues, such as missing configuration files.  
- **ERROR Logs**: Captures exceptions and invalid operations (e.g., division by zero).  

### Dynamically Loading Logging Configuration  

```python  
import os  
import logging  
import logging.config  

# Define log directory and config path  
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  
LOG_CONFIG_PATH = os.path.join(BASE_DIR, "logging.conf")  
LOG_DIR = os.path.join(BASE_DIR, "logs")  

# Ensure log directory exists  
if not os.path.exists(LOG_DIR):  
    os.makedirs(LOG_DIR)  

# Load logging configuration  
if os.path.exists(LOG_CONFIG_PATH):  
    logging.config.fileConfig(LOG_CONFIG_PATH)  
else:  
    logging.basicConfig(level=logging.INFO)  
    logging.warning(f"Logging configuration file '{LOG_CONFIG_PATH}' not found. Using default settings.")  

logger = logging.getLogger(__name__)  
logger.info("Logging is successfully set up.")  
```  

### Where Logging is Used  
- **Calculator module**: Tracks calculations and operations.  
- **Plugins**: Logs arithmetic operations and execution.  
- **Application Initialization**: Ensures logging is configured correctly.  

## License  
This project is for academic purposes only.  

## Author  
**Monil Baxi**