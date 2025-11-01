""
Area module for geometry package.
Provides functions to calculate areas of various shapes.
"""

def square(side):
    """Calculate area of a square."""
    return side * side

def rectangle(length, width):
    """Calculate area of a rectangle."""
    return length * width

def triangle(base, height):
    """Calculate area of a triangle."""
    return 0.5 * base * height

def circle(radius):
    """Calculate area of a circle."""
    return 3.14159 * radius * radius
