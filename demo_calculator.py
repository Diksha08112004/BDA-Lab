import calculator as calc

def main():
    print("=== Simple Calculator Demo ===\n")
    
    # Get user input
    print("Enter first number: ", end="")
    num1 = float(input())
    
    print("Enter operation (+, -, *, /): ", end="")
    operation = input().strip()
    
    print("Enter second number: ", end="")
    num2 = float(input())
    
    # Perform calculation
    result = None
    if operation == '+':
        result = calc.add(num1, num2)
    elif operation == '-':
        result = calc.subtract(num1, num2)
    elif operation == '*':
        result = calc.multiply(num1, num2)
    elif operation == '/':
        result = calc.divide(num1, num2)
    else:
        print("\nError: Invalid operation")
        return
    
    # Display result
    if result is not None:
        print(f"\n{num1} {operation} {num2} = {result}")
    else:
        print("\nError: Cannot divide by zero")

if __name__ == "__main__":
    main()
