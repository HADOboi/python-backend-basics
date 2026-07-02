def add(a, b):
    return a+b

def subtract(a, b):
    return a-b

def multiply(a, b):
    return a*b

def divide(a, b):
    return a/b

while True:
    print("\nCALCULATOR")
    print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Exit")

    choice = int(input("enter your choice: "))

    if choice == 5:
        print("Exitted")
        break

    if choice not in [1, 2, 3, 4]:
        print("invalid choice")
        continue

    try:
        num1 = float(input("enter first number: "))
        num2 = float(input("enter second number: "))

        if choice == 1:
            print("Result: ", add(num1, num2))

        elif choice == 2:
            print("Result: ", subtract(num1, num2))

        elif choice == 3:
            print("Result: ", multiply(num1, num2))

        elif choice == 4:
            if num2 == 0:
                print("cannot divide by zero")
            else:
                print("Result: ", divide(num1, num2))

    except ValueError:
        print("Enter valid numbers")
        