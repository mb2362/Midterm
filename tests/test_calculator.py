'''My Calculator Test'''

# Import pytest for testing framework support
import pytest # pylint: disable=unused-import

# Import the Calculator class from the calculator module
from calculator import Calculator

def test_addition():
    '''Test that the addition function correctly adds two numbers.'''
    # Test with two positive numbers (2 + 2)
    result = Calculator.add(2, 2)  # Perform addition
    assert result == 4, f"Expected 4, but got {result}"  # Assert the expected result

def test_subtraction():
    '''Test that the subtraction function correctly subtracts two numbers.'''
    # Test with two equal numbers (2 - 2)
    result = Calculator.subtract(2, 2)  # Perform subtraction
    assert result == 0, f"Expected 0, but got {result}"  # Assert the expected result

def test_multiply():
    '''Test that the multiplication function correctly multiplies two numbers.'''
    # Test with two positive numbers (2 * 2)
    result = Calculator.multiply(2, 2)  # Perform multiplication
    assert result == 4, f"Expected 4, but got {result}"  # Assert the expected result

def test_divide():
    '''Test that the division function correctly divides two numbers.'''
    # Test with two equal numbers (2 / 2)
    result = Calculator.divide(2, 2)  # Perform division
    assert result == 1, f"Expected 1, but got {result}"  # Assert the expected result

    # Test division by a non-zero number (4 / 2)
    result = Calculator.divide(4, 2)  # Perform division
    assert result == 2, f"Expected 2, but got {result}"  # Assert the expected result

    # Test division by a non-zero decimal number (10 / 2.5)
    result = Calculator.divide(10, 2.5)  # Perform division
    assert result == 4, f"Expected 4, but got {result}"  # Assert the expected result

    # Test division by zero (should raise ZeroDivisionError)
    try:
        Calculator.divide(5, 0)  # Attempt division by zero
        assert False, "Expected ZeroDivisionError, but no exception was raised."
    except ZeroDivisionError:
        pass  # Correct behavior, no action needed
