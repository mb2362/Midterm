"""
Multiplication Command.

This module defines the `multiplyCommand` class, which implements the `execute` method
to handle multiplication operations in the command-line interface.
"""

# Import CLI as the base class for commands
import logging
from app.commands import CLI  

# Import Calculator to perform arithmetic operations
from calculator import Calculator  

# Configure logger
logger = logging.getLogger(__name__)

class multiplyCommand(CLI):
    """
    Command class to handle multiplication operations.

    This class inherits from `CLI` and implements the `execute` method
    to perform multiplication using the `Calculator` class.
    """

    def execute(self, args):
        """
        Executes the multiplication command.

        Parameters:
        -----------
        args (list): List of arguments passed from the command-line input.
                     Expected format: ["number1", "number2"]

        Functionality:
        --------------
        - Validates that exactly two arguments are provided.
        - Converts the arguments to floats.
        - Performs multiplication using `Calculator.multiply(a, b)`.
        - Displays the result.

        Error Handling:
        ---------------
        - Prints a usage message if incorrect arguments are provided.
        - Handles ValueError if inputs are not valid numbers.
        """
        if len(args) != 2:
            logger.warning("Invalid number of arguments passed to multiply command.")
            print("Usage: multiply <a> <b>")
            return

        try:
            a = float(args[0])  # Convert first argument to float
            b = float(args[1])  # Convert second argument to float
            result = Calculator.multiply(a, b)  # Perform multiplication using Calculator
            logger.info(f"Multiplication operation performed: {a} x {b} = {result}")
            print(f"The result of {int(a)} x {int(b)} is equal to {result}")

        except ValueError:
            logger.error(f"Invalid number input: {args[0]} or {args[1]} is not a valid number.")
            print(f"Invalid number input: {args[0]} or {args[1]} is not a valid number.")