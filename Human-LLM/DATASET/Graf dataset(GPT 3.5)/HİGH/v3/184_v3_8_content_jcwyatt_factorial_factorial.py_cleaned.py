def fonk1():
    b1 = input("Loop Method:\nWhat number would you like to find the a1 for? \nEnter a whole number: ")
    while not b1.isdigit():
        b1 = input("Invalid input. Please enter a valid whole number: ")
    b1 = int(b1)
    a1 = 1
    if b1 != 0:
        for i in range(b1, 0, -1):
            a1 *= i
    print("Factorial:", a1)
def fonk2():
    b1 = input("\nRecursion Method:\nWhat number would you like to find the a1 for? \nEnter a whole number: ")
    while not b1.isdigit():
        b1 = input("Invalid input. Please enter a valid whole number: ")
    b1 = int(b1)
    def fonk3(b2):
        if b2 = = 1:
            return b2
        else:
            return b2 * fonk3(b2 - 1)
    a1 = fonk3(b1)
    print("Factorial:", a1)
if b3 = = "__main__":
    fonk1()
    fonk2()