"""Calculator Module.

This module defines the `Calculator` class, which provides basic arithmetic 
operations (addition, subtraction, multiplication, and division). Each operation 
is performed using the `Calculation` class to ensure modularity and maintainability.
"""

# Import necessary modules and classes
from decimal import Decimal  # For high-precision arithmetic
from typing import Callable  # For type hinting callable objects

# Import arithmetic operations and calculation management classes
from calculator.calculations import Calculations  # Manages history of calculations
from calculator.operations import add, subtract, multiply, divide  # Arithmetic operations
from calculator.calculation import Calculation  # Represents a single calculation

class Calculator:
    """
    A simple calculator class that performs basic arithmetic operations.

    This class supports:
    - Addition
    - Subtraction
    - Multiplication
    - Division

    Each operation is performed using the `Calculation` class, ensuring modularity 
    and maintainability. All calculations are stored in history using `Calculations`.
    """

    @staticmethod
    def _perform_operation(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]) -> Decimal:
        """
        Create and perform a calculation, then return the result.

        This method:
        1. Creates a `Calculation` object.
        2. Adds it to the history using `Calculations`.
        3. Executes the operation and returns the result.

        Parameters:
        -----------
        a (Decimal): The first operand.
        b (Decimal): The second operand.
        operation (Callable[[Decimal, Decimal], Decimal]): The function representing the operation.

        Returns:
        --------
        Decimal: The result of the operation.
        """
        # Create a Calculation object
        calculation = Calculation.create(a, b, operation)
        # Store the calculation in history
        Calculations.add_calculation(calculation)
        # Perform the calculation and return the result
        return calculation.perform()

    @staticmethod
    def add(a: Decimal, b: Decimal) -> Decimal:
        """
        Perform addition of two numbers.

        Parameters:
        -----------
        a (Decimal): The first number to add.
        b (Decimal): The second number to add.

        Returns:
        --------
        Decimal: The result of adding `a` and `b`.
        """
        return Calculator._perform_operation(a, b, add)

    @staticmethod
    def subtract(a: Decimal, b: Decimal) -> Decimal:
        """
        Perform subtraction of two numbers.

        Parameters:
        -----------
        a (Decimal): The number to subtract from.
        b (Decimal): The number to subtract.

        Returns:
        --------
        Decimal: The result of subtracting `b` from `a`.
        """
        return Calculator._perform_operation(a, b, subtract)

    @staticmethod
    def multiply(a: Decimal, b: Decimal) -> Decimal:
        """
        Perform multiplication of two numbers.

        Parameters:
        -----------
        a (Decimal): The first number to multiply.
        b (Decimal): The second number to multiply.

        Returns:
        --------
        Decimal: The result of multiplying `a` and `b`.
        """
        return Calculator._perform_operation(a, b, multiply)

    @staticmethod
    def divide(a: Decimal, b: Decimal) -> Decimal:
        """
        Perform division of two numbers.

        Parameters:
        -----------
        a (Decimal): The numerator (dividend).
        b (Decimal): The denominator (divisor).

        Returns:
        --------
        Decimal: The result of dividing `a` by `b`.

        Raises:
        -------
        ZeroDivisionError: If `b` is zero.
        """
        if b == Decimal('0'):
            raise ZeroDivisionError("Cannot divide by zero.")
        return Calculator._perform_operation(a, b, divide)