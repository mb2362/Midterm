"""
Calculation Module.

This module defines the `Calculation` class, which represents a mathematical
calculation involving two operands and an arithmetic operation.
The class performs the specified operation (addition, subtraction, multiplication, or division)
and returns the result.
"""

# Import logging
import logging

# Import Decimal for precise floating-point arithmetic, avoiding rounding errors
from decimal import Decimal  

# Import Callable from typing to specify that the operation parameter is a function
from typing import Callable  

# Import arithmetic operations from the calculator module
from calculator.operations import add, subtract, multiply, divide  

# Configure logger
logger = logging.getLogger(__name__)

class Calculation:
    """
    A class to represent a mathematical calculation.

    This class takes two numeric values (operands) and an arithmetic operation function 
    (addition, subtraction, multiplication, or division) and performs the operation.

    Attributes:
    -----------
    a : Decimal
        The first operand (input number).
    b : Decimal
        The second operand (input number).
    operation : Callable[[Decimal, Decimal], Decimal]
        A function that performs an arithmetic operation on two Decimal values.
    """

    def __init__(self, a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        """
        Initializes a Calculation instance with two operands and an operation function.

        Parameters:
        -----------
        a (Decimal): The first operand (input number).
        b (Decimal): The second operand (input number).
        operation (Callable[[Decimal, Decimal], Decimal]): The function to apply to a and b.
        """
        self.a = a
        self.b = b
        self.operation = operation
        logger.debug(f"Initialized Calculation with a={a}, b={b}, operation={operation.__name__}")

    @staticmethod    
    def create(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]) -> "Calculation":
        """
        Factory method to create a Calculation instance.

        This method creates an instance of `Calculation` using the provided operands
        and the operation function.

        Parameters:
        -----------
        a (Decimal): The first operand (input number).
        b (Decimal): The second operand (input number).
        operation (Callable[[Decimal, Decimal], Decimal]): The operation function to apply.

        Returns:
        --------
        Calculation: A new `Calculation` instance with the provided parameters.
        """
        logger.debug(f"Creating Calculation instance with a={a}, b={b}, operation={operation.__name__}")
        return Calculation(a, b, operation)

    def perform(self) -> Decimal:
        """
        Perform the stored calculation using the given operation.

        This method applies the stored operation (addition, subtraction, multiplication, or division)
        to the operands `a` and `b`, and returns the result.

        Returns:
        --------
        Decimal: The result of applying the operation to `a` and `b`.
        """
        logger.debug(f"Performing calculation: {self.a} {self.operation.__name__} {self.b}")
        result = self.operation(self.a, self.b)
        logger.debug(f"Calculation result: {result}")
        return result

    def __repr__(self) -> str:
        """
        Return a string representation of the Calculation object.

        This method returns a string that clearly represents the calculation,
        showing the operands and the operation name.

        Returns:
        --------
        str: A string representing the `Calculation` object.
        """
        return f"Calculation({self.a}, {self.b}, {self.operation.__name__})"