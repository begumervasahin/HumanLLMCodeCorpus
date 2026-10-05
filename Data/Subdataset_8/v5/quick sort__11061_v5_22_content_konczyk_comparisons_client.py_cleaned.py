import argparse
import random
import sys
from pivots import first_index, last_index, median_of_three_index
from comparisons import Comparisons
PIVOTS = {
    'first': first_index,
    'last': last_index,
    'median': median_of_three_index
}
def parse_arguments():
    parser = argparse.ArgumentParser(
        description='Comparisons client.',
        formatter_class=argparse.RawTextHelpFormatter
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-b', '--bound', type=int, help='Upper bound number')
    group.add_argument('infile', nargs='?', type=argparse.FileType('r'),
                       default=sys.stdin,
                       help='Input file with numbers (default stdin)')
    parser.add_argument('-p', '--pivot', choices=PIVOTS.keys(),
                        metavar='PIVOT', default='first',
                        help='Pivot selection strategy:'
                             '\nfirst: use first element as pivot (default)'
                             '\nlast: use last element as pivot'
                             '\nmedian: use median of three elements as pivot')
    return parser.parse_args()
def generate_numbers(args):
    if args.bound is not None:
        nums = list(range(1, args.bound + 1))
        random.shuffle(nums)
    else:
        nums = [int(num) for num in args.infile]
    return nums
def main():
    args = parse_arguments()
    nums = generate_numbers(args)
    comp = Comparisons(nums, PIVOTS[args.pivot])
    print(comp.count())
if __name__ == "__main__":
    main()