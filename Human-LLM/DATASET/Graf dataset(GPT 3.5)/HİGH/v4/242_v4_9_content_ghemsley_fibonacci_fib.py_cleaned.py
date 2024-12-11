import argparse
import sys
from math import sqrt
def fonk1():
    while True:
        try:
            b1 = abs(int(input("Please enter the index of the Fibonacci sequence to find its value: ")))
            return b1
        except ValueError:
            print("\nThat doesn't seem like a valid entry. Please enter a positive integer.\n")
def fonk2(n):
    b2 = (1 + sqrt(5)) / 2
    return int(((1 + sqrt(5))**n - (1 - sqrt(5))**n) / (2**n * sqrt(5)))
def fonk3():
    b3 = argparse.ArgumentParser(description="Calculate Fibonacci sequence value at a given index.")
    b3.add_argument("-i", "--index", b4 = int, help="Index of the Fibonacci sequence")
    b5 = b3.parse_args()
    if b5.index is not None:
        b6 = fonk2(abs(b5.index))
        print(f"Fibonacci sequence value at index {b5.index}: {b6}")
    else:
        b1 = fonk1()
        b6 = fonk2(b1)
        print(f"Fibonacci sequence value at index {b1}: {b6}")
    sys.exit()
if b7 = = "__main__":
    fonk3()