"""
Unit tests for command classes in the CLI calculator application.
"""

from unittest.mock import patch
import pytest   # pylint: disable=unused-import
from app import App
from app.commands import CommandHandler, CLI
from app.commands.add import addCommand
from app.commands.subtract import subtractCommand
from app.commands.multiply import multiplyCommand
from app.commands.divide import divideCommand

def test_app_init():
    """Test that the App initializes with a CommandHandler."""
    app = App()
    assert app.command_handler is not None  # Ensure the CommandHandler is initialized

def test_app_start_menu_command():
    """Test App start method handling a menu command."""
    app = App()
    with patch("builtins.input", side_effect=["menu", "exit"]), patch("builtins.print") as mock_print:
        with pytest.raises(SystemExit):  # Exit after calling 'exit'
            app.start()
    # Verify that the menu command is recognized
    mock_print.assert_any_call("Available Commands:")   # Correct output
    mock_print.assert_any_call("- add <a> <b>: Perform addition")  # Additional menu info
    mock_print.assert_any_call("- subtract <a> <b>: Perform subtraction")  # Subtraction menu info
    mock_print.assert_any_call("- multiply <a> <b>: Perform multiplication")    # Multiplication menu info
    mock_print.assert_any_call("- divide <a> <b>: Perform division")    # Division menu info
    mock_print.assert_any_call("- exit: Exit the application")  # Correct exit message

def test_app_invalid_command():
    """Test handling of an invalid command."""
    app = App()
    with patch("builtins.input", side_effect=["unknown", "exit"]), patch("builtins.print") as mock_print:
        with pytest.raises(SystemExit):
            app.start()
    mock_print.assert_any_call("No such command: unknown")

def test_add_command(capfd):
    """Test addition command with valid inputs."""
    command = addCommand()
    command.execute(["5", "3"])
    out, _ = capfd.readouterr()
    assert out == "The result of 5 + 3 is equal to 8.0\n"

def test_subtract_command(capfd):
    """Test subtraction command with valid inputs."""
    command = subtractCommand()
    command.execute(["10", "2"])
    out, _ = capfd.readouterr()
    assert out == "The result of 10 - 2 is equal to 8.0\n"

def test_multiply_command(capfd):
    """Test multiplication command with valid inputs."""
    command = multiplyCommand()
    command.execute(["4", "5"])
    out, _ = capfd.readouterr()
    assert out == "The result of 4 x 5 is equal to 20.0\n"

def test_divide_command(capfd):
    """Test division command with valid inputs."""
    command = divideCommand()
    command.execute(["20", "4"])
    out, _ = capfd.readouterr()
    assert out == "The result of 20 / 4 is equal to 5.0\n"

class DummyCommand(CLI):
    """A dummy command for testing CommandHandler functionality."""
    def execute(self, args):
        super().execute(args)
        print("Dummy executed")

def test_execute_command_success(capfd):
    """Test that a registered command is executed successfully."""
    handler = CommandHandler()
    handler.register_command("dummy", DummyCommand())
    handler.execute_command("dummy")
    out, _ = capfd.readouterr()
    assert "Dummy executed" in out

def test_execute_command_keyerror(capfd):
    """Test that calling an unregistered command prints an error message."""
    handler = CommandHandler()
    handler.execute_command("nonexistent")
    out, _ = capfd.readouterr()
    assert "No such command: nonexistent" in out

def test_add_command_missing_arguments(capfd):
    """Test addCommand with missing arguments."""
    command = addCommand()
    command.execute([])  # No arguments provided
    out, _ = capfd.readouterr()
    assert out == "Usage: add <a> <b>\n"

def test_add_command_invalid_argument(capfd):
    """Test addCommand with non-numeric argument."""
    command = addCommand()
    command.execute(["5", "b"])
    out, _ = capfd.readouterr()
    assert out == "Invalid number input: 5 or b is not a valid number.\n"

def test_divide_command_invalid_argument_2(capfd):
    """Test divideCommand with division by zero."""
    command = divideCommand()
    command.execute(["5", "0"])
    out, _ = capfd.readouterr()
    assert out == "An error occurred: Cannot divide by zero.\n"

def test_multiply_command_missing_arguments(capfd):
    """Test multiplyCommand with missing arguments."""
    command = multiplyCommand()
    command.execute([])  # No arguments provided
    out, _ = capfd.readouterr()
    assert out == "Usage: multiply <a> <b>\n"

def test_subtract_command_missing_arguments(capfd):
    """Test subtractCommand with missing arguments."""
    command = subtractCommand()
    command.execute([])  # No arguments provided
    out, _ = capfd.readouterr()
    assert out == "Usage: subtract <a> <b>\n"

def test_subtract_command_invalid(capfd):
    """Test subtractCommand with non-numeric argument."""
    command = subtractCommand()
    command.execute(["5", "b"])
    out, _ = capfd.readouterr()
    assert out == "Invalid number input: 5 or b is not a valid number.\n"
