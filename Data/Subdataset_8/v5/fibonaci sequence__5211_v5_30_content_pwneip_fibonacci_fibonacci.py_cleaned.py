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
        version="fibonacci.py 1.0",
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
    try:
        arguments = parser.parse_args()
    except IOError as e:
        parser.error(str(e))
    output = generate_fibonacci_sequence(arguments.number, arguments.binary)
    print(output)
def generate_fibonacci_sequence(n, binary=False):
    fibonacci_sequence = [str(calculate_fibonacci(x, binary)) for x in range(1, n + 1)]
    return " ".join(fibonacci_sequence)
def calculate_fibonacci(n, binary=False):
    fibonacci_number = int(((1 + sqrt(5)) ** n - (1 - sqrt(5)) ** n) / (2 ** n * sqrt(5)))
    if binary:
        return bin(fibonacci_number)[2:]
    return fibonacci_number
if __name__ == '__main__':
    main()