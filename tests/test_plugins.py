"""
Unit tests for the plugin manager in the CLI calculator application.

These tests verify the dynamic loading and error handling of plugins. The plugin manager
is responsible for loading commands such as 'add', 'subtract', 'multiply', 'divide', 
'menu', and 'exit' from dynamically imported plugin modules. These tests ensure the 
correct behavior of the plugin manager under various scenarios, including successful 
plugin loading, handling missing plugins, and error handling when a plugin fails to load.
"""

from unittest.mock import patch
import pytest   # pylint: disable=unused-import
from app.commands import CommandHandler
from app.plugins.plugins_manager import load_plugins

def test_plugins_load():
    """Test that plugins are loaded dynamically."""
    # Load plugins and check that the necessary commands are registered
    command_handler = load_plugins()
    # Ensure the expected commands are available
    assert "add" in command_handler.commands
    assert "subtract" in command_handler.commands
    assert "multiply" in command_handler.commands
    assert "divide" in command_handler.commands
    assert "menu" in command_handler.commands
    assert "exit" in command_handler.commands

def test_plugins_manager_dynamic_loading():
    """Test that the plugins manager correctly loads available plugins."""
    # Load plugins and check the type of the command handler
    command_handler = load_plugins()
    # Ensure the command handler is an instance of CommandHandler
    assert isinstance(command_handler, CommandHandler)
    # Ensure the necessary commands are available
    assert "add" in command_handler.commands
    assert "subtract" in command_handler.commands
    assert "multiply" in command_handler.commands
    assert "divide" in command_handler.commands

def test_plugins_manager_handles_missing_plugin():
    """Test plugins manager's handling of non-existent plugins."""
    # Load plugins and verify non-existent plugins are not in the command list
    command_handler = load_plugins()
    # Assert that a plugin not present in the system is not loaded
    assert "nonexistent" not in command_handler.commands

def test_plugins_manager_error_handling():
    """Test that the plugins manager does not crash on errors."""
    # Simulate a plugin import error
    with patch("importlib.import_module", side_effect=ImportError("Fake error")):
        # Load plugins and ensure that CommandHandler is still returned, even with an error
        command_handler = load_plugins()
        assert isinstance(command_handler, CommandHandler)
