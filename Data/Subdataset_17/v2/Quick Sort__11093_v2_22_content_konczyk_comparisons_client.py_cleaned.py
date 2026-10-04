import argparse
import random
import sys
from comparisons import Comparisons
import pivots
PIVOTS = {
    'first': pivots.first_index,
    'last': pivots.last_index,
    'median': pivots.median_of_three_index
}
def parse_arguments():
    parser = argparse.ArgumentParser(
        description='Client to compare pivot functions.',
        formatter_class=argparse.RawTextHelpFormatter
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-b', '--bound', type=int, help='Upper bound for number generation')
    group.add_argument('infile', nargs='?', type=argparse.FileType('r'), default=sys.stdin, help='Input file with numbers (default: stdin)')
    parser.add_argument(
        '-p', '--pivot',
        choices=PIVOTS.keys(),
        metavar='PIVOT',
        default='first',
        help='Choose pivot:\n'
             'first: use first element as pivot (default)\n'
             'last: use last element as pivot\n'
             'median: use median of three elements as pivot'
    )
    return parser.parse_args()
def generate_numbers(bound):
    numbers = list(range(1, bound + 1))
    random.shuffle(numbers)
    return numbers
def read_numbers_from_file(file):
    return [int(num) for num in file]
def main():
    args = parse_arguments()
    if args.bound is not None:
        numbers = generate_numbers(args.bound)
    else:
        numbers = read_numbers_from_file(args.infile)
    pivot_function = PIVOTS[args.pivot]
    comparisons = Comparisons(numbers, pivot_function)
    print(comparisons.count())
if __name__ == "__main__":
    main()