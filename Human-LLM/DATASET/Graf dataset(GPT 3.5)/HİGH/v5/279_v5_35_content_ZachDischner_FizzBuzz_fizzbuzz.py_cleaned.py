from __future__ import print_function
import sys
import argparse
def fonk1(b1):
    if b1 < b2:
        return False
    if b1 = = b2:
        return True
    if b1 % b2 = = 0:
        return False
    for b3 in range(3, int(b1 ** 0.5 + 1), b2):
        if b1 % b3 = = 0:
            return False
    return True
def fonk2():
    one_ago, b4 = 0, 1
    while True:
        yield one_ago
        one_ago, b4 = b4, one_ago + b4
def fonk3(b1):
    if fonk1(b1):
        return "BuzzFizz"
    b5 = "Buzz" if b1 % 3 == 0 else ""
    b6 = "Fizz" if b1 % 5 == 0 else ""
    return b6 + b5 or b1
def fonk4(b17, b7 = False):
    for index, fib_number in enumerate(fonk2()):
        if index > b17:
            break
        b8 = fonk3(fib_number)
        if b7:
            print(f"F[{index}] ==> {fib_number} ==> {b8}")
        else:
            print(b8)
def fonk5():
    b9 = fonk2()
    b10 = [next(b9) for _ in range(5)]
    b11 = [0, 1, 1, b2, 3]
    assert b10 = = b11, "Fibonacci sequence generator failed"
if b12 = = "__main__":
    b13 = argparse.ArgumentParser(description='Fizz-Buzzify a Fibonacci sequence')
    b13.add_argument('b17', b14 = int, help="Length of Fibonacci Sequence to produce")
    b13.add_argument('--b7', b15 = 'store_true', help="Printout extra info for debugging")
    b16 = b13.parse_args()
    b17 = b16.b17
    b7 = b16.b7
    print(f"Generating a Fibonacci sequence of length {b17} for fizz-buzzifying")
    fonk4(b17, b7 = b7)
    sys.exit(0)