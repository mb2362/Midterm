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
from app.plugins.history import historyCommand
from app.plugins.plugins_manager import load_plugins
from calculator.calculations import Calculations

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

# History commands tests

@pytest.fixture
def mock_calculations():
    """Mock the Calculations class to simulate history actions."""
    with patch.object(Calculations, 'get_history', return_value=["Calculation(2, 2, add)", "Calculation(5, 3, subtract)"]) as mock_get_history, \
         patch.object(Calculations, 'save_history') as mock_save_history, \
         patch.object(Calculations, 'load_history') as mock_load_history, \
         patch.object(Calculations, 'clear_history') as mock_clear_history:
        yield mock_get_history, mock_save_history, mock_load_history, mock_clear_history

def test_show_history(mock_calculations, capsys):
    """Test the 'show' action of the history command."""

    mock_get_history, _, _, _ = mock_calculations

    # Create historyCommand instance
    command = historyCommand()
    command.show_history()

    # Capture the output
    captured = capsys.readouterr()

    # Ensure the history is displayed correctly
    assert "📜 Calculation History:" in captured.out
    assert "1. Calculation(2, 2, add)" in captured.out
    assert "2. Calculation(5, 3, subtract)" in captured.out

    # Ensure get_history was called
    mock_get_history.assert_called_once()

def test_save_history(mock_calculations, capsys):
    """Test the 'save' action of the history command."""

    _, mock_save_history, _, _ = mock_calculations

    # Create historyCommand instance
    command = historyCommand()
    command.save_history()

    # Capture the output
    captured = capsys.readouterr()

    # Ensure the history save message is printed
    mock_save_history.assert_called_once()
    assert "✅ History saved successfully." in captured.out

def test_load_history(mock_calculations, capsys):
    """Test the 'load' action of the history command."""

    _, _, mock_load_history, _ = mock_calculations

    # Create historyCommand instance
    command = historyCommand()
    command.load_history()

    # Capture the output
    captured = capsys.readouterr()

    # Ensure the history load message is printed
    mock_load_history.assert_called_once()
    assert "✅ History loaded successfully." in captured.out

def test_clear_history(mock_calculations, capsys):
    """Test the 'clear' action of the history command."""

    _, _, _, mock_clear_history = mock_calculations

    # Create historyCommand instance
    command = historyCommand()
    command.clear_history()

    # Capture the output
    captured = capsys.readouterr()

    # Ensure the history clear message is printed
    mock_clear_history.assert_called_once()
    assert "🗑️ History cleared." in captured.out
