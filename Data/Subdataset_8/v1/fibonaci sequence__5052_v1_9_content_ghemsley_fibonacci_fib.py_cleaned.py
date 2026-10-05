import argparse
import sys
from math import sqrt
def get_input():
    fib_num = None
    print("Please enter the Fibonacci sequence index to find the value of: ")
    try:
        fib_num = abs(int(input()))
    except ValueError:
        print("\nThat doesn't seem like a valid entry. Please enter a positive integer.\n")
        fib_num = get_input()
    return fib_num
def fib(n):
    return int(((1 + sqrt(5))**n - (1 - sqrt(5))**n) / (2**n * sqrt(5)))
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--index", help="Fibonacci sequence index to find value of", type=int)
    args = parser.parse_args()
    if args.index is not None:
        print(str(fib(abs(args.index))))
    else:
        print("Fibonacci sequence result:", fib(get_input()))
    sys.exit()
if __name__ == "__main__":
    main()