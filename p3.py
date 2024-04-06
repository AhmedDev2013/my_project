class Student:
    def __init__(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade
    def get_letter_grade(self):
        return 'A' if self.grade >=90 else 'B' if self.grade >=80 else 'C' if self.grade>70 else 'D'


s=Student('Ahmed',22,93)
print(f"The grade of {s.name} is {s.get_letter_grade()}")