"""Calculator"""
# Import necessary modules and classes
from calculator.calculations import Calculations  # Manages history of calculations
from calculator.operations import add, subtract, multiply, divide  # Arithmetic operations
from calculator.calculation import Calculation  # Represents a single calculation
from decimal import Decimal  # For high-precision arithmetic
from typing import Callable  # For type hinting callable objects

class Calculator:
    """
    A simple calculator class that performs basic arithmetic operations.
    The operations include addition, subtraction, multiplication, and division.
    Each operation is performed using the Calculation class to ensure modularity and maintainability.
    """
    @staticmethod
    def _perform_operation(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]) -> Decimal:
        """Create and perform a calculation, then return the result."""
        # Create a Calculation object using the static create method, passing in operands and the operation
        calculation = Calculation.create(a, b, operation)
        # Add the calculation to the history managed by the Calculations class
        Calculations.add_calculation(calculation)
        # Perform the calculation and return the result
        return calculation.perform()

    @staticmethod
    def add(a, b):
        """
        Perform addition of two numbers.

        Parameters:
        a (float): The first number to add.
        b (float): The second number to add.

        Returns:
        float: The result of adding a and b.
        """
        # Perform addition by delegating to the _perform_operation method with the add operation
        return Calculator._perform_operation(a, b, add)

    @staticmethod
    def subtract(a, b):
        """
        Perform subtraction of two numbers.

        Parameters:
        a (float): The number to subtract from.
        b (float): The number to subtract.

        Returns:
        float: The result of subtracting b from a.
        """
        # Perform subtraction by delegating to the _perform_operation method with the subtract operation
        return Calculator._perform_operation(a, b, subtract)

    @staticmethod
    def multiply(a, b):
        """
        Perform multiplication of two numbers.

        Parameters:
        a (float): The first number to multiply.
        b (float): The second number to multiply.

        Returns:
        float: The result of multiplying a and b.
        """
        # Perform multiplication by delegating to the _perform_operation method with the multiply operation
        return Calculator._perform_operation(a, b, multiply)

    @staticmethod
    def divide(a, b):
        """
        Perform division of two numbers.

        Parameters:
        a (float): The numerator (dividend).
        b (float): The denominator (divisor).

        Returns:
        float: The result of dividing a by b.

        Raises:
        ZeroDivisionError: If the denominator (b) is zero.
        """
        # Perform division by delegating to the _perform_operation method with the divide operation
        return Calculator._perform_operation(a, b, divide)