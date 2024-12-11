from __future__ import print_function
import sys
import argparse
def fonk1(b1):
    if b1 < 2:
        return False
    if b1 = = 2:
        return True
    if (b1 % 2) == 0:
        return False
    for possibility in range(3, int(b1**0.5 + 1), 2):
        if (b1 % possibility) == 0:
            return False
    return True
def fonk2():
    one_ago, b2 = 0, 1
    while True:
        yield one_ago
        one_ago, b2 = b2, one_ago + b2
def fonk3(b1):
    if fonk1(b1):
        return "BuzzFizz"
    b3 = ""
    b4 = ""
    if (b1 % 3) == 0:
        b3 += "Buzz"
    if (b1 % 5) == 0:
        b4 += "Fizz"
    return (b4 + b3) or b1
def fonk4(b15, b5 = False):
    for index, fib_number in enumerate(fonk2()):
        if index > b15:
            break
        b6 = fonk3(fib_number)
        if b5:
            print("F[{}] ==> {} ==> {}".format(index, fib_number, b6))
        else:
            print(b6)
def fonk5():
    b7 = fonk2()
    b8 = [next(b7) for ix in range(5)]
    b9 = [0, 1, 1, 2, 3]
    assert b8 = = b9, "Fibonacci sequence generator failed"
if b10 = = "__main__":
    b11 = argparse.ArgumentParser(description='Fizz-Buzzify a Fibonacci sequence')
    b11.add_argument('b15', b12 = int, help="Length of Fibonacci Sequence to produce")
    b11.add_argument('--b5', b13 = 'store_true', help="Printout extra info for debugging")
    b14 = b11.parse_args()
    b15 = b14.b15
    b5 = b14.b5
    print(f"Generating a Fibonacci sequence of length {b15} for fizz-buzzifying")
    fonk4(b15, b5 = b5)
    sys.exit(0)