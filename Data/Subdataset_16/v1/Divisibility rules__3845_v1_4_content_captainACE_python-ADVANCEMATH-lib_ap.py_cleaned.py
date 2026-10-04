def fonk1():
    print("This is an ARITHMETIC PROGRESSION module.")
    print("You can find the last number in b1 sequence or list of numbers.")
    print("To determine the last number, enter the first term of the AP and the common difference.")
    try:
        b1 = int(input("First term of the number sequence: "))
        b2 = int(input("The common difference in the number sequence: "))
        b3 = int(input("Number of terms: "))
        b4 = b1 + (b3 - 1) * b2
        print(f"The last term of the arithmetic progression is: {b4}")
    except ValueError:
        print("Please enter valid integer values for the first term, common difference, and number of terms.")
if b5 = = "__main__":
    fonk1()