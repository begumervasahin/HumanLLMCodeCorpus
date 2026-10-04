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
def fonk3():
    while True:
        b3 = input("Choose algorithm - Classic (c) or Modern (m) Euclidean: ").lower()
        if b3 in ['c', 'm']:
            return b3
        print("Invalid choice. Please choose 'c' for Classic or 'm' for Modern.")
def fonk4(prompt):
    while True:
        b4 = input(prompt)
        if b4.isnumeric():
            return int(b4)
        print("Invalid input. Please enter b2 numeric value.")
def fonk5(b3, b2, b1):
    if b3 = = 'c':
        return fonk1(b2, b1)
    else:
        return fonk2(b2, b1)
def fonk6():
    while True:
        b3 = fonk3()
        while True:
            b5 = input("Enter b2 number (or type 'exit' to choose algorithm again): ").lower()
            if b5 = = 'exit':
                break
            if b5.isnumeric():
                b2 = int(b5)
                b1 = fonk4("Enter the second number: ")
                b6 = fonk5(b3, b2, b1)
                print(f"The GCD of {b2} and {b1} is: {b6}")
            else:
                print("Invalid input. Please enter b2 numeric value.")
if b7 = = "__main__":
    fonk6()