import geometry as geo

def main():
    print("=== Geometry Package Demo ===\n")
    
    # Square calculations
    side = 5
    print(f"Square (side = {side}):")
    print(f"  Area: {geo.area.square(side)}")
    print(f"  Perimeter: {geo.perimeter.square(side)}")
    
    # Rectangle calculations
    length, width = 6, 4
    print(f"\nRectangle ({length}x{width}):")
    print(f"  Area: {geo.area.rectangle(length, width)}")
    print(f"  Perimeter: {geo.perimeter.rectangle(length, width)}")
    
    # Triangle calculations
    base, height = 3, 4
    side1, side2, side3 = 3, 4, 5
    print(f"\nTriangle (base={base}, height={height}):")
    print(f"  Area: {geo.area.triangle(base, height)}")
    print(f"  Perimeter: {geo.perimeter.triangle(side1, side2, side3)}")
    
    # Circle calculations
    radius = 7
    print(f"\nCircle (radius = {radius}):")
    print(f"  Area: {geo.area.circle(radius):.2f}")
    print(f"  Circumference: {geo.perimeter.circle(radius):.2f}")

if __name__ == "__main__":
    main()
