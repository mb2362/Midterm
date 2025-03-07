"""
Operations Module.

This module contains the basic arithmetic operations (addition, subtraction, multiplication, and division).
Each operation is implemented as a function and performs the operation on two numbers.
"""

def add(a, b):
    """
    Add two numbers.

    Parameters:
    -----------
    a (int or float): The first number.
    b (int or float): The second number.

    Returns:
    --------
    int or float: The sum of a and b.

    Example:
    --------
    add(2, 3) -> 5
    """
    return a + b


def subtract(a, b):
    """
    Subtract one number from another.

    Parameters:
    -----------
    a (int or float): The number to subtract from.
    b (int or float): The number to subtract.

    Returns:
    --------
    int or float: The result of a - b.

    Example:
    --------
    subtract(5, 2) -> 3
    """
    return a - b


def divide(a, b):
    """
    Divide one number by another.

    Parameters:
    -----------
    a (int or float): The numerator.
    b (int or float): The denominator.

    Returns:
    --------
    float: The result of a / b.

    Raises:
    -------
    ZeroDivisionError: If b is zero.

    Example:
    --------
    divide(6, 2) -> 3.0
    divide(5, 0) -> Raises ZeroDivisionError
    """
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return a / b


def multiply(a, b):
    """
    Multiply two numbers.

    Parameters:
    -----------
    a (int or float): The first number.
    b (int or float): The second number.

    Returns:
    --------
    int or float: The product of a and b.

    Example:
    --------
    multiply(3, 4) -> 12
    """
    return a * b