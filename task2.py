def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"

def calculator():
    print("Simple Calculator")

    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
            continue

        operation = input("Choose an operation (+, -, *, /): ")

        if operation not in ['+', '-', '*', '/']:
            print("Invalid operation. Please choose +, -, *, or /.")
            continue

        if operation == '+':
            result = add(num1, num2)
        elif operation == '-':
            result = subtract(num1, num2)
        elif operation == '*':
            result = multiply(num1, num2)
        elif operation == '/':
            result = divide(num1, num2)

        print(f"Result: {result}")

        play_again = input("Do you want to perform another calculation? (yes/no): ").lower()
        if play_again != 'yes':
            print('Thanks for using the calculator!')
            break

if __name__ == "__main__":
    calculator()
