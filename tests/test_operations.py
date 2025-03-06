''' Operations tests'''
from calculator.operations import add, subtract, multiply, divide

def test_addition():
    '''Test that the addition function correctly adds two numbers.'''
    assert add(2, 2) == 4  # Testing positive integers
    assert add(-1, 1) == 0  # Testing addition of a negative and positive number
    assert add(0, 0) == 0  # Testing addition of zeros
    assert add(-5, -5) == -10  # Testing addition of negative numbers
    assert add(3.5, 2.5) == 6.0  # Testing addition with floating-point numbers
    assert add(1e-10, 1e-10) == 2e-10  # Edge case for small numbers

def test_subtraction():
    '''Test that the subtraction function correctly subtracts two numbers.'''
    assert subtract(2, 2) == 0  # Testing subtraction of equal numbers
    assert subtract(5, 3) == 2  # Testing positive integers
    assert subtract(0, 5) == -5  # Testing subtraction with a negative result
    assert subtract(-3, -7) == 4  # Testing subtraction with negative numbers
    assert subtract(3.5, 1.5) == 2.0  # Testing subtraction with floating-point numbers

def test_divide():
    '''Test that the division function correctly divides two numbers.'''
    assert divide(2, 2) == 1  # Testing basic division
    assert divide(10, 2) == 5  # Testing division of integers
    assert divide(5, 2) == 2.5  # Testing division resulting in floating-point numbers
    assert divide(-10, 2) == -5  # Testing division with negative numbers
    assert divide(7, 0.5) == 14  # Testing division with fractional divisor
    assert divide(1, 1e10) == 1e-10  # Edge case for very small results
    assert divide(1e308, 2) == 5e307  # Large number division check

def test_multiply():
    '''Test that the multiplication function correctly multiplies two numbers.'''
    assert multiply(2, 2) == 4  # Basic multiplication
    assert multiply(-1, 5) == -5  # Testing multiplication with negative numbers
    assert multiply(0, 100) == 0  # Multiplication with zero
    assert multiply(-3, -3) == 9  # Multiplying negative numbers
    assert multiply(2.5, 4) == 10.0  # Testing with floating-point numbers
    assert multiply(1e-10, 1e10) == 1.0  # Edge case for floating-point precision

def test_edge_cases():
    '''Test edge cases for arithmetic operations.'''
    assert add(1e10, 1e10) == 2e10  # Adding large numbers
    assert subtract(-1e10, 1e10) == -2e10  # Subtraction with large values
    assert multiply(1e5, 1e5) == 1e10  # Multiplying large values
    assert divide(1, 3) == 1/3  # Dividing by 3 to check precision
    assert multiply(0, 1e10) == 0  # Zero multiplication check

def test_division_by_zero():
    '''Test that division by zero raises a ZeroDivisionError.'''
    try:
        divide(5, 0)
        assert False  # If no error is raised, fail the test
    except ZeroDivisionError:
        assert True  # Expecting ZeroDivisionError to be raised

def test_large_numbers():
    '''Test operations with very large numbers.'''
    assert add(1e308, 1e308) == float('inf')  # Overflow test for addition
    assert multiply(1e155, 1e155) == float('inf')  # Overflow test for multiplication
    assert divide(1e308, 1) == 1e308  # Large number division check

def test_negative_large_numbers():
    '''Test operations with very large negative numbers.'''
    assert add(-1e308, -1e308) == -float('inf')  # Negative overflow for addition
    assert multiply(-1e155, 1e155) == -1e310  # Large negative multiplication check
    assert divide(-1e308, 1) == -1e308  # Large negative division check
