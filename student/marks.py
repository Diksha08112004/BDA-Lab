""
Marks module for student package.
Provides functions to manage and calculate student marks.
"""

# Dictionary to store student marks
student_marks = {}

def add_student(student_id):
    """Initialize a new student record."""
    if student_id not in student_marks:
        student_marks[student_id] = {}
        return True
    return False

def add_mark(student_id, subject, mark):
    """Add a mark for a student in a specific subject."""
    if student_id not in student_marks:
        add_student(student_id)
    student_marks[student_id][subject] = mark
    return student_marks[student_id]

def get_marks(student_id):
    """Get all marks for a student."""
    return student_marks.get(student_id, {})

def get_average(student_id):
    """Calculate average marks for a student."""
    marks = get_marks(student_id).values()
    if not marks:
        return 0
    return sum(marks) / len(marks)

def get_total(student_id):
    """Calculate total marks for a student."""
    return sum(get_marks(student_id).values())

def get_subject_average(subject):
    """Calculate class average for a specific subject."""
    marks = [marks[subject] for marks in student_marks.values() 
             if subject in marks]
    if not marks:
        return 0
    return sum(marks) / len(marks)
