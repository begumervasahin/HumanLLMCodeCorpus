def fonk1(b2, b1):
    if b1 = = 0:
        return b2
    if b2 = = 0:
        return b1
    if b2 > b1:
        return fonk1(b2 - b1, b1)
    else:
        return fonk1(b2, b1 - b2)
def fonk2(b2, b1):
    if b1 = = 0:
        return b2
    return fonk2(b1, b2 % b1)
if b3 = = "__main__":
    while True:
        b4 = input("Choose Classic (c) or Modern (e) Euclid algorithm: ")
        while True:
            b5 = input("Enter 'exit' to choose another algorithm. Otherwise, enter b2 number: ")
            if b5.isnumeric():
                b2 = int(b5)
                b1 = int(input("Enter the second number: "))
                if b4.lower() == "c":
                    b6 = fonk1(b2, b1)
                else:
                    b6 = fonk2(b2, b1)
                print(f"The GCD of {b2} and {b1} is: {b6}")
            else:
                break