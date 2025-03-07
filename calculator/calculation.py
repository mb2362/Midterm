#Calculation.py
# Importing Decimal for precise floating-point arithmetic, avoiding rounding errors.
from decimal import Decimal  

# Importing Callable from typing to specify that the operation parameter is a function.
from typing import Callable  

# Importing arithmetic operations from the calculator module.
from calculator.operations import add, subtract, multiply, divide  

class Calculation:
    """
    A class to represent a mathematical calculation.

    This class takes two numeric values and an arithmetic operation function
    (addition, subtraction, multiplication, or division) and performs the operation.

    Attributes:
    -----------
    a : Decimal
        The first operand.
    b : Decimal
        The second operand.
    operation : Callable[[Decimal, Decimal], Decimal]
        A function that performs an arithmetic operation on two Decimal values.
    """

    def __init__(self, a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        """
        Initializes a Calculation instance with two operands and an operation function.

        Parameters:
        -----------
        a (Decimal): The first operand.
        b (Decimal): The second operand.
        operation (Callable[[Decimal, Decimal], Decimal]): The function to apply to a and b.
        """
        self.a = a
        self.b = b
        self.operation = operation

    @staticmethod    
    def create(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]) -> "Calculation":
        """
        Factory method to create a Calculation instance.

        Parameters:
        -----------
        a (Decimal): The first operand.
        b (Decimal): The second operand.
        operation (Callable[[Decimal, Decimal], Decimal]): The function to apply to a and b.

        Returns:
        --------
        Calculation: A new Calculation instance with the given parameters.
        """
        return Calculation(a, b, operation)

    def perform(self) -> Decimal:
        """
        Perform the stored calculation using the given operation.

        Returns:
        --------
        Decimal: The result of applying the operation to a and b.
        """
        return self.operation(self.a, self.b)

    def __repr__(self) -> str:
        """
        Return a string representation of the Calculation object.

        Returns:
        --------
        str: A string representing the calculation, showing the operands and operation name.
        """
        return f"Calculation({self.a}, {self.b}, {self.operation.__name__})"