import json

with open("students.json", "r") as file:
    students = json.load(file)

print("Current students:")
for student in students:
    print(student)

name = input("Enter student naem: ")
age = input("Enter student age: ")
course = input("Enter student course: ")

new_student = {
    "name": name,
    "age": age,
    "course": course
}

students.append(new_student)

with open("students.json", "w") as file:
    json.dump(students, file, indent = 4)

print("studnet added successfully")