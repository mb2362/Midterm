import importlib
import logging
import os
from app.commands import CommandHandler

PLUGIN_FOLDER = "app.plugins"

# Configure logger
logger = logging.getLogger(__name__)

def load_plugins():
    """
    Dynamically load all plugins from subdirectories within the plugins folder.

    This function scans the plugins directory for subdirectories. Each subdirectory is
    treated as a plugin module and must contain an `__init__.py` file to be considered valid.
    The function attempts to dynamically import each plugin and register its corresponding command
    class with the `CommandHandler`. The class name is expected to follow the pattern 
    `<plugin_name>Command` (e.g., `addCommand` for the `add` plugin).

    Returns:
    --------
    CommandHandler
        The command handler instance populated with the dynamically loaded commands from the plugins.
    """
    command_handler = CommandHandler()  # Initialize a new CommandHandler instance
    plugin_path = os.path.dirname(__file__)  # Get the path to the plugins directory

    # Iterate over the items in the plugins directory
    for folder in os.listdir(plugin_path):
        plugin_dir = os.path.join(plugin_path, folder)
        
        # Ensure the folder is a directory and contains an __init__.py file (valid Python package)
        if os.path.isdir(plugin_dir) and "__init__.py" in os.listdir(plugin_dir):
            module_name = f"{PLUGIN_FOLDER}.{folder}"  # Convert folder name to module path
            
            try:
                # Dynamically import the plugin module
                module = importlib.import_module(module_name)
                
                # Construct the expected command class name based on the folder name
                command_class_name = f"{folder}Command"  # e.g., "addCommand" for "add" folder
                
                # Get the command class dynamically from the module
                command_class = getattr(module, command_class_name, None)

                # Register the command class if found
                if command_class:
                    command_handler.register_command(folder, command_class())  # Register the command
                    logger.info(f"Successfully loaded plugin: {module_name} -> {command_class_name}")
                else:
                    logger.warning(f"⚠ Warning: {command_class_name} not found in {module_name}")
            except Exception as e:
                logger.error(f"❌ Error loading plugin {module_name}: {e}")

    return command_handler  # Return the populated command handler