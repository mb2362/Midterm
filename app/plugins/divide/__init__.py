"""
Division Command.

This module defines the `divideCommand` class, which implements the `execute` method
to handle division operations in the command-line interface.
"""

# Import CLI as the base class for commands
import logging
from app.commands import CLI  

# Import Calculator to perform arithmetic operations
from calculator import Calculator  

# Configure logger
logger = logging.getLogger(__name__)

class divideCommand(CLI):
    """
    Command class to handle division operations.

    This class inherits from `CLI` and implements the `execute` method
    to perform division using the `Calculator` class.
    """

    def execute(self, args):
        """
        Executes the division command.

        Parameters:
        -----------
        args (list): List of arguments passed from the command-line input.
                     Expected format: ["number1", "number2"]

        Functionality:
        --------------
        - Validates that exactly two arguments are provided.
        - Converts the arguments to floats.
        - Checks for division by zero.
        - Performs division using `Calculator.divide(a, b)`.
        - Displays the result.
        
        Error Handling:
        ---------------
        - Prints a usage message if incorrect arguments are provided.
        - Handles ValueError if inputs are not valid numbers.
        - Prevents division by zero and provides a meaningful error message.
        """
        if len(args) != 2:
            logger.warning("Invalid number of arguments passed to divide command.")
            print("Usage: divide <a> <b>")
            return

        try:
            a, b = float(args[0]), float(args[1])  # Convert inputs to floats

            if b == 0:
                logger.error("Attempted division by zero.")
                print("An error occurred: Cannot divide by zero.")
                return

            result = Calculator.divide(a, b)  # Perform division using Calculator
            logger.info(f"Division operation performed: {a} / {b} = {result}")
            print(f"The result of {int(a)} / {int(b)} is equal to {result}")

        except ValueError:
            logger.error(f"Invalid number input: {args[0]} or {args[1]} is not a valid number.")
            print(f"Invalid number input: {args[0]} or {args[1]} is not a valid number.")