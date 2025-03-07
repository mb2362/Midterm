# Operations
def add(a, b):
    """
    Add two numbers.

    Parameters:
    a (int or float): The first number.
    b (int or float): The second number.

    Returns:
    int or float: The sum of a and b.
    """
    return a + b


def subtract(a, b):
    """
    Subtract one number from another.

    Parameters:
    a (int or float): The number to subtract from.
    b (int or float): The number to subtract.

    Returns:
    int or float: The result of a - b.
    """
    return a - b


def divide(a, b):
    """
    Divide one number by another.

    Parameters:
    a (int or float): The numerator.
    b (int or float): The denominator.

    Returns:
    float: The result of a / b.

    Raises:
    ZeroDivisionError: If b is zero.
    """
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return a / b


def multiply(a, b):
    """
    Multiply two numbers.

    Parameters:
    a (int or float): The first number.
    b (int or float): The second number.

    Returns:
    int or float: The product of a and b.
    """
    return a * b