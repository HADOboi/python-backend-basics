class Student:
    def __init__(self, name, age, course):
        self.__name = name
        self.__age = age
        self.__course = course

        def get_name(self):
            return self.__name

        def get_age(self):
            return self.__age

        def get_course(self):
            return self.__course

        def set_age(self, age):
            if age > 0:
                self.__age = age
            else:
                print("Invalid age")

    def display_details(self):
        print("\n\nSTUDENT DETAILS")
        print("---------------")
        print("Name : ", self.__name)
        print("Age : ", self.__age)
        print("Course : ", self.__course)

class GraduateStudent(Student):
    def __init__(self, name, age, course, specialization):
        super().__init__(name, age,course)
        self.__specialization = specialization

    def display_details(self):
        super().display_details()
        print("Specialization : ", self.__specialization)
    
name = input("enter student name: ")

while True:
    try:
        age = int(input("enter sutdent age: "))
        if age <= 0:
            print("age must be greater than 0")
            continue
        break
    except ValueError:
        print("Enter valid age")

course = input("enter course: ")
specialization = input("enter specialization: ")

student1 = GraduateStudent(name, age, course, specialization)
student1.display_details()