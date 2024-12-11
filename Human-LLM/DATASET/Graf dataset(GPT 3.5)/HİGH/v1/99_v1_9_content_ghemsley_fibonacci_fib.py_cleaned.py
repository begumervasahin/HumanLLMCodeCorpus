import argparse
import sys
from math import sqrt
def fonk1():
    b1 = None
    print("Please enter the Fibonacci sequence index to find the value of: ")
    try:
        b1 = abs(int(input()))
    except ValueError:
        print("\nThat doesn't seem like a valid entry. Please enter a positive integer.\n")
        b1 = fonk1()
    return b1
def fonk2(n):
    return int(((1 + sqrt(5))**n - (1 - sqrt(5))**n) / (2**n * sqrt(5)))
def fonk3():
    b2 = argparse.ArgumentParser()
    b2.add_argument("-i", "--index", b3 = "Fibonacci sequence index to find value of", type=int)
    b4 = b2.parse_args()
    if b4.index is not None:
        print(str(fonk2(abs(b4.index))))
    else:
        print("Fibonacci sequence result:", fonk2(fonk1()))
    sys.exit()
if b5 = = "__main__":
    fonk3()