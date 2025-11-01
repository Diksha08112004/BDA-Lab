import math

def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    return math.factorial(n)

def square_root(n):
    if n < 0:
        raise ValueError("Square root is not defined for negative numbers")
    return math.sqrt(n)

def power(base, exponent):
    return math.pow(base, exponent)
