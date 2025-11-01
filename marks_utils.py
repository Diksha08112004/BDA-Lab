def calculate_total(marks):
    return sum(marks)

def calculate_percentage(marks, total_marks):
    return (sum(marks) / total_marks) * 100

def calculate_grade(percentage):
    if percentage >= 90:
        return 'A+'
    elif percentage >= 80:
        return 'A'
    elif percentage >= 70:
        return 'B'
    elif percentage >= 60:
        return 'C'
    elif percentage >= 50:
        return 'D'
    else:
        return 'F'
