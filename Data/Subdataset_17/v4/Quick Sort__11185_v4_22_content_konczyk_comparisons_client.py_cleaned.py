import argparse
import random
import sys
import pivots
from comparisons import Comparisons
pivots_choice = {
    'first': pivots.first_index,
    'last': pivots.last_index,
    'median': pivots.median_of_three_index
}
parser = argparse.ArgumentParser(
    description='Comparisons client.',
    formatter_class=argparse.RawTextHelpFormatter
)
group = parser.add_mutually_exclusive_group()
group.add_argument(
    '-b', '--bound',
    type=int,
    help='Upper bound number'
)
group.add_argument(
    'infile',
    nargs='?',
    type=argparse.FileType('r'),
    default=sys.stdin,
    help='Input file with numbers (default stdin)'
)
parser.add_argument(
    '-p', '--pivot',
    choices=pivots_choice.keys(),
    metavar='PIVOT',
    default='first',
    help='first: use first element as a pivot (default)\n'
         'last: use last element as a pivot\n'
         'median: use median of three elements as a pivot'
)
args = parser.parse_args()
if args.bound is not None:
    nums = list(range(1, args.bound + 1))
    random.shuffle(nums)
else:
    nums = [int(num) for num in args.infile]
comp = Comparisons(nums, pivots_choice[args.pivot])
print(comp.count())