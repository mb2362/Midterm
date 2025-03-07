"""
Application entry point for handling commands.

This module initializes and starts the application, registering available commands
and providing a command-line interface for user interaction.
"""

# Import required command classes
from app.commands import CommandHandler  # Command manager to handle command registration and execution
from app.commands.add import addCommand  # Command for addition
from app.commands.subtract import subtractCommand  # Command for subtraction
from app.commands.multiply import multiplyCommand  # Command for multiplication
from app.commands.divide import divideCommand  # Command for division
from app.commands.menu import menuCommand  # Command to display menu options
from app.commands.exit import exitCommand  # Command to exit the application

class App:
    """
    The main application class that manages command execution.

    Attributes:
    -----------
    command_handler : CommandHandler
        An instance of CommandHandler to manage available commands.
    """

    def __init__(self):
        """
        Initializes the App instance and sets up the command handler.
        """
        self.command_handler = CommandHandler()  # Initialize command handler

    def start(self):
        """
        Starts the command-line interface (CLI) for the application.

        Registers available commands and enters an interactive loop
        to receive and execute user commands.
        """
        # Register arithmetic operation commands
        self.command_handler.register_command("add", addCommand())
        self.command_handler.register_command("subtract", subtractCommand())
        self.command_handler.register_command("multiply", multiplyCommand())
        self.command_handler.register_command("divide", divideCommand())

        # Register additional utility commands
        self.command_handler.register_command("menu", menuCommand())
        self.command_handler.register_command("exit", exitCommand())

        print("Type 'exit' to exit or 'menu' to enter the menu section.")

        while True:
            cmd_input = input(">>> ").strip().split()  # Read and process user input
            if not cmd_input:
                continue  # Ignore empty input

            cmd_name = cmd_input[0].lower()  # Extract command name
            args = cmd_input[1:]  # Extract command arguments

            if cmd_name in self.command_handler.commands:
                # Execute the corresponding command
                self.command_handler.commands[cmd_name].execute(args)
            else:
                print(f"No such command: {cmd_name}")  # Handle unknown commands