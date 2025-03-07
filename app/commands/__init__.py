"""
Command Handling System.

This module defines an abstract base class (CLI) for commands and a CommandHandler
to register and execute commands in the application.
"""

# Import ABC and abstractmethod to define an abstract base class for commands
from abc import ABC, abstractmethod  

class CLI(ABC):
    """
    Abstract Base Class (ABC) for command-line commands.

    Any command that inherits from this class must implement the `execute` method.
    """

    @abstractmethod
    def execute(self, args):
        """
        Execute the command.

        Parameters:
        -----------
        args (list): List of arguments passed to the command.
        """
        pass  # To be implemented by subclasses

class CommandHandler:
    """
    A class that manages the registration and execution of commands.

    Attributes:
    -----------
    commands : dict
        A dictionary mapping command names to command instances.
    """

    def __init__(self):
        """
        Initializes a CommandHandler instance with an empty command dictionary.
        """
        self.commands = {}  # Dictionary to store registered commands

    def register_command(self, command_name: str, command: CLI):
        """
        Registers a new command in the command handler.

        Parameters:
        -----------
        command_name (str): The name of the command.
        command (CLI): An instance of a command class inheriting from CLI.
        """
        self.commands[command_name] = command  # Store the command in the dictionary

    def execute_command(self, command_name: str):
        """
        Executes a registered command.

        Parameters:
        -----------
        command_name (str): The name of the command to execute.

        Raises:
        -------
        KeyError: If the command does not exist in the registry.
        """
        try:
            self.commands[command_name].execute([])  # Execute command with empty argument list
        except KeyError:
            print(f"No such command: {command_name}")  # Handle missing command gracefully