import converter as cv

def main():
    print("=== Length Conversions ===")
    # Centimeters to Meters
    cm = 150
    print(f"{cm} cm = {cv.cm_to_m(cm)} meters")
    
    # Meters to Centimeters
    meters = 1.75
    print(f"{meters} meters = {cv.m_to_cm(meters)} cm")
    
    # Kilometers to Miles
    km = 10
    print(f"{km} km = {cv.km_to_miles(km):.2f} miles")
    
    # Miles to Kilometers
    miles = 6.21
    print(f"{miles} miles = {cv.miles_to_km(miles):.2f} km")
    
    print("\n=== Weight Conversions ===")
    # Kilograms to Grams
    kg = 2.5
    print(f"{kg} kg = {cv.kg_to_g(kg)} grams")
    
    # Grams to Kilograms
    grams = 3500
    print(f"{grams} grams = {cv.g_to_kg(grams)} kg")
    
    # Real-world examples
    print("\n=== Real-world Examples ===")
    
    # Example 1: Height conversion
    print("\nExample 1: Height Conversion")
    height_cm = 175
    print(f"A person's height is {height_cm} cm, which is {cv.cm_to_m(height_cm)} meters")
    
    # Example 2: Weight conversion for cooking
    print("\nExample 2: Cooking Measurement")
    flour_kg = 0.5
    print(f"Recipe requires {flour_kg} kg of flour, which is {cv.kg_to_g(flour_kg)} grams")
    
    # Example 3: Distance conversion for travel
    print("\nExample 3: Travel Distance")
    distance_km = 100
    print(f"The next city is {distance_km} km away, which is approximately {cv.km_to_miles(distance_km):.1f} miles")
    
    # Conversion table
    print("\n=== Conversion Table ===")
    print("Centimeters | Meters    | Kilometers | Miles")
    print("-" * 50)
    for cm in [50, 100, 150, 200, 250]:
        m = cv.cm_to_m(cm)
        km = m / 1000
        miles = cv.km_to_miles(km)
        print(f"{cm:^10} | {m:^9.2f} | {km:^10.3f} | {miles:.4f}")

if __name__ == "__main__":
    main()
