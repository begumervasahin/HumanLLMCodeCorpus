import argparse
from math import sqrt
__author__ = "PwnEIP"
__copyright__ = "Copyright 2007, The Cogent Project"
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "PwnEIP"
__email__ = "pwneip@gmail.com"
__status__ = "Production"
def fibonacci(n):
    phi = (1 + sqrt(5)) / 2
    psi = (1 - sqrt(5)) / 2
    return int((phi**n - psi**n) / sqrt(5))
def main():
    parser = argparse.ArgumentParser(description='Generate Fibonacci sequence')
    parser.add_argument(
        "-b", "--binary",
        action="store_true",
        help="Print output in binary"
    )
    parser.add_argument(
        "number",
        type=int,
        help="Generate n length sequence"
    )
    args = parser.parse_args()
    output = []
    for x in range(1, args.number + 1):
        fib_num = fibonacci(x)
        if args.binary:
            output.append(bin(fib_num)[2:])
        else:
            output.append(str(fib_num))
    print(" ".join(output))
if __name__ == '__main__':
    main()