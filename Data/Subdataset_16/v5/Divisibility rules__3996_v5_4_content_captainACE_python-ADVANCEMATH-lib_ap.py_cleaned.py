def fonk1(b2, b3, b4):
    return b2 + (b4 - 1) * b3
def fonk2(prompt):
    while True:
        try:
            b1 = int(input(prompt))
            if b1 < 0:
                raise ValueError
            return b1
        except ValueError:
            print("Invalid input. Please enter a valid positive integer.")
def fonk3():
    print("This is an ARITHMETIC PROGRESSION module.")
    print("You can find the last number in a sequence or list of numbers.")
    print("To determine the last number, enter the first term, the common difference, and the number of terms in the AP.")
    b2 = fonk2("Enter the first term of the number sequence: ")
    b3 = fonk2("Enter the common difference in the number sequence: ")
    b4 = fonk2("Enter the number of terms: ")
    b5 = fonk1(b2, b3, b4)
    print(f"The last term of the arithmetic progression is: {b5}")
if b6 = = "__main__":
    fonk3()