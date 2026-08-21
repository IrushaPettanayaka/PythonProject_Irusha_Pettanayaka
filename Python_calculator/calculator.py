def add(x, y):
    return x + y

def subtract(x, y):
    return x - y 

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        print("Error: Division by zero is not allowed.")
        return None
    return x / y

def power(x, y):
    return x ** y

def square_root(x):
    if x < 0:
        print("Error: Square root of negative number is not defined.")
        return None
    return x ** 0.5

def modulus(x, y):
    if y == 0:
        print("Error: Modulus by zero is not allowed.")
        return None
    return x % y

def floor_division(x, y):
    if y == 0:
        print("Error: Floor division by zero is not allowed.")
        return None
    return x // y

def main():
    while True:
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Power")
        print("6. Square Root")
        print("7. Modulus")
        print("8. Floor Division")
        print("9. Exit")
        
        choice = input("Enter the Choice (1/2/3/4/5/6/7/8/9): ").strip()
        
        if choice == '9':
            print("Exiting the calculator. Goodbye!")
            break

        
        if choice not in ['1', '2', '3', '4', '5', '6', '7', '8']:
            print("Invalid input. Please try again.")
            continue

       
        try:
            num1 = float(input('Enter the first number: '))
            
            if choice in ['1', '2', '3', '4', '7', '8']:
                num2 = float(input('Enter the second number: '))
            elif choice == '5':
                num2 = float(input('Enter the exponent: '))
            elif choice == '6':
                num2 = None
        except ValueError:
            print("Error: Invalid numeric input. Please enter numbers only.")
            continue

        # Execute selected operation
        if choice == '1':
            print('Result:', num1, "+", num2, "=", add(num1, num2))
        elif choice == '2':
            print('Result:', num1, "-", num2, "=", subtract(num1, num2))
        elif choice == '3':
            print('Result:', num1, "*", num2, "=", multiply(num1, num2))
        elif choice == '4':
            result = divide(num1, num2)
            if result is not None:
                print('Result:', num1, "/", num2, "=", result)
        elif choice == '5':
            print('Result:', num1, "^", num2, "=", power(num1, num2))
        elif choice == '6':
            result = square_root(num1)
            if result is not None:
                print('Result: Square root of', num1, "=", result)
        elif choice == '7':
            result = modulus(num1, num2)
            if result is not None:
                print('Result:', num1, "%", num2, "=", result)
        elif choice == '8':
            result = floor_division(num1, num2)
            if result is not None:
                print('Result:', num1, "//", num2, "=", result)

if __name__ == "__main__":
    main()
