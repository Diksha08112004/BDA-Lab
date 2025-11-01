""
Demo of Python's built-in math module
Focusing on factorial, power, and square root functions
"""

import math

def main():
    # Factorial demonstration
    print("=== Factorial ===")
    numbers = [0, 1, 5, 7, 10]
    for num in numbers:
        print(f"{num}! = {math.factorial(num)}")
    
    # Power demonstration
    print("\n=== Power (x^y) ===")
    base = 2
    exponents = [0, 1, 3, 5]
    for exp in exponents:
        print(f"{base}^{exp} = {math.pow(base, exp):.0f}")
    
    # Square root demonstration
    print("\n=== Square Root ===")
    values = [0, 1, 4, 9, 16, 25, 2, 3.5]
    for val in values:
        print(f"√{val} = {math.sqrt(val):.3f}")
    
    # Combined example
    print("\n=== Combined Example ===")
    x = 5
    result = math.sqrt(math.factorial(x) + math.pow(x, 3))
    print(f"√({x}! + {x}³) = {result:.2f}")

if __name__ == "__main__":
    main()
