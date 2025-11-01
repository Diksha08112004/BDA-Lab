""
Basic arithmetic operations for the calculator package.
"""

def add(a, b):
    """Return the sum of two numbers."""
    return a + b

def subtract(a, b):
    """Return the difference between two numbers."""
    return a - b

def multiply(a, b):
    """Return the product of two numbers."""
    return a * b

def divide(a, b):
    """
    Return the quotient of two numbers.
    Returns None if dividing by zero.
    """
    if b == 0:
        return None
    return a / b
