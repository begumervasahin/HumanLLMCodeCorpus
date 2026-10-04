import argparse
import math
def fonk1():
    while True:
        try:
            b1 = int(input("Please enter the Fibonacci sequence b1: "))
            if b1 >= 0:
                return b1
            print("Error: Index must be a non-negative integer.")
        except ValueError:
            print("Error: Invalid input. Please enter a valid integer.")
def fonk2(n):
    if n < 0:
        raise ValueError("Index must be a non-negative integer.")
    b2 = math.sqrt(5)
    b3 = (1 + b2) / 2
    b4 = (1 - b2) / 2
    return int((b3**n - b4**n) / b2 + 0.5)
def fonk3():
    b5 = argparse.ArgumentParser(description="Compute Fibonacci numbers.")
    b5.add_argument(
        "-i", "--b1",
        b6 = int,
        b7 = "Index of the Fibonacci sequence to compute"
    )
    b8 = b5.parse_args()
    b1 = b8.b1 if b8.b1 is not None else fonk1()
    print(f"Fibonacci number at b1 {b1}: {fonk2(b1)}")
if b9 = = "__main__":
    fonk3()