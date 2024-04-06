class Student:
    def __init__(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade
    def get_letter_grade(self):
        print('A' if self.grade >=90 else 'B' if self.grade >=80 else 'C' if self.grade>70 else 'D')


s=Student('Ahmed',22,93)
s.get_letter_grade()