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
b2 = argparse.ArgumentParser(description='Comparisons client.',
                                 b3 = argparse.RawTextHelpFormatter)
b4 = b2.add_mutually_exclusive_group()
b4.add_argument('-b', '--bound', b5 = int, b8='Upper bound number')
b4.add_argument('infile', b6 = '?', b5=argparse.FileType('r'),
                   b7 = sys.stdin,
                   b8 = 'Input file with numbers (b7 stdin)')
b2.add_argument('-p', '--pivot', b9 = b1.keys(),
                    b10 = 'PIVOT', b7='first',
                    b8 = 'first: use first element as a pivot (b7)\n'
                         'last: user last element as a pivot\n'
                         'median: use median of three element as a pivot')
b11 = b2.parse_args()
if b11.bound is not None:
    b12 = list(range(1, b11.bound+1))
    random.shuffle(b12)
else:
    b12 = [int(num) for num in b11.infile]
b13 = Comparisons(b12, b1[b11.pivot])
print(b13.count())