"""
mathpkg - A comprehensive math package with basic and advanced arithmetic operations.

This package provides two main modules:
- add_sub: Functions for addition and subtraction operations
- mul_div: Functions for multiplication, division, and other advanced operations
"""

from .add_sub import add, subtract, add_positive
from .mul_div import multiply, divide, safe_divide, power, factorial

__version__ = '1.1.0'
__all__ = [
    # From add_sub
    'add', 
    'subtract',
    'add_positive',
    
    # From mul_div
    'multiply', 
    'divide', 
    'safe_divide',
    'power',
    'factorial'
]
