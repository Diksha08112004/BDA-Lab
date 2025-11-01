class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
    
    def display_info(self):
        return (f"Name: {self.name}\n"
                f"Roll No: {self.roll_no}\n"
                f"Marks: {self.marks}\n"
                f"Total: {sum(self.marks)}\n"
                f"Percentage: {sum(self.marks)/len(self.marks):.2f}%")
