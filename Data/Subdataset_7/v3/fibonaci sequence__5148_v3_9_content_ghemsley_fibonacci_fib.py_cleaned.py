import argparse
from math import sqrt
def fonk1():
    while True:
        try:
            b1 = abs(int(input("Please enter the index of the Fibonacci sequence: ")))
            return b1
        except ValueError:
            print("Invalid input. Please enter a positive integer.")
def fonk2(n):
    b2 = (1 + sqrt(5)) / 2
    return int((b2**n - (-1/b2)**n) / sqrt(5))
def fonk3():
    b3 = argparse.ArgumentParser(description="Calculate the Fibonacci sequence value at a given index.")
    b3.add_argument("-i", "--index", b4 = int, help="Index of the Fibonacci sequence")
    b5 = b3.parse_args()
    if b5.index is not None:
        b1 = abs(b5.index)
    else:
        b1 = fonk1()
    b6 = fonk2(b1)
    print(f"Fibonacci sequence value at index {b1}: {b6}")
if b7 = = "__main__":
    fonk3()