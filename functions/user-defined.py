from typing import Union

# Define a function to add two numbers
def add_numbers(a, b) :
    return a + b
print(add_numbers(10,20))

# Define a function to subtract two numbers
def subtract_numbers(a, b):
    return a - b

# Define a function to multiply two numbers
def multiply_numbers(a, b):
    return a * b

# Define a function to divide two numbers
def divide_numbers(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

# Test the functions
if __name__ == "__main__":
    x = 10
    y = 5

    print(f"Addition of {x} and {y}: {add_numbers(x, y)}")
    print(f"Subtraction of {x} and {y}: {subtract_numbers(x, y)}")
    print(f"Multiplication of {x} and {y}: {multiply_numbers(x, y)}")
    print(f"Division of {x} and {y}: {divide_numbers(x, y)}")