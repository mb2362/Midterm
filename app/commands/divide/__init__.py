"""
Division Command.

This module defines the `divideCommand` class, which implements the `execute` method
to handle division operations in the command-line interface.
"""

# Import CLI as the base class for commands
from app.commands import CLI  

# Import Calculator to perform arithmetic operations
from calculator import Calculator  

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
            print("Usage: divide <a> <b>")  # Inform the user of correct command format
            return

        try:
            a, b = float(args[0]), float(args[1])  # Convert inputs to floats

            if b == 0:
                print("An error occurred: Cannot divide by zero.")  # Prevent division by zero
                return

            result = Calculator.divide(a, b)  # Perform division using Calculator
            print(f"The result of {int(a)} / {int(b)} is equal to {result}")  # Display result

        except ValueError:
            print(f"Invalid number input: {args[0]} or {args[1]} is not a valid number.")  # Handle invalid input