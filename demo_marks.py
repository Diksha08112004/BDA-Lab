import marks_utils as mu

def main():
    # Sample student data
    subjects = ["Math", "Physics", "Chemistry", "English", "Computer Science"]
    max_marks_per_subject = 100
    total_possible_marks = len(subjects) * max_marks_per_subject
    
    # Student 1
    student1_marks = [85, 92, 78, 88, 95]
    
    # Calculate results
    total = mu.calculate_total(student1_marks)
    percentage = mu.calculate_percentage(student1_marks, total_possible_marks)
    grade = mu.calculate_grade(percentage)
    
    # Display results
    print("=== Student Grade Calculator ===\n")
    print("Subject-wise Marks (Out of 100):")
    for subject, mark in zip(subjects, student1_marks):
        print(f"{subject}: {mark}")
    
    print("\n=== Results ===")
    print(f"Total Marks: {total} / {total_possible_marks}")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade: {grade}")
    
    # Grade explanation
    print("\n=== Grade System ===")
    print("A+: 90% and above")
    print("A : 80% - 89%")
    print("B : 70% - 79%")
    print("C : 60% - 69%")
    print("D : 50% - 59%")
    print("F : Below 50%")
    
    # Additional test cases
    print("\n=== Test Cases ===")
    test_cases = [
        ([95, 92, 98, 90, 95], "Top Student"),
        ([75, 82, 78, 80, 85], "Good Student"),
        ([45, 52, 48, 50, 55], "Passing Student"),
        ([35, 42, 38, 30, 25], "Failing Student")
    ]
    
    for marks, desc in test_cases:
        total_marks = sum(marks)
        percentage = mu.calculate_percentage(marks, total_possible_marks)
        grade = mu.calculate_grade(percentage)
        print(f"\n{desc}:")
        print(f"Marks: {marks}")
        print(f"Total: {total_marks}/{total_possible_marks}")
        print(f"Percentage: {percentage:.2f}%")
        print(f"Grade: {grade}")

if __name__ == "__main__":
    main()
