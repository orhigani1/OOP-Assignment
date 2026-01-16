def is_multiple(num1, num2):
    """Check if one number is a multiple of the other"""
    if num1 == 0 or num2 == 0:
        return False
    return num1 % num2 == 0 or num2 % num1 == 0


def main():
    """Main process to input numbers and check if one is a multiple of the other"""
    while True:
        try:
            num1 = int(input("Enter first number (or -1 to exit): "))
            if num1 == -1:
                print("Program ended.")
                break
            
            num2 = int(input("Enter second number (or -1 to exit): "))
            if num2 == -1:
                print("Program ended.")
                break
            
            if is_multiple(num1, num2):
                print("Yes, one number is a multiple of the other.")
            else:
                print("No, one number is not a multiple of the other.")
        
        except ValueError:
            print("Invalid input. Please enter integers only.")


if __name__ == "__main__":
    main()