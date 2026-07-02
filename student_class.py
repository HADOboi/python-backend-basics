class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def display_details(self):
        print("\n\n")
        print("Name : ", self.name)
        print("Age : ", self.age)
        print("Course : ", self.course)
    
name = input("enter student name: ")
age = int(input("enter sutdent age: "))
course = input("enter course: ")

student1 = Student(name, age, course)
student1.display_details()