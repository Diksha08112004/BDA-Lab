import math

def rectangle_area(length, width):
    return length * width

def rectangle_perimeter(length, width):
    return 2 * (length + width)

def triangle_area(base, height):
    return 0.5 * base * height

def triangle_perimeter(side1, side2, side3):
    return side1 + side2 + side3

def circle_area(radius):
    return math.pi * radius ** 2

def circle_circumference(radius):
    return 2 * math.pi * radius
