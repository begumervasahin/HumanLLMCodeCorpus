import argparse
import random
import sys
import pivots
from comparisons import Comparisons
def fonk1():
    b1 = argparse.ArgumentParser(
        b2 = 'Comparisons client.',
        b3 = argparse.RawTextHelpFormatter
    )
    b4 = b1.add_mutually_exclusive_group()
    b4.add_argument(
        '-b', '--bound',
        b5 = int,
        b6 = 'Upper bound number'
    )
    b4.add_argument(
        'infile',
        b7 = '?',
        b5 = argparse.FileType('r'),
        b8 = sys.stdin,
        b6 = 'Input file with numbers (b8 stdin)'
    )
    b1.add_argument(
        '-p', '--pivot',
        b9 = b15.keys(),
        b10 = 'PIVOT',
        b8 = 'first',
        b6 = 'first: use first element as a pivot (b8)\n'
             'last: use last element as a pivot\n'
             'median: use median of three elements as a pivot'
    )
    return b1
def fonk2(b12):
    if b12.bound is not None:
        b11 = list(range(1, b12.bound + 1))
        random.shuffle(b11)
    else:
        b11 = [int(num) for num in b12.infile]
    return b11
def fonk3():
    b1 = fonk1()
    b12 = b1.parse_args()
    b11 = fonk2(b12)
    b13 = Comparisons(b11, b15[b12.pivot])
    print(b13.count())
if b14 = = "__main__":
    b15 = {
        'first': pivots.first_index,
        'last': pivots.last_index,
        'median': pivots.median_of_three_index
    }
    fonk3()