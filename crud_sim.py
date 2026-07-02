students = []

def create_student():
    name = input('enter student name: ')
    students.append(name)
    print("student appended successfully")

def read_students():
    if not students:
        print("no students found")
        return
    
    print("STUDNTS LIST")
    for i, student in enumerate(students, start=1):
        print(f"{i}. {student}")

def update_student():
    read_students()
    try:
        index = int(input("enter student number to update"))
        
        if 0 <= index < len(students):
            new_name = input("enter new name: ")
            students[index] = new_name
            print("student updated successfully")
        else:
            print("invalid student number")

    except ValueError:
        print("enter valid number")

def delete_student():
    read_students()

    try:
        index = int(input("enter studnet number to delete: "))-1

        if 0 <= index < len(students):
            removed_student = students.pop(index)
            print(f"{removed_student} deleted.")
        else:
            print("invalid student number")
    
    except ValueError:
        print("enter valid number")

while True:
    print("\nSTUDENTS CRUD SIMULATION")
    print("1. Create Student\n2. View Students\n3. Update Student\n4. Delete Student\n5. Exit")

    choice = int(input("enter your choice: "))-1

    if choice == 1:
        create_student()

    elif choice == 2:
        read_students()

    elif choice == 3:
        update_student()

    elif choice == 4:
        delete_student()

    elif choice == 5:
        print("exitted")
        break

    else:
        print("Invalid choice")