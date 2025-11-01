# Demo script showing usage of all modules and packages
import calc_utils as cu
import string_ops as so
import list_tools as lt
import math_ops as mo
import temperature as temp
import finance as fin
import geometry as geo
import marks_utils as mu
import converter as conv
import date_ops as do
import string_compare as sc
import number_utils as nu
import file_tools as ft
import matrix_utils as mat
from student_info import Student

# Import from packages
from geometrypkg.area import *
from geometrypkg.perimeter import *
from studentpkg.marks import *
from studentpkg.grade import *

def main():
    print("=== Calculator Utils ===")
    print(f"5 + 3 = {cu.add(5, 3)}")
    print(f"10 - 4 = {cu.subtract(10, 4)}")
    
    print("\n=== String Operations ===")
    test_str = "Hello, World!"
    print(f"Vowels in '{test_str}': {so.count_vowels(test_str)}")
    print(f"Is 'madam' a palindrome? {so.is_palindrome('madam')}")
    
    print("\n=== Number Utils ===")
    print(f"Is 7 prime? {nu.is_prime(7)}")
    print(f"Is 28 a perfect number? {nu.is_perfect(28)}")
    
    print("\n=== Geometry Package ===")
    print(f"Area of circle (r=5): {circle(5):.2f}")
    print(f"Perimeter of rectangle (4x5): {rectangle(4, 5)}")
    
    print("\n=== Student Package ===")
    marks = [85, 90, 78, 92, 88]
    total = calculate_total(marks)
    percentage = calculate_percentage(marks, 500)
    print(f"Total marks: {total}")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade: {calculate_grade(percentage)}")
    
    print("\n=== Temperature Conversion ===")
    print(f"25°C = {temp.celsius_to_fahrenheit(25):.1f}°F")
    print(f"98.6°F = {temp.fahrenheit_to_celsius(98.6):.1f}°C")
    
    print("\n=== File Tools ===")
    # Create a test file
    with open('test.txt', 'w') as f:
        f.write("Hello World!\nThis is a test file.\nIt has multiple lines.")
    
    lines, words, chars = ft.count_file_stats('test.txt')
    print(f"File stats - Lines: {lines}, Words: {words}, Characters: {chars}")
    
    print("\n=== Matrix Operations ===")
    m1 = [[1, 2], [3, 4]]
    m2 = [[5, 6], [7, 8]]
    print(f"Matrix addition: {mat.add_matrices(m1, m2)}")
    print(f"Matrix transpose: {mat.transpose_matrix(m1)}")
    
    print("\n=== Student Info ===")
    student = Student("Alice", "S001", [85, 90, 78, 92, 88])
    print(student.display_info())
    
    print("\n=== String Comparison ===")
    print(sc.compare_strings("apple", "banana"))
    
    print("\n=== Unit Conversion ===")
    print(f"100 cm = {conv.cm_to_m(100)} m")
    print(f"2.5 kg = {conv.kg_to_g(2.5)} g")
    
    print("\n=== Date Operations ===")
    days = do.days_between_dates("2023-01-01", "2023-12-31")
    print(f"Days between 2023-01-01 and 2023-12-31: {days}")
    
    print("\n=== Finance ===")
    print(f"Simple Interest (P=1000, R=5%, T=2): {fin.simple_interest(1000, 5, 2)}")
    print(f"Compound Interest (P=1000, R=5%, T=2): {fin.compound_interest(1000, 5, 2):.2f}")

if __name__ == "__main__":
    main()
