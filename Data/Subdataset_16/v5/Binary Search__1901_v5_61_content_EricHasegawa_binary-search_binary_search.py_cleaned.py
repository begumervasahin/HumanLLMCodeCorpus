def fonk1():
    while True:
        b1 = fonk2()
        b2 = fonk3("numberlist.txt")
        b3 = sorted(b2)
        if fonk4(b3, b1):
            print("Target found!")
        else:
            print("Target not found.")
        if not fonk5():
            print("Exiting. Goodbye!")
            break
def fonk2():
    while True:
        try:
            return int(input("Enter an integer: "))
        except ValueError:
            print("You did not enter an integer. Please try again.")
def fonk3(filename):
    with open(filename) as file:
        b4 = file.read()
        return list(map(int, b4.split(", ")))
def fonk4(b3, b1):
    b7, b5 = 0, len(b3) - 1
    while b7 <= b5:
        b6 = (b7 + b5)
        if b1 = = b3[b6]:
            return True
        elif b1 > b3[b6]:
            b7 = b6 + 1
        else:
            b5 = b6 - 1
    return False
def fonk5():
    while True:
        b8 = input("Would you like to test another number? (y/n): ").lower()
        if b8 in ['y', 'n']:
            return b8 = = 'y'
        print("Invalid input. Please enter 'y' or 'n'.")
fonk1()