import argparse
import math
def get_input():
    while True:
        try:
            fib_num = abs(int(input("Please enter the Fibonacci sequence index to find the value of: ")))
            return fib_num
        except ValueError:
            print("\nThat doesn't seem like a valid entry. Please enter a positive integer.\n")
def fib(n):
    if n < 0:
        raise ValueError("Index must be a non-negative integer.")
    sqrt_5 = math.sqrt(5)
    phi = (1 + sqrt_5) / 2
    psi = (1 - sqrt_5) / 2
    return int((phi**n - psi**n) / sqrt_5 + 0.5)
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--index", help="Fibonacci sequence index to find the value of", type=int)
    args = parser.parse_args()
    if args.index is not None:
        index = abs(args.index)
    else:
        index = get_input()
    print(f"Fibonacci sequence result: {fib(index)}")
if __name__ == "__main__":
    main()