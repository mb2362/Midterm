import logging
from app.commands import CLI
from calculator.calculations import Calculations

logger = logging.getLogger(__name__)

class historyCommand(CLI):
    """
    Command class to manage calculation history.
    
    Supports:
    - Viewing history (`history show`)
    - Saving history (`history save`)
    - Loading history (`history load`)
    - Clearing history (`history clear`)
    """

    def execute(self, args):
        """Executes the history command with the given arguments."""
        if not args:
            print("Usage: history <show|save|load|clear>")
            return

        action = args[0].lower()

        if action == "show":
            self.show_history()
        elif action == "save":
            self.save_history()
        elif action == "load":
            self.load_history()
        elif action == "clear":
            self.clear_history()
        else:
            print("Invalid history command. Use: history <show|save|load|clear>")

    def show_history(self):
        """Displays calculation history."""
        history = Calculations.get_history()
        if not history:
            print("📜 No history available.")
            return

        print("\n📜 Calculation History:")
        for i, calc in enumerate(history, start=1):
            print(f"{i}. {calc.a} {calc.operation.__name__} {calc.b} equal to {calc.perform()}")

    def save_history(self):
        """Saves history to a CSV file."""
        Calculations.save_history()
        print("✅ History saved successfully.")

    def load_history(self):
        """Loads history from a CSV file."""
        Calculations.load_history()
        print("✅ History loaded successfully.")

    def clear_history(self):
        """Clears the history."""
        Calculations.clear_history()
        print("🗑️ History cleared.")