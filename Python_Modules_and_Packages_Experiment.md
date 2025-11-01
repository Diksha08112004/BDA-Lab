# Python Modules and Packages Experiment

## User-Defined Modules

### 1. Calculator Utilities
**Question:** Create a module `calc_utils.py` with functions for addition, subtraction, multiplication, and division. Import and use it in another file.

**Program:**
```python
# calc_utils.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

# demo_calc.py
import calc_utils as cu

print("5 + 3 =", cu.add(5, 3))
print("10 - 4 =", cu.subtract(10, 4))
print("6 * 7 =", cu.multiply(6, 7))
print("15 / 3 =", cu.divide(15, 3))
```

**Output:**
```
5 + 3 = 8
10 - 4 = 6
6 * 7 = 42
15 / 3 = 5.0
```

### 2. String Operations
**Question:** Develop a module `string_ops.py` with functions to count vowels, reverse strings, and check for palindromes.

**Program:**
```python
# string_ops.py
def count_vowels(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)

def reverse_string(s):
    return s[::-1]

def is_palindrome(s):
    s = ''.join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]

# demo_string.py
import string_ops as so

text = "A man, a plan, a canal: Panama"
print(f"Vowels in '{text}': {so.count_vowels(text)}")
print(f"Reversed: '{so.reverse_string(text)}'")
print(f"Is palindrome? {so.is_palindrome(text)}")
```

**Output:**
```
Vowels in 'A man, a plan, a canal: Panama': 12
Reversed: '!amanaP :lanac a ,nalp a ,nam A'
Is palindrome? True
```

### 3. List Tools
**Question:** Create a module `list_tools.py` to find the largest, smallest, and average of list elements.

**Program:**
```python
# list_tools.py
def find_largest(numbers):
    if not numbers:
        return None
    return max(numbers)

def find_smallest(numbers):
    if not numbers:
        return None
    return min(numbers)

def calculate_average(numbers):
    if not numbers:
        return None
    return sum(numbers) / len(numbers)

# demo_list.py
import list_tools as lt

numbers = [5, 2, 9, 1, 7, 3]
print(f"List: {numbers}")
print(f"Largest: {lt.find_largest(numbers)}")
print(f"Smallest: {lt.find_smallest(numbers)}")
print(f"Average: {lt.calculate_average(numbers):.2f}")
```

**Output:**
```
List: [5, 2, 9, 1, 7, 3]
Largest: 9
Smallest: 1
Average: 4.50
```

## Packages

### 1. Geometry Package
**Question:** Design a package `geometry` with modules `area.py` and `perimeter.py` for basic shapes.

**Program:**
```python
# geometrypkg/__init__.py
# Initialize geometry package

# geometrypkg/area.py
import math

def rectangle(length, width):
    return length * width

def triangle(base, height):
    return 0.5 * base * height

def circle(radius):
    return math.pi * radius ** 2

# geometrypkg/perimeter.py
import math

def rectangle(length, width):
    return 2 * (length + width)

def triangle(side1, side2, side3):
    return side1 + side2 + side3

def circle(radius):
    return 2 * math.pi * radius

# demo_geometry.py
from geometrypkg.area import rectangle as area_rect, circle as area_circle
from geometrypkg.perimeter import rectangle as peri_rect

print(f"Area of rectangle (4x5): {area_rect(4, 5)}")
print(f"Perimeter of rectangle (4x5): {peri_rect(4, 5)}")
print(f"Area of circle (r=3): {area_circle(3):.2f}")
```

**Output:**
```
Area of rectangle (4x5): 20
Perimeter of rectangle (4x5): 18
Area of circle (r=3): 28.27
```

### 2. Student Package
**Question:** Build a package `student` with modules `marks.py` (total, percentage) and `grade.py` (grade evaluation).

**Program:**
```python
# studentpkg/__init__.py
# Initialize student package

# studentpkg/marks.py
def calculate_total(marks):
    return sum(marks)

def calculate_percentage(marks, total_marks):
    return (sum(marks) / total_marks) * 100

# studentpkg/grade.py
def calculate_grade(percentage):
    if percentage >= 90:
        return 'A+'
    elif percentage >= 80:
        return 'A'
    elif percentage >= 70:
        return 'B'
    elif percentage >= 60:
        return 'C'
    elif percentage >= 50:
        return 'D'
    else:
        return 'F'

# demo_student.py
from studentpkg.marks import calculate_total, calculate_percentage
from studentpkg.grade import calculate_grade

marks = [85, 92, 78, 90, 88]
total_marks = 500

total = calculate_total(marks)
percentage = calculate_percentage(marks, total_marks)
grade = calculate_grade(percentage)

print(f"Marks: {marks}")
print(f"Total: {total}/{total_marks}")
print(f"Percentage: {percentage:.2f}%")
print(f"Grade: {grade}")
```

**Output:**
```
Marks: [85, 92, 78, 90, 88]
Total: 433/500
Percentage: 86.60%
Grade: A
```

## Built-in Python Modules

### 1. Math Module
**Question:** Use the `math` module to calculate factorial, power, and square root.

**Program:**
```python
import math

# Calculate factorial
fact_5 = math.factorial(5)

# Calculate power
power = math.pow(2, 5)

# Calculate square root
sqrt_16 = math.sqrt(16)

print(f"Factorial of 5: {fact_5}")
print(f"2 to the power of 5: {power}")
print(f"Square root of 16: {sqrt_16}")
```

**Output:**
```
Factorial of 5: 120
2 to the power of 5: 32.0
Square root of 16: 4.0
```

### 2. Datetime Module
**Question:** Use the `datetime` module to display current date and time and calculate a person's age.

**Program:**
```python
from datetime import datetime, date

# Current date and time
now = datetime.now()
print(f"Current date and time: {now}")

# Calculate age
def calculate_age(birth_date):
    today = date.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

birth_date = date(1995, 5, 15)
age = calculate_age(birth_date)
print(f"Age for someone born on {birth_date}: {age} years")
```

**Output:**
```
Current date and time: [current date and time]
Age for someone born on 1995-05-15: [calculated age] years
```

### 3. Random Module
**Question:** Use the `random` module to generate random integers and simulate rolling two dice.

**Program:**
```python
import random

# Generate random number between 1 and 100
random_number = random.randint(1, 100)
print(f"Random number between 1-100: {random_number}")

# Simulate rolling two dice
die1 = random.randint(1, 6)
die2 = random.randint(1, 6)
print(f"Dice roll: {die1} and {die2}")
print(f"Total: {die1 + die2}")
```

**Output:**
```
Random number between 1-100: [random number between 1-100]
Dice roll: [1-6] and [1-6]
Total: [sum of two dice]
```

## Conclusion

This document demonstrates the creation and usage of various Python modules and packages, along with examples of built-in modules. Each section includes the problem statement, the solution code, and the expected output. The examples cover a wide range of functionality from basic arithmetic operations to more complex data manipulations using Python's module system.
