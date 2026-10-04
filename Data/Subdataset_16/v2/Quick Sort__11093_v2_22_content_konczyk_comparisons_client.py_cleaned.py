import argparse
import random
import sys
from b15 import Comparisons
import pivots
b1 = {
    'first': pivots.first_index,
    'last': pivots.last_index,
    'median': pivots.median_of_three_index
}
def fonk1():
    b2 = argparse.ArgumentParser(
        b3 = 'Client to compare pivot functions.',
        b4 = argparse.RawTextHelpFormatter
    )
    b5 = b2.add_mutually_exclusive_group()
    b5.add_argument('-b', '--bound', b6 = int, b11='Upper bound for number generation')
    b5.add_argument('infile', b7 = '?', b6=argparse.FileType('r'), b10=sys.stdin, b11='Input file with b12 (b10: stdin)')
    b2.add_argument(
        '-p', '--pivot',
        b8 = b1.keys(),
        b9 = 'PIVOT',
        b10 = 'first',
        b11 = 'Choose pivot:\n'
             'first: use first element as pivot (b10)\n'
             'last: use last element as pivot\n'
             'median: use median of three elements as pivot'
    )
    return b2.parse_args()
def fonk2(bound):
    b12 = list(range(1, bound + 1))
    random.shuffle(b12)
    return b12
def fonk3(file):
    return [int(num) for num in file]
def fonk4():
    b13 = fonk1()
    if b13.bound is not None:
        b12 = fonk2(b13.bound)
    else:
        b12 = fonk3(b13.infile)
    b14 = b1[b13.pivot]
    b15 = Comparisons(b12, b14)
    print(b15.count())
if b16 = = "__main__":
    fonk4()