# Import system for capturing inputs
import sys

# Import logging for logs
import logging

# Import App to start the app
from app import App

# Import Calculator to perform arithmetic operations
from calculator import Calculator

# Importing the Calculation class to manage individual arithmetic operations.
from calculator.calculation import Calculation

# Configure logger
logger = logging.getLogger(__name__)

def parse_args(args):
    """
    Parses the command-line arguments.
    
    Expected arguments: a, b, operation
    - a: first operand (float)
    - b: second operand (float)
    - operation: a string specifying the arithmetic operation (add, subtract, multiply, divide)
    
    Returns:
        tuple: (a, b, operation) where a and b are floats if valid.
    
    Raises:
        ValueError: If the arguments are not in the correct format or are invalid.
    """
    if len(args) != 3:
        raise ValueError("Please provide exactly three arguments: a, b, and operation.")

    a_str, b_str, operation = args

    try:
        # Convert operands to float
        a = float(a_str)
        b = float(b_str)
    except ValueError:
        raise ValueError(f"Invalid number input: {a_str} or {b_str} is not a valid number.")
    
    return a, b, operation

def perform_operation(a, b, operation):
    """
    Maps the operation string to the corresponding Calculator method.
    
    Args:
        a (float): First operand.
        b (float): Second operand.
        operation (str): Arithmetic operation (add, subtract, multiply, divide).
    
    Returns:
        float: The result of the operation.
    
    Raises:
        ValueError: If the operation is unknown.
        ZeroDivisionError: If attempting division by zero.
    """
    logger.debug(f"Performing operation: {a} {operation} {b}")
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
            # Log error for division by zero and raise exception
            logger.error(f"Attempted to divide {a} by {b}. Division by zero is not allowed.")
            raise ZeroDivisionError("Cannot divide by zero.")
    else:
        # Log error for unknown operation and raise exception
        logger.error(f"Unknown operation: {operation}")
        raise ValueError(f"Unknown operation: {operation}")

def main():
    """
    Main function to parse the command-line arguments and perform the operation.
    
    - Parses arguments using parse_args.
    - Performs the operation using perform_operation.
    - Logs and prints the result or error message.
    """
    try:
        # Exclude the script name and parse the arguments from the command line
        a, b, operation = parse_args(sys.argv[1:])
        
        # Perform the operation and log the result
        result = perform_operation(a, b, operation)
        
        # Log the result and print to the console
        logger.info(f"Calculation result: The result of {int(a)} {operation} {int(b)} is equal to {result}")
        print(f"The result of {int(a)} {operation} {int(b)} is equal to {result}")
    
    except Exception as e:
        # Log any error that occurs and print the error message
        logger.error(f"An error occurred: {e}")
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    """
    Entry point for the application.
    Initializes and starts the CLI application using App.
    """
    app = App()
    app.start()