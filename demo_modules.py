# Importing our custom modules
import calc_utils as cu
import string_ops as so
import list_tools as lt
import math_ops as mo
import temperature as temp

def main():
    # Demo calc_utils
    print("=== Calculator Utils ===")
    print(f"5 + 3 = {cu.add(5, 3)}")
    print(f"10 - 4 = {cu.subtract(10, 4)}")
    print(f"6 * 7 = {cu.multiply(6, 7)}")
    print(f"15 / 3 = {cu.divide(15, 3)}")
    
    # Demo string_ops
    print("\n=== String Operations ===")
    test_str = "Hello, World!"
    print(f"Vowels in '{test_str}': {so.count_vowels(test_str)}")
    print(f"Reversed: '{so.reverse_string(test_str)}'")
    print(f"Is 'A man a plan a canal Panama' a palindrome? {so.is_palindrome('A man a plan a canal Panama')}")
    
    # Demo list_tools
    print("\n=== List Operations ===")
    numbers = [5, 2, 9, 1, 7, 3]
    print(f"List: {numbers}")
    print(f"Largest: {lt.find_largest(numbers)}")
    print(f"Smallest: {lt.find_smallest(numbers)}")
    print(f"Average: {lt.calculate_average(numbers):.2f}")
    
    # Demo math_ops
    print("\n=== Math Operations ===")
    print(f"Factorial of 5: {mo.factorial(5)}")
    print(f"Square root of 16: {mo.square_root(16)}")
    print(f"2 to the power of 5: {mo.power(2, 5)}")
    
    # Demo temperature
    print("\n=== Temperature Conversions ===")
    celsius = 25
    print(f"{celsius}°C = {temp.celsius_to_fahrenheit(celsius):.1f}°F")
    print(f"{celsius}°C = {temp.celsius_to_kelvin(celsius):.2f}K")

if __name__ == "__main__":
    main()
