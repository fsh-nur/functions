operation = input("1:Addition, 2:Subtraction, 3:Division, 4:Multiplication ")


def addition(int1, int2):
    return int1 + int2


def subtraction(int1: int, int2: int):
    return int1 - int2


def division(int1: int, int2: int):
    return int1 / int2


def multiplication(int1: int, int2: int):
    return int1 * int2


if operation == "1":
    int1 = int(input("Enter the first number: "))
    int2 = int(input("Enter the second number: "))
    print(addition(int1, int2))
elif operation == "2":
    int1 = int(input("Enter the first number: "))
    int2 = int(input("Enter the second number: "))
    print(subtraction(int1, int2))
elif operation == "3":
    int1 = int(input("Enter the first number: "))
    int2 = int(input("Enter the second number: "))
    print(division(int1, int2))
elif operation == "4":
    int1 = int(input("Enter the first number: "))
    int2 = int(input("Enter the second number: "))
    print(multiplication(int1, int2))
else:
    print("This is not a valid input")
