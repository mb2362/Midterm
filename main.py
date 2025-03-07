"""
Main script for running the calculator application.

This script parses command-line arguments, performs calculations using the Calculator class,
and handles exceptions gracefully.
"""

# Import required modules
import sys  # Import sys for command-line argument handling
from app import App  # Import App class for starting the application
from calculator import Calculator  # Import Calculator class for arithmetic operations
from calculator.calculation import Calculation  # Import Calculation class for managing individual calculations

def parse_args(args):
    """
    Parses command-line arguments.

    Expected arguments:
    - a (str): The first operand (should be a valid number).
    - b (str): The second operand (should be a valid number).
    - operation (str): The arithmetic operation (add, subtract, multiply, divide).

    Parameters:
    -----------
    args (list): List of command-line arguments excluding the script name.

    Returns:
    --------
    tuple: (a, b, operation) where a and b are converted to floats.

    Raises:
    -------
    ValueError: If arguments are missing or invalid.
    """
    if len(args) != 3:
        raise ValueError("Please provide exactly three arguments: a, b, and operation.")

    a_str, b_str, operation = args

    try:
        a = float(a_str)  # Convert first argument to float
        b = float(b_str)  # Convert second argument to float
    except ValueError:
        raise ValueError(f"Invalid number input: {a_str} or {b_str} is not a valid number.")
    
    return a, b, operation

def perform_operation(a, b, operation):
    """
    Performs the specified arithmetic operation.

    Parameters:
    -----------
    a (float): The first operand.
    b (float): The second operand.
    operation (str): The operation to perform (add, subtract, multiply, divide).

    Returns:
    --------
    float: The result of the arithmetic operation.

    Raises:
    -------
    ValueError: If an unknown operation is provided.
    ZeroDivisionError: If attempting to divide by zero.
    """
    if operation == 'add':
        return Calculator.add(a, b)
    elif operation == 'subtract':
        return Calculator.subtract(a, b)
    elif operation == 'multiply':
        return Calculator.multiply(a, b)
    elif operation == 'divide':
        try:
            return Calculator.divide(a, b)
        except ZeroDivisionError:
            raise ZeroDivisionError("Cannot divide by zero.")
    else:
        raise ValueError(f"Unknown operation: {operation}")

def main():
    """
    Main function to handle command-line execution.

    It parses arguments, performs calculations, and displays the result.
    Handles errors gracefully to provide user-friendly messages.
    """
    try:
        # Exclude the script name and parse arguments
        a, b, operation = parse_args(sys.argv[1:])
        result = perform_operation(a, b, operation)
        print(f"The result of {int(a)} {operation} {int(b)} is equal to {result}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    """
    Entry point of the program.

    If executed directly, it starts the App instance and runs the command-line calculator.
    """
    app = App()
    app.start()