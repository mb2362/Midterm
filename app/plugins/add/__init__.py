"""
Addition Command.

This module defines the `addCommand` class, which implements the `execute` method
to handle addition operations in the command-line interface.
"""
import logging
# Import CLI as the base class for commands
from app.commands import CLI  

# Import Calculator to perform arithmetic operations
from calculator import Calculator  

# Configure logger
logger = logging.getLogger(__name__)

class addCommand(CLI):
    """
    Command class to handle addition operations.

    This class inherits from `CLI` and implements the `execute` method
    to perform addition using the `Calculator` class.
    """

    def execute(self, args):
        """
        Executes the addition command.

        Parameters:
        -----------
        args (list): List of arguments passed from the command-line input.
                     Expected format: ["number1", "number2"]

        Functionality:
        --------------
        - Validates that exactly two arguments are provided.
        - Converts the arguments to floats.
        - Performs addition using `Calculator.add(a, b)`.
        - Displays the result.
        
        Error Handling:
        ---------------
        - Prints a usage message if incorrect arguments are provided.
        - Handles ValueError if inputs are not valid numbers.
        """
        if len(args) != 2:
            logging.warning("Invalid number of arguments passed to add command.")
            print("Usage: add <a> <b>")
            return

        try:
            a = float(args[0])  # Convert first argument to float
            b = float(args[1])  # Convert second argument to float
            result = Calculator.add(a, b)  # Perform addition using Calculator
            logging.info(f"Addition operation performed: {a} + {b} = {result}")
            print(f"The result of {int(a)} + {int(b)} is equal to {result}")
        except ValueError:
            logging.error(f"Invalid number input: {args[0]} or {args[1]} is not a valid number.")
            print(f"Invalid number input: {args[0]} or {args[1]} is not a valid number.")