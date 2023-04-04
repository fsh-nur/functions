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

## ** Addition of Function of CM  -> M and M -> FT:
### The functions:
```commandline
def cm_m(int1: float):
    return int1 / 100


def m_ft(int1: float) -> float:
    return int1 * 3.2808399
```

### Calling the function if user inputs "5" or "6" in the calculator:
```commandline
elif operation == "5":
    int1 = int(input("Enter the number in centimeters to meters:"))
    print(cm_m(int1))

elif operation == "6":
    int1 = int(input("Enter the number in meters to feet:"))

    print(m_ft(int1))
```

### Example output for centimeters to meters:
```commandline
1:Addition, 2:Subtraction, 3:Division, 4:Multiplication 5: CM --> M  6: M --> FT 5
Enter the number in centimeters to meters:100
1.0
```

### Example output for meters to feet:
```commandline
1:Addition, 2:Subtraction, 3:Division, 4:Multiplication 5: CM --> M  6: M --> FT 6
Enter the number in meters to feet:150
492.125985
```