'''Tests for Calculations.py'''

# Import required modules
from unittest.mock import patch, MagicMock
from decimal import Decimal  # Import Decimal for precise arithmetic operations
import pandas as pd
import pytest  # Import pytest for unit testing framework

# Import necessary classes and functions from the calculator module
from calculator.calculation import Calculation
from calculator.calculations import Calculations
from calculator.operations import add, subtract

@pytest.fixture
def setup_calculations():
    """
    Pytest fixture to set up test data.

    Clears any existing history and adds sample calculations to ensure
    consistent testing conditions.
    """
    # Reset history before each test
    Calculations.clear_history()

    # Add an addition and a subtraction calculation to the history
    Calculations.add_calculation(Calculation(Decimal('10'), Decimal('5'), add))
    Calculations.add_calculation(Calculation(Decimal('20'), Decimal('3'), subtract))

def test_add_calculation(setup_calculations):
    """
    Test adding a calculation to the history.

    Ensures that a new calculation is correctly added to the history
    and becomes the latest calculation.
    """
    # Create a new addition calculation
    calc = Calculation(Decimal('2'), Decimal('2'), add)
    # Add the calculation to the history
    Calculations.add_calculation(calc)
    # Ensure the latest calculation is the one just added
    assert Calculations.get_latest() == calc, "Failed to add the calculation to the history"

def test_get_history(setup_calculations):
    """
    Test retrieving the entire calculation history.

    Ensures that the history contains the expected number of calculations.
    """
    # Retrieve the full history
    history = Calculations.get_history()
    # Assert that there are 2 calculations in the history (from the fixture)
    assert len(history) == 2, "History does not contain the expected number of calculations"

def test_clear_history(setup_calculations):
    """
    Test clearing the entire calculation history.

    Ensures that all stored calculations are removed from history.
    """
    # Clear the history
    Calculations.clear_history()
    # Assert that the history is now empty
    assert len(Calculations.get_history()) == 0, "History was not cleared"

def test_get_latest(setup_calculations):
    """
    Test getting the latest calculation from the history.

    Ensures that the most recently added calculation is returned as the latest.
    """
    # Retrieve the latest calculation
    latest = Calculations.get_latest()
    # Assert that the latest calculation has the expected operands
    assert latest.a == Decimal('20') and latest.b == Decimal('3'), "Did not get the correct latest calculation"

def test_find_by_operation(setup_calculations):
    """
    Test finding calculations in the history by operation type.

    Ensures that calculations are correctly filtered based on operation names.
    """
    # Find all addition calculations
    add_operations = Calculations.find_by_operation("add")
    # Assert that there's one addition operation in the history
    assert len(add_operations) == 1, "Did not find the correct number of calculations with add operation"

    # Find all subtraction calculations
    subtract_operations = Calculations.find_by_operation("subtract")
    # Assert that there's one subtraction operation in the history
    assert len(subtract_operations) == 1, "Did not find the correct number of calculations with subtract operation"

def test_get_latest_with_empty_history():
    """
    Test getting the latest calculation when the history is empty.

    Ensures that `get_latest()` correctly returns None when no calculations exist.
    """
    # Clear the history to ensure it's empty
    Calculations.clear_history()
    # Assert that the latest calculation is None when the history is empty
    assert Calculations.get_latest() is None, "Expected None for latest calculation with empty history"

# History tests
# Mock for Calculation object
@pytest.fixture
def mock_calculation():
    """Fixture to create a mock Calculation object."""
    mock_calc = MagicMock(spec=Calculation)
    mock_calc.a = 2
    mock_calc.b = 2
    mock_calc.operation = add  # Setting operation to 'add'
    mock_calc.operation.__name__ = "add"  # Ensure operation has a name
    mock_calc.perform.return_value = 4  # Mock the result of perform() method
    return mock_calc

# Mock pandas functions
@pytest.fixture
def mock_calculations():
    """Mock the Calculations class to simulate history actions."""
    with patch("pandas.read_csv") as mock_read_csv, patch("pandas.DataFrame.to_csv") as mock_to_csv:
        yield mock_read_csv, mock_to_csv

# Test get_history - check if history is correctly returned
def test_get_history_csv(mock_calculation, mock_calculations):
    """Test the 'get_history' method of the Calculations class."""
    mock_read_csv, _ = mock_calculations # pylint: disable=unused-variable

    # Clear the history before adding a new calculation
    Calculations.history.clear()

    # Simulate adding a calculation to the history
    Calculations.add_calculation(mock_calculation)

    # Call get_history
    history = Calculations.get_history()

    # Assert the history has one calculation
    assert len(history) == 1  # Now it should only contain the mock_calculation
    assert history[0].a == 2
    assert history[0].operation.__name__ == "add"

# Test save_history - check if history is saved correctly
def test_save_history(mock_calculation, mock_calculations, capsys):
    """Test the 'save_history' method of the Calculations class."""
    _, mock_to_csv = mock_calculations

    # Add a calculation to the history
    Calculations.add_calculation(mock_calculation)

    # Call save_history
    Calculations.save_history()

    # Assert that to_csv was called to save the history
    mock_to_csv.assert_called_once()

    # Capture printed output
    captured = capsys.readouterr()
    assert "History saved." in captured.out

# Test load_history - check if history is loaded correctly
def test_load_history(mock_calculation, mock_calculations, capsys):
    """Test the 'load_history' method of the Calculations class."""
    mock_read_csv, _ = mock_calculations

    # Mock the dataframe returned by read_csv
    mock_read_csv.return_value = pd.DataFrame([{
        "Operand1": 2, "Operand2": 2, "Operation": "add", "Result": 4
    }])

    # Call load_history to load mock data
    Calculations.load_history()

    # Capture printed output
    captured = capsys.readouterr()
    assert "History loaded successfully." in captured.out

# Test clear_history - check if history is cleared correctly
def test_clear_history_csv(mock_calculation, mock_calculations, capsys):
    """Test the 'clear_history' method of the Calculations class."""
    _, mock_to_csv = mock_calculations

    # Add a calculation to the history
    Calculations.add_calculation(mock_calculation)

    # Call clear_history
    Calculations.clear_history()

    # Ensure history is cleared
    assert len(Calculations.get_history()) == 0

    # Verify that the history file was written with empty data
    mock_to_csv.assert_called_once()

    # Capture printed output
    captured = capsys.readouterr()
    assert "History cleared." in captured.out
