# 🟢Q2 – Student Grade Evaluator
# Create a class Student with name and marks (list of 5 subjects).

# Add a method calculate_grade() that:
# Averages marks
# Returns “A”, “B”, “C”, or “F” based on the average

class Student:
    def __init__(self,name , marks ):
        self.name = name
        self.marks = marks

    def calculate_grade(self):
        total = sum(self.marks)

        if total > 250:
            print("your mark is greater than total marks")
        elif total >= 230:
            print(f"Total Marks : {self.marks} Grade: A+")
        elif total >= 200:
            print(f"Total Marks : {self.marks} Grade: A")
        elif total >= 160:
            print(f"Total Marks : {self.marks} Grade: B")
        elif total >= 130 :
            print(f"Total Marks : {self.marks} Grade: C")
        elif total >= 100:
            print(f"Total Marks : {self.marks} Grade: D")
        elif total < 100:
            print(f"Total Marks : {self.marks} fails better than next time..")


new_student = Student("Hassan" , [20 , 30 , 30 , 10, 9])
new_student.calculate_grade()