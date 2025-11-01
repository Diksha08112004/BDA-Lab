import student_info as si

def main():
    print("=== Student Information System Demo ===\n")
    
    # Create some students
    print("1. Creating student records...")
    student1 = si.Student("S001", "John Doe", 20, "Computer Science")
    student2 = si.Student("S002", "Jane Smith", 21, "Electrical Engineering")
    student3 = si.Student("S003", "Alice Johnson", 19, "Mathematics")
    
    # Test display_info method
    print("\n2. Displaying student information:")
    student1.display_info()
    print()
    student2.display_info()
    
    # Test adding courses and grades
    print("\n3. Adding courses and grades...")
    student1.add_grade("CS101", 85)
    student1.add_grade("MATH201", 92)
    student1.add_grade("PHYS101", 78)
    
    student2.add_grade("EE201", 88)
    student2.add_grade("MATH202", 95)
    
    student3.add_grade("MATH301", 90)
    student3.add_grade("CS101", 82)
    
    # Test getting grades
    print("\n4. Getting student grades:")
    print(f"{student1.name}'s grades: {student1.get_grades()}")
    print(f"{student2.name}'s grades: {student2.get_grades()}")
    
    # Test calculating GPA
    print("\n5. Calculating GPAs:")
    print(f"{student1.name}'s GPA: {student1.calculate_gpa():.2f}")
    print(f"{student2.name}'s GPA: {student2.calculate_gpa():.2f}")
    print(f"{student3.name}'s GPA: {student3.calculate_gpa():.2f}")
    
    # Test getting student by ID
    print("\n6. Getting student by ID:")
    student_id = "S002"
    print(f"Looking up student with ID {student_id}...")
    # In a real scenario, we'd have a StudentDatabase class to handle this
    students = {s.student_id: s for s in [student1, student2, student3]}
    if student_id in students:
        print(f"Found student: {students[student_id].name}")
    else:
        print("Student not found")
    
    # Test updating student information
    print("\n7. Updating student information:")
    print("Before update:")
    student3.display_info()
    
    print("\nAfter updating major and age:")
    student3.update_info(major="Computer Science", age=20)
    student3.display_info()
    
    # Test getting student status
    print("\n8. Student status:")
    print(f"{student1.name} is a {student1.get_status()} student")
    print(f"{student2.name} is a {student2.get_status()} student")
    
    # Test getting student's courses
    print("\n9. Student's courses:")
    print(f"{student1.name}'s courses: {list(student1.grades.keys())}")
    
    # Test getting specific grade
    course = "CS101"
    print(f"\n10. {student1.name}'s grade in {course}: {student1.get_grade(course)}")
    
    # Test non-existent grade
    course = "BIO101"
    print(f"{student1.name}'s grade in {course}: {student1.get_grade(course) or 'Not enrolled'}")
    
    # Test getting student summary
    print("\n11. Student Summary:")
    print("-" * 50)
    print(f"Student ID: {student1.student_id}")
    print(f"Name: {student1.name}")
    print(f"Age: {student1.age}")
    print(f"Major: {student1.major}")
    print(f"GPA: {student1.calculate_gpa():.2f}")
    print("Courses:")
    for course, grade in student1.grades.items():
        print(f"  - {course}: {grade}")
    print("-" * 50)

if __name__ == "__main__":
    main()
