import math_ops as mo

def main():
    # Test factorial
    print("=== Factorial ===")
    print(f"5! = {mo.factorial(5)}")
    
    # Test square root
    print("\n=== Square Root ===")
    print(f"√25 = {mo.square_root(25)}")
    
    # Test power
    print("\n=== Power ===")
    print(f"2^3 = {mo.power(2, 3)}")
    
    # Test error handling
    print("\n=== Error Handling ===")
    try:
        print("Factorial of -1:", mo.factorial(-1))
    except ValueError as e:
        print(f"Error: {e}")
    
    try:
        print("Square root of -9:", mo.square_root(-9))
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
