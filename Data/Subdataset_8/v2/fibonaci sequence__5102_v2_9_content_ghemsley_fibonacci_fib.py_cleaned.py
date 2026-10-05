import argparse
import sys
from math import sqrt
def get_input():
    fib_index = None
    print("Please enter the index of the Fibonacci sequence to find its value: ")
    try:
        fib_index = abs(int(input()))
    except ValueError:
        print("\nInvalid input. Please enter a positive integer.\n")
        fib_index = get_input()
    return fib_index
def fibonacci(n):
    phi = (1 + sqrt(5)) / 2
    return int((phi**n - (-1/phi)**n) / sqrt(5))
def main():
    parser = argparse.ArgumentParser(description="Calculate Fibonacci sequence value at a given index.")
    parser.add_argument("-i", "--index", type=int, help="Index of the Fibonacci sequence")
    args = parser.parse_args()
    if args.index is not None:
        fib_value = fibonacci(abs(args.index))
        print(f"Fibonacci sequence value at index {args.index}: {fib_value}")
    else:
        fib_index = get_input()
        fib_value = fibonacci(fib_index)
        print(f"Fibonacci sequence value at index {fib_index}: {fib_value}")
if __name__ == "__main__":
    main()