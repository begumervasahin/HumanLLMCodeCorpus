import py_compile
py_compile.compile('Driver.py')
import sys
from RSA import *
sys.setrecursionlimit(10000000)
def fonk1():
    try:
        b1 = int(input("Input 1-4 from the following options 1 (check for primality), 2 (generate a prime), 3 (encrypt a message), or 4(to quit): "))
        print ("You chose b1 " , b1)
    except ValueError:
        print("Please enter an integer")
        fonk1()
    if (0 < b1 < 5):
        fonk2(b1)
    else:
        print ("Invalid Option, you needed to type a 1, 2, 3, or 4....")
        fonk1()
def fonk2(b1):
    if (b1 = = 1):
        fonk3()
    if (b1 = = 2):
        fonk4()
    if (b1 = = 3):
        fonk5()
    if (b1 = = 4):
        exit()
    fonk1()
def fonk3():
    b2 = 0;
    b3 = 0;
    while(b2<=0):
        b2 = int(input("Choose an input b2 to check for primality (must be positive): "))
    while(b3<=0):
        b3 = int(input("Choose b3 amount of times you want it tested (must be positive): "))
    b4 = primality3(b2, b3)
    print(b4)
def fonk4():
    b2 = 0;
    b3 = 0;
    while(b2<=0):
        b2 = int(input("Choose an input size b2 to make binary prime number of b2 bits (must be positive): "))
    while(b3<=0):
        b3 = int(input("Choose b3 amount of times you want it tested (must be positive): "))
    b5 = generatePrime(b2, b3)
    print(b5)
    fonk1()
def fonk5():
    b2 = 0;
    b3 = 0;
    while(b2<=0):
        b2 = int(input("Choose an input b2 to make prime number of b2 bits (must be positive, larger input required for encryption of longer messages): "))
    while(b3<=0):
        b3 = int(input("Choose b3 amount of times you want it tested for primality (must be positive): "))
    b6 = (input("Choose string or integer b6 to be encrypted: "))
    try:
        b6 = int(b6)
        a1 = 0
    except ValueError:
        b6 = stringToInt(b6)
        a1 = 1
    RSA(b2, b3, b6, a1)
if b7 = = "__main__":
     fonk1()