from geometrypkg.area import rectangle as area_rect, triangle as area_tri, circle as area_circle
from geometrypkg.perimeter import rectangle as peri_rect, triangle as peri_tri, circle as peri_circle

def main():
    # Rectangle calculations
    length, width = 5, 3
    print("=== Rectangle ===")
    print(f"Dimensions: {length} x {width}")
    print(f"Area: {area_rect(length, width)}")
    print(f"Perimeter: {peri_rect(length, width)}")
    
    # Triangle calculations
    base, height = 4, 6
    side1, side2, side3 = 3, 4, 5
    print("\n=== Triangle ===")
    print(f"Base: {base}, Height: {height}")
    print(f"Sides: {side1}, {side2}, {side3}")
    print(f"Area: {area_tri(base, height)}")
    print(f"Perimeter: {peri_tri(side1, side2, side3)}")
    
    # Circle calculations
    radius = 2.5
    print("\n=== Circle ===")
    print(f"Radius: {radius}")
    print(f"Area: {area_circle(radius):.2f}")
    print(f"Circumference: {peri_circle(radius):.2f}")
    
    # Real-world example
    print("\n=== Room Painting Example ===")
    room_length, room_width, room_height = 4, 5, 2.5  # meters
    wall_area = 2 * (room_length + room_width) * room_height  # Total wall area
    print(f"Room dimensions: {room_length}m x {room_width}m x {room_height}m")
    print(f"Total wall area to paint: {wall_area} square meters")
    paint_needed = wall_area / 10  # Assuming 1 liter covers 10 sq.m
    print(f"Paint needed: {paint_needed:.1f} liters")

if __name__ == "__main__":
    main()
