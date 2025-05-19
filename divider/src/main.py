from utils.helpers import add, subtract, multiply, divide

def main():
    
    print("Welcome to My Python App!")
    print("This app performs basic arithmetic operations.")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Please select an operation (1-4): ")

    if choice in ['1','2','3','4']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if choice == '1':
            result = add(num1, num2)
            print(f"The result of addition is: {result}")
        elif choice == '2':
            result = subtract(num1, num2)
            print(f"The result of subtraction is: {result}")
        elif choice == '3':
            result = multiply(num1, num2)
            print(f"The result of multiplication is: {result}")
        elif choice == '4':
            try:
                result = divide(num1, num2)
                print(f"The result of division is: {result}")
            except ValueError as e:
                print(e)
        else:
            print("Invalid choice. Please select a valid operation.")

    else:
        print("Invalid choice. Please select a valid operation.")
        print("Thank you for using My Python App!")

if __name__ == "__main__":
    main()