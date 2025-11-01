import student as st

def main():
    print("=== Student Marks & Grade System ===\n")
    
    # Add students and their marks
    st.marks.add_mark("S001", "Math", 85)
    st.marks.add_mark("S001", "Science", 78)
    st.marks.add_mark("S001", "English", 92)
    
    st.marks.add_mark("S002", "Math", 65)
    st.marks.add_mark("S002", "Science", 72)
    st.marks.add_mark("S002", "English", 58)
    
    # Display student information
    def show_student_info(student_id):
        print(f"\nStudent ID: {student_id}")
        print("-" * 30)
        
        # Get student marks
        marks = st.marks.get_marks(student_id)
        print("Subject-wise Marks:")
        for subject, mark in marks.items():
            grade = st.grade.calculate_grade(mark)
            print(f"  {subject}: {mark}% ({grade})")
        
        # Calculate and display summary
        total = st.marks.get_total(student_id)
        average = st.marks.get_average(student_id)
        gpa = st.grade.calculate_gpa(marks)
        overall_grade = st.grade.calculate_grade(average)
        
        print(f"\nTotal Marks: {total}")
        print(f"Average: {average:.2f}%")
        print(f"Overall Grade: {overall_grade} ({st.grade.get_grade_remark(overall_grade)})")
        print(f"GPA: {gpa:.2f}")
    
    # Show info for each student
    for student_id in ["S001", "S002"]:
        show_student_info(student_id)
    
    # Show class averages
    print("\n=== Class Averages ===")
    for subject in ["Math", "Science", "English"]:
        avg = st.marks.get_subject_average(subject)
        print(f"{subject}: {avg:.2f}%")

if __name__ == "__main__":
    main()
