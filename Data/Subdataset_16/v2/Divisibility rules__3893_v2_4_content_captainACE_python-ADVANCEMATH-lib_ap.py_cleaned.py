def fonk1():
    print("Welcome to the ARITHMETIC PROGRESSION module.")
    print("This module helps you find the last number in b1 sequence of numbers.")
    print("To determine the last number, you need to enter the first term, the common difference, and the number of terms in the AP.")
    while True:
        try:
            b1 = int(input("Please enter the first term of the sequence: "))
            b2 = int(input("Please enter the common difference of the sequence: "))
            b3 = int(input("Please enter the number of terms: "))
            b4 = b1 + (b3 - 1) * b2
            print(f"The last term of the arithmetic progression is: {b4}")
            break
        except ValueError:
            print("Invalid input. Please enter valid integer values for the first term, common difference, and number of terms.")
        except Exception as e:
            print(f"An error occurred: {e}. Please try again.")
if b5 = = "__main__":
    fonk1()