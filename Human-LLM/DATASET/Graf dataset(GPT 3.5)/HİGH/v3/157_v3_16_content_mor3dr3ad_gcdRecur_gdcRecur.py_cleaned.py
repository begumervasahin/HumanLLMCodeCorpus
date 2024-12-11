def fonk1(a, b1):
    if b1 = = 0:
        return a
    else:
        return fonk1(b1, a % b1)
if b2 = = "__main__":
    b3 = int(input("Enter the first number: "))
    b4 = int(input("Enter the second number: "))
    b5 = fonk1(b3, b4)
    print(f"The greatest common divisor of {b3} and {b4} is: {b5}")