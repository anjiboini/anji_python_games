class Student:
    def __init__(self,rollno,name):
        self.rollno = rollno
        self.name = name
    def displayStudent(self):
        print("Roll No.",self.rollno,"Name",self.name)
s1=Student(101,"anji")
s2=Student(102,"thanu")
s1.displayStudent()
s2.displayStudent()
