import calc_utils as calc

# Test addition
print("5 + 3 =", calc.add(5, 3))

# Test subtraction
print("10 - 4 =", calc.subtract(10, 4))

# Test multiplication
print("6 * 7 =", calc.multiply(6, 7))

# Test division
try:
    print("15 / 3 =", calc.divide(15, 3))
    print("10 / 0 =", calc.divide(10, 0))
except ValueError as e:
    print("Error:", e)
