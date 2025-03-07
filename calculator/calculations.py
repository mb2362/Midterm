"""
Calculations Module.

This module defines the `Calculations` class, which manages a history of arithmetic
calculations, allowing users to add, retrieve, clear, and filter calculations based on the operation.
"""

# Importing Decimal for precise floating-point arithmetic to avoid rounding errors.
from decimal import Decimal  

# Importing Callable for function type hinting and List for handling history storage.
from typing import Callable, List  

# Importing the Calculation class to manage individual arithmetic operations.
from calculator.calculation import Calculation  

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

    @classmethod
    def get_history(cls) -> List[Calculation]:
        """
        Retrieve the entire history of calculations.

        Returns:
        --------
        List[Calculation]: A list of all Calculation instances stored in history.
        """
        return cls.history  # Return the full history list

    @classmethod
    def clear_history(cls):
        """
        Clear the history of calculations.

        This removes all stored Calculation instances, resetting the history.
        """
        cls.history.clear()  # Clear the entire history list

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
            return cls.history[-1]  # Return the last calculation in the history
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
        return [calc for calc in cls.history if calc.operation.__name__ == operation_name]
        # Return a list of calculations where the operation matches the specified name