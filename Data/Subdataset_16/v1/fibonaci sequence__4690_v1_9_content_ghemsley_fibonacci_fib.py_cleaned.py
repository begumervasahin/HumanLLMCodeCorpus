import argparse
import math
def fonk1():
    while True:
        try:
            b1 = abs(int(input("Please enter the Fibonacci sequence b8 to find the value of: ")))
            return b1
        except ValueError:
            print("\nThat doesn't seem like a valid entry. Please enter a positive integer.\n")
def fonk2(n):
    if n < 0:
        raise ValueError("Index must be a non-negative integer.")
    b2 = math.sqrt(5)
    b3 = (1 + b2) / 2
    b4 = (1 - b2) / 2
    return int((b3**n - b4**n) / b2 + 0.5)
def fonk3():
    b5 = argparse.ArgumentParser()
    b5.add_argument("-i", "--b8", b6 = "Fibonacci sequence b8 to find the value of", type=int)
    b7 = b5.parse_args()
    if b7.b8 is not None:
        b8 = abs(b7.b8)
    else:
        b8 = fonk1()
    print(f"Fibonacci sequence result: {fonk2(b8)}")
if b9 = = "__main__":
    fonk3()