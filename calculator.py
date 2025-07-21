from operations import add, subtract, multiply, divide
from logger import log_operation


def main():
    print("Welcome to the Simple Calculator!")
    print("Available operations: +  -  *  /")

    while True:
        try:
            a = float(input("Enter first number: "))
            op = input("Enter operation (+, -, *, /): ")
            b = float(input("Enter second number: "))

            if op == '+':
                result = add(a, b)
            elif op == '-':
                result = subtract(a, b)
            elif op == '*':
                result = multiply(a, b)
            elif op == '/':
                result = divide(a, b)
            else:
                print("Invalid operation.")
                continue

            print(f"Result: {result}")
            log_operation(op, a, b, result)

        except ValueError as e:
            print("Error:", e)

        again = input("Do you want to perform another calculation? (y/n): ")
        if again.lower() != 'y':
            print("Thank you for using the calculator.")
            break


if __name__ == "__main__":
    main()