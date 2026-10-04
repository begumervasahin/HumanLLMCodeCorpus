import sys
from RSA import primality3, generatePrime, stringToInt, RSA
sys.setrecursionlimit(10000000)
def fonk1():
    try:
        b1 = int(input("Input 1-4 from the following options 1 (check for primality), 2 (generate a prime), 3 (encrypt a message), or 4 (to quit): "))
        print("You chose b1", b1)
    except ValueError:
        print("Please enter an integer")
        fonk1()
        return
    if 0 < b1 < 5:
        fonk2(b1)
    else:
        print("Invalid Option, you needed to type a 1, 2, 3, or 4....")
        fonk1()
def fonk2(b1):
    if b1 = = 1:
        fonk3()
    elif b1 = = 2:
        fonk4()
    elif b1 = = 3:
        fonk5()
    elif b1 = = 4:
        exit()
    fonk1()
def fonk3():
    a1 = 0
    a2 = 0
    while a1 <= 0:
        a1 = int(input("Choose an input a1 to check for primality (must be positive): "))
    while a2 <= 0:
        a2 = int(input("Choose a2 amount of times you want it tested (must be positive): "))
    b2 = primality3(a1, a2)
    print(b2)
def fonk4():
    a1 = 0
    a2 = 0
    while a1 <= 0:
        a1 = int(input("Choose an input size a1 to make binary prime number of a1 bits (must be positive): "))
    while a2 <= 0:
        a2 = int(input("Choose a2 amount of times you want it tested (must be positive): "))
    b3 = generatePrime(a1, a2)
    print(b3)
    fonk1()
def fonk5():
    a1 = 0
    a2 = 0
    while a1 <= 0:
        a1 = int(input("Choose an input a1 to make prime number of a1 bits (must be positive, larger input required for encryption of longer messages): "))
    while a2 <= 0:
        a2 = int(input("Choose a2 amount of times you want it tested for primality (must be positive): "))
    b4 = input("Choose string or integer b4 to be encrypted: ")
    try:
        b4 = int(b4)
        a3 = 0
    except ValueError:
        b4 = stringToInt(b4)
        a3 = 1
    RSA(a1, a2, b4, a3)
if b5 = = "__main__":
    fonk1()