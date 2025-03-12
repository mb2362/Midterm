"""
Subtraction Command.

This module defines the `subtractCommand` class, which implements the `execute` method
to handle subtraction operations in the command-line interface.
"""

# Import CLI as the base class for commands
import logging
from app.commands import CLI  

# Import Calculator to perform arithmetic operations
from calculator import Calculator  

# Configure logger
logger = logging.getLogger(__name__)

class subtractCommand(CLI):
    """
    Command class to handle subtraction operations.

    This class inherits from `CLI` and implements the `execute` method
    to perform subtraction using the `Calculator` class.
    """

    def execute(self, args):
        """
        Executes the subtraction command.

        Parameters:
        -----------
        args (list): List of arguments passed from the command-line input.
                     Expected format: ["number1", "number2"]

        Functionality:
        --------------
        - Validates that exactly two arguments are provided.
        - Converts the arguments to floats.
        - Performs subtraction using `Calculator.subtract(a, b)`.
        - Displays the result.

        Error Handling:
        ---------------
        - Prints a usage message if incorrect arguments are provided.
        - Handles ValueError if inputs are not valid numbers.
        """
        if len(args) != 2:
            logger.warning("Invalid number of arguments passed to subtract command.")
            print("Usage: subtract <a> <b>")
            return

        try:
            a = float(args[0])  # Convert first argument to float
            b = float(args[1])  # Convert second argument to float
            result = Calculator.subtract(a, b)  # Perform subtraction using Calculator
            logger.info(f"Subtraction operation performed: {a} - {b} = {result}")
            print(f"The result of {int(a)} - {int(b)} is equal to {result}")

        except ValueError:
            logger.error(f"Invalid number input: {args[0]} or {args[1]} is not a valid number.")
            print(f"Invalid number input: {args[0]} or {args[1]} is not a valid number.")