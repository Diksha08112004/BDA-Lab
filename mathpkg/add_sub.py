""
add_sub module for mathpkg
Provides addition and subtraction functions.
"""

def add(*args):
    """
    Add any number of values together.
    
    Args:
        *args: Variable number of numeric values to add
        
    Returns:
        The sum of all input values
        
    Example:
        >>> add(1, 2, 3, 4)
        10
    """
    return sum(args)

def subtract(a, b):
    """
    Subtract b from a.
    
    Args:
        a: The minuend
        b: The subtrahend
        
    Returns:
        The difference between a and b
        
    Example:
        >>> subtract(10, 3)
        7
    """
    return a - b

def add_positive(a, b):
    """
    Add two numbers, but return 0 if either is negative.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        Sum of a and b if both are positive, else 0
        
    Example:
        >>> add_positive(5, 3)
        8
        >>> add_positive(-2, 4)
        0
    """
    return a + b if a >= 0 and b >= 0 else 0
