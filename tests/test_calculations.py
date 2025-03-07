'''Tests for Calculations.py'''

# Import required modules
from decimal import Decimal  # Import Decimal for precise arithmetic operations
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
    Calculations.clear_history()  # Reset history before tests
    Calculations.add_calculation(Calculation(Decimal('10'), Decimal('5'), add))  # Add an addition calculation
    Calculations.add_calculation(Calculation(Decimal('20'), Decimal('3'), subtract))  # Add a subtraction calculation

def test_add_calculation(setup_calculations):
    """
    Test adding a calculation to the history.

    Ensures that a new calculation is correctly added to the history
    and becomes the latest calculation.
    """
    calc = Calculation(Decimal('2'), Decimal('2'), add)  # Create a new addition calculation
    Calculations.add_calculation(calc)  # Add calculation to history
    assert Calculations.get_latest() == calc, "Failed to add the calculation to the history"

def test_get_history(setup_calculations):
    """
    Test retrieving the entire calculation history.

    Ensures that the history contains the expected number of calculations.
    """
    history = Calculations.get_history()  # Retrieve history
    assert len(history) == 2, "History does not contain the expected number of calculations"

def test_clear_history(setup_calculations):
    """
    Test clearing the entire calculation history.

    Ensures that all stored calculations are removed from history.
    """
    Calculations.clear_history()  # Clear history
    assert len(Calculations.get_history()) == 0, "History was not cleared"

def test_get_latest(setup_calculations):
    """
    Test getting the latest calculation from the history.

    Ensures that the most recently added calculation is returned as the latest.
    """
    latest = Calculations.get_latest()  # Retrieve latest calculation
    assert latest.a == Decimal('20') and latest.b == Decimal('3'), "Did not get the correct latest calculation"

def test_find_by_operation(setup_calculations):
    """
    Test finding calculations in the history by operation type.

    Ensures that calculations are correctly filtered based on operation names.
    """
    add_operations = Calculations.find_by_operation("add")  # Find all additions
    assert len(add_operations) == 1, "Did not find the correct number of calculations with add operation"

    subtract_operations = Calculations.find_by_operation("subtract")  # Find all subtractions
    assert len(subtract_operations) == 1, "Did not find the correct number of calculations with subtract operation"

def test_get_latest_with_empty_history():
    """
    Test getting the latest calculation when the history is empty.

    Ensures that `get_latest()` correctly returns None when no calculations exist.
    """
    Calculations.clear_history()  # Ensure history is empty
    assert Calculations.get_latest() is None, "Expected None for latest calculation with empty history"
