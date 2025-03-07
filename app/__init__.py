from app.plugins.plugins_manager import load_plugins

class App:
    """
    The main application class for the CLI calculator.

    This class is responsible for loading plugins dynamically, handling user input,
    and executing commands. It provides a command loop to interact with the user
    through a text-based interface. The available commands are loaded from plugins
    and can include arithmetic operations (add, subtract, multiply, divide) as well as
    other commands like 'menu' and 'exit'.

    Attributes:
    -----------
    command_handler : CommandHandler
        An instance of CommandHandler that manages and executes the available commands.
    """

    def __init__(self):
        """
        Initializes the App instance.

        This method dynamically loads the commands using the load_plugins function.
        The CommandHandler instance is created, which contains the registered commands.
        """
        self.command_handler = load_plugins()  # Load plugins dynamically

    def start(self):
        """
        Runs the command loop to process user input.

        This method continuously prompts the user for input, processes the command entered,
        and executes the corresponding action. It handles common operations like:
        - Arithmetic operations (e.g., add, subtract)
        - Special commands like 'menu' and 'exit'
        """
        print("Type 'exit' to exit or 'menu' to enter menu section.")
        while True:
            # Capture and process the user input
            cmd_input = input(">>> ").strip().split()
            
            if not cmd_input:
                continue  # Ignore empty inputs

            cmd_name = cmd_input[0].lower()  # The first part of the input is the command name
            args = cmd_input[1:]  # Remaining parts are arguments for the command

            # Check if the command is available in the registered commands
            if cmd_name in self.command_handler.commands:
                try:
                    # Execute the command with the provided arguments
                    self.command_handler.commands[cmd_name].execute(args)
                except Exception as e:
                    # Handle errors during command execution
                    print(f"Error executing command '{cmd_name}': {e}")
            elif cmd_name == "exit":
                # Exit the application
                print("Exiting application...")
                break  # Exit the loop and terminate the program
            else:
                # Inform the user if the command is not recognized
                print(f"No such command: {cmd_name}")