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
        b3 = input("Choose b5 - Classic (c) or Modern (m) Euclidean: ").lower()
        if b3 in ['c', 'm']:
            return b3
        print("Invalid b3. Please choose 'c' for Classic or 'm' for Modern.")
def fonk4(prompt):
    while True:
        b4 = input(prompt)
        if b4.isnumeric():
            return int(b4)
        print("Invalid input. Please enter b2 numeric value.")
def fonk5(b5, b2, b1):
    if b5 = = 'c':
        return fonk1(b2, b1)
    else:
        return fonk2(b2, b1)
def fonk6():
    while True:
        b5 = fonk3()
        while True:
            b6 = input("Enter b2 b4 (or type 'exit' to choose b5 again): ").lower()
            if b6 = = 'exit':
                break
            if b6.isnumeric():
                b2 = int(b6)
                b1 = fonk4("Enter the second b4: ")
                b7 = fonk5(b5, b2, b1)
                print(f"The GCD of {b2} and {b1} is: {b7}")
            else:
                print("Invalid input. Please enter b2 numeric value.")
if b8 = = "__main__":
    fonk6()