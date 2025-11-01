import mathpkg as mp
from mathpkg.add_sub import add, subtract
from mathpkg.mul_div import multiply, divide, safe_divide

def main():
    print("=== Math Package Demo ===\n")
    
    # Basic arithmetic operations
    print("1. Basic Arithmetic:")
    a, b = 10, 3
    print(f"   {a} + {b} = {mp.add(a, b)}")
    print(f"   {a} - {b} = {mp.subtract(a, b)}")
    print(f"   {a} * {b} = {mp.multiply(a, b)}")
    print(f"   {a} / {b} = {mp.divide(a, b):.2f}")
    
    # Safe division
    print("\n2. Safe Division:")
    try:
        print(f"   {a} / 0 = {divide(a, 0):.2f}")
    except ZeroDivisionError:
        print(f"   {a} / 0 = Error: Division by zero")
    
    print(f"   {a} / 0 (safe) = {safe_divide(a, 0)}")
    
    # Multiple arguments
    print("\n3. Multiple Arguments:")
    numbers = [1, 2, 3, 4, 5]
    print(f"   Sum of {numbers} = {add(*numbers)}")
    print(f"   Product of {numbers} = {multiply(*numbers)}")
    
    # Using add_positive function
    print("\n4. Add Positive Numbers:")
    print(f"   5 + 3 = {mp.add_positive(5, 3)}")
    print(f"   -2 + 4 = {mp.add_positive(-2, 4)}")
    
    # Using safe_divide with different inputs
    print("\n5. Safe Divide Examples:")
    print(f"   10 / 2 = {safe_divide(10, 2)}")
    print(f"   10 / 0 = {safe_divide(10, 0)}")
    print(f"   -5 / 2 = {safe_divide(-5, 2)}")
    
    # Using the package's __all__ imports
    print("\n6. Using functions from package's __all__:")
    result = mp.add(100, mp.multiply(5, 20))
    print(f"   100 + (5 * 20) = {result}")
    
    # Nested operations
    print("\n7. Nested Operations:")
    expr = "(10 + 5) * (20 - 8) / 4"
    result = mp.multiply(mp.add(10, 5), mp.divide(mp.subtract(20, 8), 4))
    print(f"   {expr} = {result}")
    
    # Edge cases
    print("\n8. Edge Cases:")
    print(f"   Adding no numbers: {mp.add()}")
    print(f"   Multiplying no numbers: {mp.multiply()}")
    print(f"   Safe divide by zero: {mp.safe_divide(5, 0)}")
    print(f"   Safe divide zero by number: {mp.safe_divide(0, 5)}")

if __name__ == "__main__":
    main()
