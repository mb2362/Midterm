from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

class Calculator:
    """
    A simple calculator class that performs basic arithmetic operations.
    The operations include addition, subtraction, multiplication, and division.
    Each operation is performed using the Calculation class to ensure modularity and maintainability.
    """

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
        # Create a Calculation object for the addition operation
        calculation = Calculation(a, b, add)  # Pass the add function from calculator.operations
        return calculation.get_result()  # Return the result from the Calculation object

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
        # Create a Calculation object for the subtraction operation
        calculation = Calculation(a, b, subtract)  # Pass the subtract function from calculator.operations
        return calculation.get_result()  # Return the result from the Calculation object

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
        # Create a Calculation object for the multiplication operation
        calculation = Calculation(a, b, multiply)  # Pass the multiply function from calculator.operations
        return calculation.get_result()  # Return the result from the Calculation object

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
        # Create a Calculation object for the division operation
        calculation = Calculation(a, b, divide)  # Pass the divide function from calculator.operations
        return calculation.get_result()  # Return the result from the Calculation object