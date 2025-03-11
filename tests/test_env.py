"""
Unit Tests for Environment Variable Management in the App.

This test module verifies the correct functionality of:
- `load_environment_variables()`: Ensures environment variables are loaded properly.
- `get_environment_variable()`: Ensures retrieval of specific environment variables.

Test Features:
- Uses `unittest.mock.patch.dict` to simulate environment variables.
- Validates logging output using `caplog`.
- Ensures missing environment variables return `None`.

Run tests using:
    pytest --cov=app --cov-report=term-missing
"""

import os
import logging
from unittest.mock import patch
import pytest        # pylint: disable=unused-import
from app import App  # Assuming your App class initializes environment variables

def test_load_environment_variables(caplog):
    """
    Test Case: Load Environment Variables
    
    Description:
    This test ensures that the `load_environment_variables` method correctly loads
    environment variables into a dictionary and logs the appropriate message.

    Test Steps:
    1. Mock environment variables using `patch.dict(os.environ, mock_env_vars)`.
    2. Initialize the `App` class, which calls `load_environment_variables`.
    3. Verify that the environment variables are correctly stored in `app.settings`.
    4. Capture and validate the logging output to ensure that the method logs
       "Environment variables loaded.".

    Assertions:
    - The environment variables should be present in `app.settings` with expected values.
    - The expected log message should appear in the captured logs.
    
    Args:
        caplog (pytest fixture): Captures logging output for verification.
    """
    # Mock environment variables
    mock_env_vars = {
        "LOG_CONFIG_PATH": "test_logging.conf",
        "LOG_FILE": "test_logs",
        "HISTORY_FILE": "test_history.csv"
    }

    with patch.dict(os.environ, mock_env_vars):  # Override os.environ with mock values
        app = App()  # Initialize App, which loads environment variables

        # Check if environment variables are loaded correctly
        assert app.settings["LOG_CONFIG_PATH"] == "test_logging.conf"
        assert app.settings["LOG_FILE"] == "test_logs"
        assert app.settings["HISTORY_FILE"] == "test_history.csv"

        # Verify logging output
        with caplog.at_level(logging.INFO):
            app.load_environment_variables()
            assert "Environment variables loaded." in caplog.text

def test_get_environment_variable():
    """
    Test Case: Retrieve Environment Variable
    
    Description:
    This test verifies that the `get_environment_variable` method correctly retrieves
    existing environment variables and returns `None` when the requested variable is missing.

    Test Steps:
    1. Mock environment variables using `patch.dict(os.environ, mock_env_vars)`.
    2. Initialize the `App` class, which loads environment variables.
    3. Call `get_environment_variable` with different variable names.
    4. Validate that existing environment variables return correct values.
    5. Check that requesting a non-existent variable returns `None`.

    Assertions:
    - Existing environment variables should return the correct values.
    - A non-existent variable should return `None`.
    """
    # Mock environment variables
    mock_env_vars = {
        "LOG_CONFIG_PATH": "test_logging.conf",
        "LOG_FILE": "test_logs",
        "HISTORY_FILE": "test_history.csv"
    }

    with patch.dict(os.environ, mock_env_vars):
        app = App()  # Initialize App, which loads environment variables

        # Check existing environment variables
        assert app.get_environment_variable("LOG_CONFIG_PATH") == "test_logging.conf"
        assert app.get_environment_variable("LOG_FILE") == "test_logs"
        assert app.get_environment_variable("HISTORY_FILE") == "test_history.csv"

        # Check for a missing environment variable
        assert app.get_environment_variable("MISSING_VAR") is None  # Should return None
