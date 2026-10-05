import argparse
import sys
from math import sqrt
def get_fibonacci_index():
    while True:
        try:
            fibonacci_index = abs(int(input("Please enter the index of the Fibonacci sequence to find its value: ")))
            return fibonacci_index
        except ValueError:
            print("\nThat doesn't seem like a valid entry. Please enter a positive integer.\n")
def fibonacci(n):
    phi = (1 + sqrt(5)) / 2
    return int(((1 + sqrt(5))**n - (1 - sqrt(5))**n) / (2**n * sqrt(5)))
def main():
    parser = argparse.ArgumentParser(description="Calculate Fibonacci sequence value at a given index.")
    parser.add_argument("-i", "--index", type=int, help="Index of the Fibonacci sequence")
    args = parser.parse_args()
    if args.index is not None:
        fibonacci_result = fibonacci(abs(args.index))
        print(f"Fibonacci sequence value at index {args.index}: {fibonacci_result}")
    else:
        fibonacci_index = get_fibonacci_index()
        fibonacci_result = fibonacci(fibonacci_index)
        print(f"Fibonacci sequence value at index {fibonacci_index}: {fibonacci_result}")
    sys.exit()
if __name__ == "__main__":
    main()