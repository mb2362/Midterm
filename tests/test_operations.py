''' Operations tests'''
from calculator.operations import add, subtract, multiply, divide

def test_addition():
    '''Test that addition function works '''    
    assert add(2, 2) == 4
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(-5, -5) == -10
    assert add(3.5, 2.5) == 6.0
    assert add(1e-10, 1e-10) == 2e-10  # Edge case for small numbers

def test_subtraction():
    '''Test that subtraction function works '''    
    assert subtract(2, 2) == 0
    assert subtract(5, 3) == 2
    assert subtract(0, 5) == -5
    assert subtract(-3, -7) == 4
    assert subtract(3.5, 1.5) == 2.0

def test_divide():
    '''Test that division function works '''    
    assert divide(2, 2) == 1
    assert divide(10, 2) == 5
    assert divide(5, 2) == 2.5
    assert divide(-10, 2) == -5
    assert divide(7, 0.5) == 14
    assert divide(1, 1e10) == 1e-10  # Edge case for very small results
    assert divide(1e308, 2) == 5e307  # Large number division check

def test_multiply():
    '''Test that multiply function works '''    
    assert multiply(2, 2) == 4
    assert multiply(-1, 5) == -5
    assert multiply(0, 100) == 0
    assert multiply(-3, -3) == 9
    assert multiply(2.5, 4) == 10.0
    assert multiply(1e-10, 1e10) == 1.0  # Edge case for floating-point precision

def test_edge_cases():
    '''Test edge cases for operations'''
    assert add(1e10, 1e10) == 2e10
    assert subtract(-1e10, 1e10) == -2e10
    assert multiply(1e5, 1e5) == 1e10
    assert divide(1, 3) == 1/3
    assert multiply(0, 1e10) == 0  # Zero multiplication check

def test_division_by_zero():
    '''Test that division by zero raises ZeroDivisionError'''
    try:
        divide(5, 0)
        assert False
    except ZeroDivisionError:
        assert True

def test_large_numbers():
    '''Test operations with large numbers'''
    assert add(1e308, 1e308) == float('inf')  # Overflow test
    assert multiply(1e155, 1e155) == float('inf')  # Overflow test (corrected value)
    assert divide(1e308, 1) == 1e308  # Large division check

def test_negative_large_numbers():
    '''Test operations with large negative numbers'''
    assert add(-1e308, -1e308) == -float('inf')  # Negative overflow test
    assert multiply(-1e155, 1e155) == -1e310  # Large negative multiplication check
    assert divide(-1e308, 1) == -1e308  # Large negative division check
