"""
Calculations Module.

This module defines the `Calculations` class, which manages a history of arithmetic
calculations, allowing users to add, retrieve, clear, and filter calculations based on the operation.
"""

# Import logging
import logging

import pandas as pd

# Importing Decimal for precise floating-point arithmetic to avoid rounding errors.
from decimal import Decimal  

# Importing Callable for function type hinting and List for handling history storage.
from typing import Callable, List  

# Importing the Calculation class to manage individual arithmetic operations.
from calculator.operations import add, subtract, multiply, divide  
from calculator.calculation import Calculation  

# Configure logger
logger = logging.getLogger(__name__)

from app import App

HISTORY_FILE = App().get_environment_variable('HISTORY_FILE')

class Calculations:
    """
    A class to manage a history of calculations.

    This class maintains a history of performed calculations, allows adding new
    calculations, retrieving history, clearing history, and filtering calculations
    based on the operation type.

    Attributes:
    -----------
    history : List[Calculation]
        A class-level list that stores past Calculation instances.
    """

    # Initialize the history list to store performed calculations
    history: List[Calculation] = []  # Stores all performed calculations

    @classmethod
    def add_calculation(cls, calculation: Calculation):
        """
        Add a new calculation to the history.

        Parameters:
        -----------
        calculation (Calculation): The calculation instance to be stored in history.
        """
        cls.history.append(calculation)  # Add the calculation to the history list
        logger.debug(f"Added calculation: {calculation}")

    @classmethod
    def get_history(cls) -> List[Calculation]:
        """
        Retrieve the entire history of calculations.

        Returns:
        --------
        List[Calculation]: A list of all Calculation instances stored in history.
        """
        logger.debug(f"Retrieving full history. Total calculations: {len(cls.history)}")
        return cls.history  # Return the full history list

    @classmethod
    def clear_history(cls):
        """
        Clear the history of calculations.

        This removes all stored Calculation instances, resetting the history.
        """
        cls.history.clear()  # Clear the entire history list
        df = pd.DataFrame(columns=["Operand1", "Operand2", "Operation", "Result"])
        df.to_csv(HISTORY_FILE, index=False)
        logger.debug("Cleared the calculation history.")
        print("History cleared.")

    @classmethod
    def get_latest(cls) -> Calculation:
        """
        Get the latest calculation from history.

        Returns:
        --------
        Calculation: The most recent calculation from history.
        None: If there is no calculation in history.
        """
        if cls.history:
            logger.debug(f"Latest calculation: {cls.history[-1]}")
            return cls.history[-1]  # Return the last calculation in the history
        logger.debug("No calculations found in history.")
        return None  # Return None if the history is empty

    @classmethod
    def find_by_operation(cls, operation_name: str) -> List[Calculation]:
        """
        Find and return a list of calculations by operation name.

        Parameters:
        -----------
        operation_name (str): The name of the operation function (e.g., 'add', 'subtract').

        Returns:
        --------
        List[Calculation]: A list of calculations that match the given operation name.
        """
        matching_calculations = [calc for calc in cls.history if calc.operation.__name__ == operation_name]
        logger.debug(f"Found {len(matching_calculations)} calculations for operation: {operation_name}")
        return matching_calculations
    
    @classmethod
    def save_history(cls):
        """Save the calculation history to a CSV file."""
        if cls.history:
            data = [{
                "Operand1": calc.a,
                "Operand2": calc.b,
                "Operation": calc.operation.__name__,  # Save operation name as string
                "Result": calc.perform()
            } for calc in cls.history]

            df = pd.DataFrame(data)
            df.to_csv(HISTORY_FILE, index=False)
            print("History saved.")

    @classmethod
    def load_history(cls):
        """Load calculation history from a CSV file."""
        try:
            df = pd.read_csv(HISTORY_FILE)
            
            # Clear the current history before loading from the file
            cls.history.clear()

            # Iterate over each row in the dataframe
            for _, row in df.iterrows():
                # Fetch operands and operation from CSV
                operand1 = Decimal(row["Operand1"])
                operand2 = Decimal(row["Operand2"])
                operation_name = row["Operation"]

                # Map operation name to the corresponding operation function
                if operation_name == "add":
                    operation = add
                elif operation_name == "subtract":
                    operation = subtract
                elif operation_name == "multiply":
                    operation = multiply
                elif operation_name == "divide":
                    operation = divide
                else:
                    logger.warning(f"Unknown operation '{operation_name}' in history file.")
                    continue  # Skip if the operation is not recognized

                # Create the Calculation instance and add it to the history
                calculation = Calculation(operand1, operand2, operation)
                cls.history.append(calculation)

            print("History loaded successfully.")
            logger.info(f"History loaded. Total calculations: {len(cls.history)}")

        except FileNotFoundError:
            print("No history file found.")
            logger.warning("History file not found.")
        except Exception as e:
            print(f"Error loading history: {e}")
            logger.error(f"Error loading history: {e}")