import temperature as temp

def main():
    # Test Celsius to Fahrenheit
    celsius = 25
    fahrenheit = temp.celsius_to_fahrenheit(celsius)
    print(f"{celsius}°C = {fahrenheit:.2f}°F")
    
    # Test Fahrenheit to Celsius
    fahrenheit = 77
    celsius = temp.fahrenheit_to_celsius(fahrenheit)
    print(f"{fahrenheit}°F = {celsius:.2f}°C")
    
    # Test Celsius to Kelvin
    celsius = 0
    kelvin = temp.celsius_to_kelvin(celsius)
    print(f"{celsius}°C = {kelvin:.2f}K")
    
    # Test Kelvin to Celsius
    kelvin = 273.15
    celsius = temp.kelvin_to_celsius(kelvin)
    print(f"{kelvin}K = {celsius:.2f}°C")
    
    # Test Fahrenheit to Kelvin
    fahrenheit = 32
    kelvin = temp.fahrenheit_to_kelvin(fahrenheit)
    print(f"{fahrenheit}°F = {kelvin:.2f}K")
    
    # Test Kelvin to Fahrenheit
    kelvin = 373.15
    fahrenheit = temp.kelvin_to_fahrenheit(kelvin)
    print(f"{kelvin}K = {fahrenheit:.2f}°F")
    
    # Test all conversions in a chain
    print("\nConversion chain test:")
    celsius = 100
    print(f"Original: {celsius}°C")
    f = temp.celsius_to_fahrenheit(celsius)
    print(f"To Fahrenheit: {f:.2f}°F")
    k = temp.fahrenheit_to_kelvin(f)
    print(f"To Kelvin: {k:.2f}K")
    c = temp.kelvin_to_celsius(k)
    print(f"Back to Celsius: {c:.2f}°C")

if __name__ == "__main__":
    main()
