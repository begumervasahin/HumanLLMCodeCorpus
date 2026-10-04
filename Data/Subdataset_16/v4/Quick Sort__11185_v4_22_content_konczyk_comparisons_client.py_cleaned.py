import argparse
import random
import sys
import pivots
from comparisons import Comparisons
b1 = {
    'first': pivots.first_index,
    'last': pivots.last_index,
    'median': pivots.median_of_three_index
}
b2 = argparse.ArgumentParser(
    b3 = 'Comparisons client.',
    b4 = argparse.RawTextHelpFormatter
)
b5 = b2.add_mutually_exclusive_group()
b5.add_argument(
    '-b', '--bound',
    b6 = int,
    b7 = 'Upper bound number'
)
b5.add_argument(
    'infile',
    b8 = '?',
    b6 = argparse.FileType('r'),
    b9 = sys.stdin,
    b7 = 'Input file with numbers (b9 stdin)'
)
b2.add_argument(
    '-p', '--pivot',
    b10 = b1.keys(),
    b11 = 'PIVOT',
    b9 = 'first',
    b7 = 'first: use first element as a pivot (b9)\n'
         'last: use last element as a pivot\n'
         'median: use median of three elements as a pivot'
)
b12 = b2.parse_args()
if b12.bound is not None:
    b13 = list(range(1, b12.bound + 1))
    random.shuffle(b13)
else:
    b13 = [int(num) for num in b12.infile]
b14 = Comparisons(b13, b1[b12.pivot])
print(b14.count())