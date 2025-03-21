"""
Tests for calculation.py.

This module contains test cases to ensure that the Calculation class performs
correctly for basic arithmetic operations (addition, subtraction, multiplication, and division).
"""

# Import necessary modules for testing
from decimal import Decimal  # Import Decimal for precise floating-point arithmetic
# Import pytest for testing framework support
import pytest

# Import Calculation class and operation functions from the calculator module
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

# Parameterized test cases for different operations
@pytest.mark.parametrize("a, b, operation, expected", [
    (Decimal('10'), Decimal('5'), add, Decimal('15')),  # Addition test
    (Decimal('10'), Decimal('5'), subtract, Decimal('5')),  # Subtraction test
    (Decimal('10'), Decimal('5'), multiply, Decimal('50')),  # Multiplication test
    (Decimal('10'), Decimal('2'), divide, Decimal('5')),  # Division test
    (Decimal('10.5'), Decimal('0.5'), add, Decimal('11.0')),  # Decimal addition test
    (Decimal('10.5'), Decimal('0.5'), subtract, Decimal('10.0')),  # Decimal subtraction test
    (Decimal('10.5'), Decimal('2'), multiply, Decimal('21.0')),  # Decimal multiplication test
    (Decimal('10'), Decimal('0.5'), divide, Decimal('20')),  # Decimal division test
])
def test_calculation_operations(a, b, operation, expected):
    """
    Test calculation operations with various inputs.

    This test ensures that the Calculation class correctly performs different
    arithmetic operations (addition, subtraction, multiplication, and division)
    using the provided input values.

    Parameters:
    -----------
    a (Decimal): The first operand for the operation.
    b (Decimal): The second operand for the operation.
    operation (Callable[[Decimal, Decimal], Decimal]): The operation function (add, subtract, etc.)
    expected (Decimal): The expected result after performing the operation.
    """
    calc = Calculation(a, b, operation)  # Create a Calculation instance with given values
    result = calc.perform()  # Perform the calculation
    assert result == expected, f"Failed {operation.__name__} operation with {a} and {b}. Expected {expected}, got {result}."  # Verify the result

def test_calculation_repr():
    """
    Test the string representation (__repr__) of the Calculation class.

    This test ensures that the __repr__ method correctly formats the string representation
    of the Calculation instance.
    """
    calc = Calculation(Decimal('10'), Decimal('5'), add)  # Create a Calculation instance for testing
    expected_repr = "Calculation(10, 5, add)"  # Define the expected string representation
    actual_repr = calc.__repr__()  # Get the actual string representation
    assert actual_repr == expected_repr, f"The __repr__ method output does not match the expected string. Got: {actual_repr}, Expected: {expected_repr}"

def test_divide_by_zero():
    """
    Test division by zero to ensure it raises a ZeroDivisionError.

    This test checks that dividing a number by zero raises the appropriate exception.
    """
    calc = Calculation(Decimal('10'), Decimal('0'), divide)  # Create a Calculation instance with a zero divisor
    with pytest.raises(ZeroDivisionError, match=".*"):  # Expect a ZeroDivisionError to be raised
        calc.perform()  # Attempt the division operation, which should fail
