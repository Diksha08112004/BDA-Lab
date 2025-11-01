""
Perimeter module for geometry package.
Provides functions to calculate perimeters of various shapes.
"""

def square(side):
    """Calculate perimeter of a square."""
    return 4 * side

def rectangle(length, width):
    """Calculate perimeter of a rectangle."""
    return 2 * (length + width)

def triangle(side1, side2, side3):
    """Calculate perimeter of a triangle."""
    return side1 + side2 + side3

def circle(radius):
    """Calculate circumference of a circle."""
    return 2 * 3.14159 * radius
