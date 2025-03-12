# Advanced Python Calculator

## Overview
This project is an **Advanced Python-based Calculator** designed for a software engineering graduate course midterm. It follows professional software development practices, including clean code structure, modular design, comprehensive test coverage, environmental variables and logging.

## Features
- **Basic Arithmetic Operations**: Addition, Subtraction, Multiplication, Division
- **Advanced Calculation Management**: Tracks calculations using a structured approach
- **Test Coverage**: 95%+ test coverage using **Pytest**
- **Error Handling**: Graceful handling of exceptions like division by zero
- **Logging**: Implements structured logging for debugging and tracking calculations
- **Modular Design**: Separated concerns using `operations.py`, `calculation.py`, and `calculations.py`
- **Environment Variables**: Uses `.env` files for configuration management

## Project Structure
```
MIDTERM
├── .github/workflows/          # GitHub Actions for CI/CD
│   ├── python-app.yml          # Workflow configuration for automated testing
├── .pytest_cache/              # Pytest cache directory
├── app/                        # Main application directory
│   ├── __pycache__/            # Compiled Python files
│   ├── commands/               # Command-related modules
│   │   ├── __pycache__/
│   │   ├── __init__.py
│   ├── plugins/                # Plugins for arithmetic operations
│   │   ├── __pycache__/
│   │   ├── add/
│   │   ├── divide/
│   │   ├── exit/
│   │   ├── history/
│   │   ├── menu/
│   │   ├── multiply/
│   │   ├── subtract/
│   │   ├── plugins_manager.py  # Manages plugins
│   │   ├── __init__.py
│   ├── calculator/             # Core calculation logic
│   │   ├── __pycache__/
│   │   ├── __init__.py
│   │   ├── calculation.py
│   │   ├── calculations.py
│   │   ├── operations.py
├── logs/                       # Logging directory
│   ├── app.log                 # Log file for application events
├── test_logs/                  # Log files for tests
├── tests/                      # Unit tests
│   ├── __pycache__/
│   ├── __init__.py
│   ├── test_calculation.py
│   ├── test_calculations.py
│   ├── test_calculator.py
│   ├── test_command.py
│   ├── test_env.py
├── venv/                       # Virtual environment directory
├── .coverage                   # Code coverage report
├── .env                        # Environment variables file
├── .gitignore                  # Git ignore file
├── .pylintrc                   # Pylint configuration
├── logging.conf                 # Logging configuration
├── main.py                      # Entry point of the application
├── pytest.ini                   # Pytest configuration
├── README.md                    # Project documentation (this file)
├── requirements.txt              # Python dependencies
```

## Environment Variables Usage

This project uses environment variables to manage configuration settings securely and flexibly. Environment variables are stored in a `.env` file and loaded using `python-dotenv`.

### How Environment Variables Are Used
- **Logging Configuration**: The path for logging configuration (`LOG_CONFIG_PATH`) and log files (`LOG_FILE`) are read from the `.env` file.
- **History File**: The history of calculations is stored in the file defined by `HISTORY_FILE`.

### Example `.env` File
```
LOG_CONFIG_PATH=logging.conf
LOG_FILE=logs
HISTORY_FILE=history.csv
```

### Code Implementation
Environment variables are loaded in the `App` class:
```python
import os
import logging
import logging.config
from dotenv import load_dotenv

class App:
    def __init__(self):
        load_dotenv()
        self.settings = self.load_environment_variables()
        self.configure_logging()
        self.logger.info("Initializing application and loading plugins.")
        self.command_handler = load_plugins()  # Load plugins dynamically
    
    def configure_logging(self):
        # Define log directory and config path
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Project root
        LOG_CONFIG_PATH = os.path.join(BASE_DIR, self.get_environment_variable('LOG_CONFIG_PATH'))
        LOG_DIR = os.path.join(BASE_DIR, self.get_environment_variable('LOG_FILE'))
        # Ensure log directory exists
        if not os.path.exists(LOG_DIR):
            os.makedirs(LOG_DIR)  # Create the logs directory if it doesn't exist

        # Load logging configuration
        if os.path.exists(LOG_CONFIG_PATH):
            logging.config.fileConfig(LOG_CONFIG_PATH)
        else:
            logging.basicConfig(level=logging.INFO)  # Fallback in case logging.conf is missing
            logging.warning(f"Logging configuration file '{LOG_CONFIG_PATH}' not found. Using default settings.")
        self.logger = logging.getLogger(__name__)
        self.logger.info("Logging is successfully set up.")
    
    def load_environment_variables(self):
        settings = {key: value for key, value in os.environ.items()}  # Create a dictionary with environment variables
        logging.info("Environment variables loaded.")  # Log the loading process
        return settings  # Return the dictionary with environment variables

    def get_environment_variable(self, env_var: str):
        return self.settings.get(env_var, None)  # Return the value of the requested environment variable or None
```

Environment variables are loaded in the `Calculations` class:
```python
HISTORY_FILE = App().get_environment_variable('HISTORY_FILE')
```

By using this approach, we ensure that configuration settings are managed efficiently and securely without hardcoding them into the codebase.

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

## Testing and Coverage
- **Pytest** is used for unit testing in the `tests/` folder.
- **Code coverage** is tracked using `pytest-cov`.
- To check the coverage and generate reports:
  ```sh
  pytest --cov=calculator
  ```
- The **`.coverage`** file stores coverage reports and can be used for further analysis.

## Logging
The calculator includes structured logging for debugging and tracking calculations:

INFO Logs: Tracks operations performed.
ERROR Logs: Captures exceptions and invalid operations.
Logs are written to the console and to a log file.

## Exception Handling
This project implements **"Look Before You Leap" (LBYL)** and **"Easier to Ask for Forgiveness than Permission" (EAFP)** exception-handling strategies:
- **LBYL**: Checks before division by zero.
- **EAFP**: Uses try-except blocks to handle errors dynamically.

## License
This project is for academic purposes only.

## Author
**Monil Baxi**