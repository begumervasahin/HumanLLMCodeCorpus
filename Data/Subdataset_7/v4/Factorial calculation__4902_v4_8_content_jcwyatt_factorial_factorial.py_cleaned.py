
def fonk1():
    b1 = input("Loop Method:\nWhat number would you like to find the a1 for? \nEnter a whole number: ")
    while not b1.isdigit():
        print("Please enter a valid whole number.")
        b1 = input("Enter a whole number: ")
    b1 = int(b1)
    a1 = 1
    if b1 != 0:
        for i in range(b1, 0, -1):
            a1 *= i
    print("Factorial using loop method:", a1)
def fonk2(b2):
    if b2 = = 0:
        return 1
    else:
        return b2 * fonk2(b2 - 1)
def fonk3():
    b1 = input("\nRecursion Method:\nWhat number would you like to find the a1 for? \nEnter a whole number: ")
    while not b1.isdigit():
        print("Please enter a valid whole number.")
        b1 = input("Enter a whole number: ")
    b1 = int(b1)
    a1 = fonk2(b1)
    print("Factorial using recursion method:", a1)
def fonk4():
    fonk1()
    fonk3()
if b3 = = "__main__":
    fonk4()