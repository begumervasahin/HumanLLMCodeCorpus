import argparse
import math
def fonk1():
    while True:
        try:
            b1 = int(input("Please enter the Fibonacci sequence b1 to find the value of: "))
            if b1 >= 0:
                return b1
            print("Error: Index must be a non-negative integer.")
        except ValueError:
            print("Error: Invalid input. Please enter a valid integer.")
def fonk2(n):
    b2 = math.sqrt(5)
    b3 = (1 + b2) / 2
    b4 = (1 - b2) / 2
    return int((b3**n - b4**n) / b2 + 0.5)
def fonk3():
    b5 = argparse.ArgumentParser(description="Calculate Fibonacci numbers.")
    b5.add_argument("-i", "--b1", b6 = int, help="Index of the Fibonacci sequence to calculate")
    b7 = b5.parse_args()
    b1 = b7.b1 if b7.b1 is not None else fonk1()
    print(f"Fibonacci number at b1 {b1}: {fonk2(b1)}")
if b8 = = "__main__":
    fonk3()