from math import sqrt
import argparse
__author__ = "PwnEIP"
__copyright__ = "Copyright 2007, The Cogent Project"
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "PwnEIP"
__email__ = "pwneip@gmail.com"
__status__ = "Production"
def main():
    parser = argparse.ArgumentParser(
        description='Generate Fibonacci sequence',
        usage="fibonacci.py [-b] number",
        add_help=True
    )
    parser.add_argument(
        "-b", "--binary",
        action="store_true",
        dest="binary",
        default=False,
        help="Print output in binary"
    )
    parser.add_argument(
        "number",
        type=int,
        help="Generate n length sequence"
    )
    arguments = parser.parse_args()
    output = generate_fibonacci_sequence(arguments.number, arguments.binary)
    print(output)
def generate_fibonacci_sequence(n, binary=False):
    fibonacci_sequence = []
    for x in range(1, n + 1):
        fibonacci_number = calculate_fibonacci(x)
        if binary:
            fibonacci_sequence.append(bin(fibonacci_number)[2:])
        else:
            fibonacci_sequence.append(repr(fibonacci_number))
    return " ".join(fibonacci_sequence)
def calculate_fibonacci(n):
    return int(((1 + sqrt(5)) ** n - (1 - sqrt(5)) ** n) / (2 ** n * sqrt(5)))
if __name__ == '__main__':
    main()