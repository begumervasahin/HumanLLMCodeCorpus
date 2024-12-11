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
    else:
        return fonk2(b1, b2 % b1)
if b3 = = "__main__":
    while True:
        b4 = input("Classic (c) or modern Euclid (e) algorithm? ")
        if b4.lower() not in ['c', 'e']:
            print("Invalid input. Please choose 'c' or 'e'.")
            continue
        while True:
            b5 = input("Enter 'exit' to choose another algorithm. Otherwise, enter b2 number: ")
            if b5.lower() == 'exit':
                break
            elif b5.isnumeric():
                b2 = int(b5)
                b1 = int(input("Enter the second number: "))
                if b4 = = "c":
                    b6 = fonk1(b2, b1)
                else:
                    b6 = fonk2(b2, b1)
                print(f"GCD of {b2} and {b1} is: {b6}")
            else:
                print("Invalid input. Please enter b2 number or 'exit'.")