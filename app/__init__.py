import logging
import logging.config
import os
from dotenv import load_dotenv
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
        load_dotenv()
        self.settings = self.load_environment_variables()
        self.configure_logging()
        self.logger.info("Initializing application and loading plugins.")
        
        self.command_handler = load_plugins()  # Load plugins dynamically
    
    def configure_logging(self):
        # Define log directory and config path
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Project root
        LOG_CONFIG_PATH = os.path.join(BASE_DIR, self.get_environment_variable('LOG_CONFIG_PATH'))
        LOG_DIR = os.path.join(BASE_DIR, self.get_environment_variable('LOG_FILE'))
        # Ensure log directory exists
        if not os.path.exists(LOG_DIR):
            os.makedirs(LOG_DIR)  # Create the logs directory if it doesn't exist

        # Load logging configuration
        if os.path.exists(LOG_CONFIG_PATH):
            logging.config.fileConfig(LOG_CONFIG_PATH)
        else:
            logging.basicConfig(level=logging.INFO)  # Fallback in case logging.conf is missing
            logging.warning(f"Logging configuration file '{LOG_CONFIG_PATH}' not found. Using default settings.")
        self.logger = logging.getLogger(__name__)
        self.logger.info("Logging is successfully set up.")
    
    def load_environment_variables(self):
        """
        Loads all environment variables into a dictionary.
        Iterates through os.environ.items() and stores each key-value pair in the 'settings' dictionary.
        Logs a message indicating that the environment variables have been loaded.
        
        Returns:
            dict: A dictionary containing all environment variables.
        """
        settings = {key: value for key, value in os.environ.items()}  # Create a dictionary with environment variables
        logging.info("Environment variables loaded.")  # Log the loading process
        return settings  # Return the dictionary with environment variables

    def get_environment_variable(self, env_var: str):
        """
        Retrieves the value of a specific environment variable.
        If the variable is not found, it returns None.

        Args:
            env_var (str): The name of the environment variable to retrieve. Defaults to 'ENVIRONMENT'.
            
        Returns:
            str or None: The value of the environment variable or None if not found.
        """
        return self.settings.get(env_var, None)  # Return the value of the requested environment variable or None

    def start(self):
        """
        Runs the command loop to process user input.

        This method continuously prompts the user for input, processes the command entered,
        and executes the corresponding action. It handles common operations like:
        - Arithmetic operations (e.g., add, subtract)
        - Special commands like 'menu' and 'exit'
        """
        self.logger.info("Application started. Waiting for user input.")
        print("Type 'exit' to exit or 'menu' to enter menu section.")
        while True:
            # Capture and process the user input
            cmd_input = input(">>> ").strip().split()
            
            if not cmd_input:
                continue  # Ignore empty inputs

            cmd_name = cmd_input[0].lower()  # The first part of the input is the command name
            args = cmd_input[1:]  # Remaining parts are arguments for the command
            self.logger.info(f"User input received: {cmd_name} {args}")
    
            # Check if the command is available in the registered commands
            if cmd_name in self.command_handler.commands:
                try:
                    self.logger.info(f"Executing command: {cmd_name}")
                    # Execute the command with the provided arguments
                    self.command_handler.commands[cmd_name].execute(args)
                except Exception as e:
                    self.logger.error(f"Error executing command '{cmd_name}': {e}", exc_info=True)
                    # Handle errors during command execution
                    print(f"Error executing command '{cmd_name}': {e}")
            elif cmd_name == "exit":
                self.logger.info("Exiting application.")
                # Exit the application
                print("Exiting application...")
                break  # Exit the loop and terminate the program
            else:
                self.logger.warning(f"Unknown command: {cmd_name}")
                # Inform the user if the command is not recognized
                print(f"No such command: {cmd_name}")