'''My Calculator Test'''
from calculator import Calculator

def test_addition():
    '''Test that the addition function correctly adds two numbers.'''
    # Testing addition of two positive numbers (2 + 2)
    assert Calculator.add(2, 2) == 4  # The expected result is 4

def test_subtraction():
    '''Test that the subtraction function correctly subtracts two numbers.'''
    # Testing subtraction of two equal numbers (2 - 2)
    assert Calculator.subtract(2, 2) == 0  # The expected result is 0

def test_multiply():
    '''Test that the multiplication function correctly multiplies two numbers.'''
    # Testing multiplication of two positive numbers (2 * 2)
    assert Calculator.multiply(2, 2) == 4  # The expected result is 4

def test_divide():
    '''Test that the division function correctly divides two numbers.'''
    # Testing division of two equal numbers (2 / 2)
    assert Calculator.divide(2, 2) == 1  # The expected result is 1
