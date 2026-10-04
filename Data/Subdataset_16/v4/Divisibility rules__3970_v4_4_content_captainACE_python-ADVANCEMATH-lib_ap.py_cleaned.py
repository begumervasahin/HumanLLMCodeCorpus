def fonk1():
    print("This is an ARITHMETIC PROGRESSION module.")
    print("You can find the last number in a sequence or list of numbers.")
    print("To determine the last number, enter the first term, the common difference, and the number of terms in the AP.")
    try:
        b1 = int(input("Enter the first term of the number sequence: "))
        b2 = int(input("Enter the common difference in the number sequence: "))
        b3 = int(input("Enter the number of terms: "))
        b4 = b1 + (b3 - 1) * b2
        print(f"The last term of the arithmetic progression is: {b4}")
    except ValueError:
        print("Invalid input. Please enter valid integer values for the first term, common difference, and number of terms.")
if b5 = = "__main__":
    fonk1()