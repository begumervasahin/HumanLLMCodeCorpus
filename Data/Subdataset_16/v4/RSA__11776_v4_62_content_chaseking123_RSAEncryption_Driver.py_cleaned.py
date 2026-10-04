import py_compile
import sys
from RSA import *
import py_compile
sys.setrecursionlimit(10000000)
py_compile.compile('Driver.py')
def fonk1():
    try:
        b1 = int(input("Input 1-4 from the following options:\n"
                           "1: Check for primality\n"
                           "2: Generate a prime\n"
                           "3: Encrypt a message\n"
                           "4: Quit\n"
                           "Enter your choice: "))
        print(f"You chose b1 {b1}")
    except ValueError:
        print("Please enter an integer.")
        fonk1()
        return
    if 1 <= b1 <= 4:
        fonk2(b1)
    else:
        print("Invalid Option, you needed to type 1, 2, 3, or 4.")
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
def fonk3():
    b2 = fonk6("Choose an input b2 to check for primality (must be positive): ")
    b3 = fonk6("Choose b3 amount of times you want it tested (must be positive): ")
    b4 = primality3(b2, b3)
    print(f"Is the number prime? {b4}")
def fonk4():
    b2 = fonk6("Choose an input size b2 to make binary prime number of b2 bits (must be positive): ")
    b3 = fonk6("Choose b3 amount of times you want it tested (must be positive): ")
    b5 = generatePrime(b2, b3)
    print(f"Generated prime number: {b5}")
    fonk1()
def fonk5():
    b2 = fonk6("Choose an input b2 to make prime number of b2 bits (must be positive, larger input required for encryption of longer messages): ")
    b3 = fonk6("Choose b3 amount of times you want it tested for primality (must be positive): ")
    b6 = input("Choose string or integer b6 to be encrypted: ")
    try:
        b6 = int(b6)
        a1 = 0
    except ValueError:
        b6 = stringToInt(b6)
        a1 = 1
    RSA(b2, b3, b6, a1)
def fonk6(prompt):
    while True:
        try:
            b7 = int(input(prompt))
            if b7 > 0:
                return b7
            else:
                print("The number must be positive.")
        except ValueError:
            print("Please enter a valid integer.")
if b8 = = "__main__":
    fonk1()