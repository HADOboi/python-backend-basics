class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def display_details(self):
        print("\n\nSTUDENT DETAILS")
        print("---------------")
        print("Name : ", self.name)
        print("Age : ", self.age)
        print("Course : ", self.course)

class GraduateStudent(Student):
    def __init__(self, name, age, course, specialization):
        super().__init__(name, age,course)
        self.specialization = specialization

    def display_details(self):
        super().display_details()
        print("Specialization : ", self.specialization)
    
name = input("enter student name: ")
age = int(input("enter sutdent age: "))
course = input("enter course: ")
specialization = input("enter specialization: ")

student1 = GraduateStudent(name, age, course, specialization)
student1.display_details()