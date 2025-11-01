""
Grade module for student package.
Provides functions to calculate grades based on marks.
"""

def calculate_grade(percentage):
    """
    Calculate grade based on percentage.
    
    Grading Scale:
    - A: 90-100
    - B: 80-89
    - C: 70-79
    - D: 60-69
    - F: Below 60
    """
    if not isinstance(percentage, (int, float)) or percentage < 0 or percentage > 100:
        return 'Invalid'
    
    if percentage >= 90:
        return 'A'
    elif percentage >= 80:
        return 'B'
    elif percentage >= 70:
        return 'C'
    elif percentage >= 60:
        return 'D'
    else:
        return 'F'

def get_grade_points(grade):
    """Convert letter grade to grade points."""
    grade_points = {
        'A': 4.0,
        'B': 3.0,
        'C': 2.0,
        'D': 1.0,
        'F': 0.0
    }
    return grade_points.get(grade.upper(), 0.0)

def calculate_gpa(marks_dict):
    """
    Calculate GPA based on a dictionary of subject:mark pairs.
    Assumes all subjects have equal weight.
    """
    if not marks_dict:
        return 0.0
    
    total_grade_points = 0
    for mark in marks_dict.values():
        grade = calculate_grade(mark)
        total_grade_points += get_grade_points(grade)
    
    return round(total_grade_points / len(marks_dict), 2)

def get_grade_remark(grade):
    """Get a descriptive remark for a grade."""
    remarks = {
        'A': 'Excellent',
        'B': 'Good',
        'C': 'Average',
        'D': 'Needs Improvement',
        'F': 'Fail'
    }
    return remarks.get(grade.upper(), 'Invalid Grade')
