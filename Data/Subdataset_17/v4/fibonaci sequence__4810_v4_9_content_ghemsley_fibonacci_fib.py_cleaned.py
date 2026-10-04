import argparse
import math
def get_input():
    while True:
        try:
            index = int(input("Please enter the Fibonacci sequence index to find the value of: "))
            if index >= 0:
                return index
            else:
                print("Error: Index must be a non-negative integer.")
        except ValueError:
            print("Error: Invalid input. Please enter a valid integer.")
def compute_fibonacci(n):
    if n < 0:
        raise ValueError("Index must be a non-negative integer.")
    sqrt_5 = math.sqrt(5)
    phi = (1 + sqrt_5) / 2
    psi = (1 - sqrt_5) / 2
    return int((phi**n - psi**n) / sqrt_5 + 0.5)
def main():
    parser = argparse.ArgumentParser(description="Calculate Fibonacci numbers.")
    parser.add_argument("-i", "--index", type=int, help="Index of the Fibonacci sequence to calculate")
    args = parser.parse_args()
    if args.index is not None:
        index = args.index
    else:
        index = get_input()
    print(f"Fibonacci number at index {index}: {compute_fibonacci(index)}")
if __name__ == "__main__":
    main()