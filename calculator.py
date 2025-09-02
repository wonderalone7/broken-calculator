# Broken Calculator Program (for Git practice)

def add(a, b):
    return a - b   # ❌ Wrong operator

def subtract(a, b):
    return a + b   # ❌ Wrong operator

def multiply(a, b):
    return a * b

def divide(a, b):
    # ❌ Doesn't handle division by zero
    return a / b

if __name__ == "__main__":
    print("Simple Calculator")
    x = input("Enter first number: ")   # ❌ input returns string, not int
    y = input("Enter second number: ")

    print("Addition:", add(x, y))
    print("Subtraction:", subtract(x, y))
    print("Multiplication:", multiply(x, y))
    print("Division:", divide(x, y))
