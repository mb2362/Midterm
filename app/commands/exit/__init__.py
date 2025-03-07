"""
Exit Command.

This module defines the `exitCommand` class, which implements the `execute` method
to terminate the application.
"""

# Import CLI as the base class for commands
from app.commands import CLI  

# Import sys to allow program termination
import sys  

class exitCommand(CLI):
    """
    Command class to handle application exit.

    This class inherits from `CLI` and implements the `execute` method
    to terminate the application when called.
    """

    def execute(self, args):
        """
        Executes the exit command.

        Functionality:
        --------------
        - Prints an exit message to the console.
        - Terminates the program using `sys.exit()`.

        Parameters:
        -----------
        args (list): List of arguments (not used in this command).
        """
        print("Exiting...")  # Inform the user that the application is closing
        sys.exit("Exiting...")  # Terminate the program
