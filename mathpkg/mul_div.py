"""
mul_div module for mathpkg
Provides multiplication and division functions.
"""

def multiply(*args):
    """
    Multiply any number of values together.
    
    Args:
        *args: Variable number of numeric values to multiply
        
    Returns:
        The product of all input values. Returns 1 if no arguments are provided.
        
    Example:
        >>> multiply(2, 3, 4)
        24
        >>> multiply()
        1
    """
    if not args:
        return 1
    
    result = 1
    for num in args:
        result *= num
    return result

def divide(a, b):
    """
    Divide a by b.
    
    Args:
        a: The dividend
        b: The divisor (must not be zero)
        
    Returns:
        The quotient of a divided by b
        
    Raises:
        ZeroDivisionError: If b is zero
        
    Example:
        >>> divide(10, 2)
        5.0
    """
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b

def safe_divide(a, b):
    """
    Safely divide a by b, returning None if dividing by zero.
    
    Args:
        a: The dividend
        b: The divisor
        
    Returns:
        The quotient of a divided by b, or None if b is zero
        
    Example:
        >>> safe_divide(10, 2)
        5.0
        >>> safe_divide(10, 0) is None
        True
    """
    try:
        return divide(a, b)
    except ZeroDivisionError:
        return None

def power(base, exponent):
    """
    Calculate base raised to the power of exponent.
    
    Args:
        base: The base number
        exponent: The exponent
        
    Returns:
        base raised to the power of exponent
        
    Example:
        >>> power(2, 3)
        8
        >>> power(4, 0.5)
        2.0
    """
    return base ** exponent

def factorial(n):
    """
    Calculate the factorial of a non-negative integer.
    
    Args:
        n: A non-negative integer
        
    Returns:
        The factorial of n (n!)
        
    Raises:
        ValueError: If n is negative
        
    Example:
        >>> factorial(5)
        120
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("n must be a non-negative integer")
    return 1 if n == 0 else n * factorial(n - 1)
