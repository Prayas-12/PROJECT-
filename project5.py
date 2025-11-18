#basic calculator
import math

print("========== ADVANCED PYTHON CALCULATOR ==========")

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Cannot divide by zero."
    return a / b

def power(a, b):
    return a ** b

def square_root(a):
    if a < 0:
        return "Error! Cannot take square root of negative number."
    return math.sqrt(a)

def logarithm(a):
    if a <= 0:
        return "Error! Logarithm undefined for zero or negative numbers."
    return math.log10(a)

def sine(a):
    return math.sin(math.radians(a))

def cosine(a):
    return math.cos(math.radians(a))

def tangent(a):
    return math.tan(math.radians(a))

def factorial(n):
    if n < 0:
        return "Error! Factorial of negative number doesn't exist."
    return math.factorial(n)

while True:
    print("\n----- MENU -----")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power (a^b)")
    print("6. Square Root")
    print("7. Logarithm (log10)")
    print("8. Sine")
    print("9. Cosine")
    print("10. Tangent")
    print("11. Factorial")
    print("12. Exit")

    choice = input("Enter choice: ")

    if choice == '12':
        print("Exiting Calculator... Goodbye!")
        break

    # operations that need two numbers
    if choice in ['1','2','3','4','5']:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if choice == '1':
            print("Result =", add(a, b))
        elif choice == '2':
            print("Result =", subtract(a, b))
        elif choice == '3':
            print("Result =", multiply(a, b))
        elif choice == '4':
            print("Result =", divide(a, b))
        elif choice == '5':
            print("Result =", power(a, b))

    # operations with one number
    elif choice in ['6','7','8','9','10']:
        a = float(input("Enter number: "))

        if choice == '6':
            print("Result =", square_root(a))
        elif choice == '7':
            print("Result =", logarithm(a))
        elif choice == '8':
            print("Result = sin(a) =", sine(a))
        elif choice == '9':
            print("Result = cos(a) =", cosine(a))
        elif choice == '10':
            print("Result = tan(a) =", tangent(a))

    elif choice == '11':
        n = int(input("Enter an integer: "))
        print("Result =", factorial(n))

    else:
        print("Invalid choice! Try again.")
