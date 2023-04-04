# functions

# Allow you to follow DRY

# Do Not Repeat Yourself

# def print_something(print_string) -> object:
#     return print(print_string)
#
#
# print_something("My name is Fatima")
# print_something("I am 23")


#
#
# # return statement
#
# def addition(int1, int2):
#     return int1 + int2
#
#
# print(addition(2, 2))

# Default arguments


# def addition(int1=2, int2=1):
#     return int1 + int2
#
# print(addition(10, 2))

# multiple arguments

def multi_args(*multiargs):
    print(type(multiargs))

    for arg in multiargs:
        print(arg)


multi_args(1, 2, 3, "Hello", 4, 6, 6)


# Type hints

def greeting(name: str):
    print("Hello, my name is " + name)


greeting("Fatima")


def division(denum: int, num: int) -> float:
    return denum / num


print(division(12, 5))

# This function subtracts 2 numbers
def subtraction(int1: int = 5, int2: int = 2) -> int:
    return int1 - int2


print(subtraction())

# functions best practices

# 1. Name your methods using lower case and underscores
# 2. All arguments should be clear in their need and where possible their expected type
# 3. Remember the return statement or your function will return None in most cases
# 4. Keep your functions as small as possible, and keep them as readable as possible
# 5. Use commments within your methods to help with instructions on how to use them
# 6. Consider using Type hHints in order to avoid errors