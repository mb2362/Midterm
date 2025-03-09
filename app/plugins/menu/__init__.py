"""
Menu Command.

This module defines the `menuCommand` class, which implements the `execute` method
to display the available commands in the application.
"""

# Import CLI as the base class for commands
import logging
from app.commands import CLI  

# Configure logger
logger = logging.getLogger(__name__)

class menuCommand(CLI):
    """
    Command class to display the available commands in the application.

    This class inherits from `CLI` and implements the `execute` method
    to print a list of supported commands and their usage.
    """

    def execute(self, args):
        """
        Executes the menu command.

        Functionality:
        --------------
        - Displays a list of available commands and their descriptions.

        Parameters:
        -----------
        args (list): List of arguments (not used in this command).
        """
        logger.info("Menu command executed. Displaying available commands.")
        print("Available Commands:")
        print("- add <a> <b>: Perform addition")
        print("- subtract <a> <b>: Perform subtraction")
        print("- multiply <a> <b>: Perform multiplication")
        print("- divide <a> <b>: Perform division")
        print("- exit: Exit the application")