# Geometry Package Documentation

## Package Structure
```
geometrypkg/
├── __init__.py
├── area.py
└── perimeter.py
```

## 1. area.py
This module contains functions to calculate areas of different shapes.

### Functions:

#### 1. rectangle(length, width)
Calculates the area of a rectangle.
- **Parameters:**
  - `length` (float): Length of the rectangle
  - `width` (float): Width of the rectangle
- **Returns:**
  - float: Area of the rectangle

#### 2. triangle(base, height)
Calculates the area of a triangle.
- **Parameters:**
  - `base` (float): Base of the triangle
  - `height` (float): Height of the triangle
- **Returns:**
  - float: Area of the triangle

#### 3. circle(radius)
Calculates the area of a circle.
- **Parameters:**
  - `radius` (float): Radius of the circle
- **Returns:**
  - float: Area of the circle

## 2. perimeter.py
This module contains functions to calculate perimeters of different shapes.

### Functions:

#### 1. rectangle(length, width)
Calculates the perimeter of a rectangle.
- **Parameters:**
  - `length` (float): Length of the rectangle
  - `width` (float): Width of the rectangle
- **Returns:**
  - float: Perimeter of the rectangle

#### 2. triangle(side1, side2, side3)
Calculates the perimeter of a triangle.
- **Parameters:**
  - `side1` (float): Length of first side
  - `side2` (float): Length of second side
  - `side3` (float): Length of third side
- **Returns:**
  - float: Perimeter of the triangle

#### 3. circle(radius)
Calculates the circumference of a circle.
- **Parameters:**
  - `radius` (float): Radius of the circle
- **Returns:**
  - float: Circumference of the circle

## Example Usage

```python
# Import the package
from geometrypkg import area, perimeter

# Calculate areas
rect_area = area.rectangle(5, 3)
tri_area = area.triangle(4, 6)
circle_area = area.circle(2.5)

# Calculate perimeters
rect_peri = perimeter.rectangle(5, 3)
tri_peri = perimeter.triangle(3, 4, 5)
circle_circum = perimeter.circle(2.5)

print(f"Rectangle - Area: {rect_area}, Perimeter: {rect_peri}")
print(f"Triangle - Area: {tri_area}, Perimeter: {tri_peri}")
print(f"Circle - Area: {circle_area:.2f}, Circumference: {circle_circum:.2f}")
```

## Output
```
Rectangle - Area: 15, Perimeter: 16
Triangle - Area: 12.0, Perimeter: 12
Circle - Area: 19.63, Circumference: 15.71
```

## Error Handling
The functions include basic error handling for invalid inputs (e.g., negative values for dimensions).

## Dependencies
- Python 3.6+
- math module (included in Python standard library)
