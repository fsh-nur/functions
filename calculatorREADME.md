# Calculator Program

## 1. User inputs number according to what function they would like to use:

```commandline
operation = input("1:Addition, 2:Subtraction, 3:Division, 4:Multiplication ")

```

### Output:

```commandline
1:Addition, 2:Subtraction, 3:Division, 4:Multiplication 
```

## 2. Functions are defined for each operation:

```commandline
def addition(int1, int2):
    return int1 + int2


def subtraction(int1: int, int2: int):
    return int1 - int2


def division(int1: int, int2: int):
    return int1 / int2


def multiplication(int1: int, int2: int):
    return int1 * int2
```

## 3. IF/ELSEIF/ELSE statements according to what function the user chooses, is called and they are also asked to input the two numbers they would like to use for the calculator:

```commandline
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
```

### Output

```commandline
Enter the first number: 
Enter the second number:
```

## Example output of program:

```commandline
1:Addition, 2:Subtraction, 3:Division, 4:Multiplication 4
Enter the first number: 3
Enter the second number: 4
12
```