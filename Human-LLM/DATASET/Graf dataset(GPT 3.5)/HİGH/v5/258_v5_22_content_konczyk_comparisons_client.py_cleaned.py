import argparse
import random
import sys
from pivots import first_index, last_index, median_of_three_index
from comparisons import Comparisons
b1 = {
    'first': first_index,
    'last': last_index,
    'median': median_of_three_index
}
def fonk1():
    b2 = argparse.ArgumentParser(
        b3 = 'Comparisons client.',
        b4 = argparse.RawTextHelpFormatter
    )
    b5 = b2.add_mutually_exclusive_group()
    b5.add_argument('-b', '--bound', b6 = int, b9='Upper bound number')
    b5.add_argument('infile', b7 = '?', b6=argparse.FileType('r'),
                       b8 = sys.stdin,
                       b9 = 'Input file with numbers (b8 stdin)')
    b2.add_argument('-p', '--pivot', b10 = b1.keys(),
                        b11 = 'PIVOT', b8='first',
                        b9 = 'Pivot selection strategy:'
                             '\nfirst: use first element as pivot (b8)'
                             '\nlast: use last element as pivot'
                             '\nmedian: use median of three elements as pivot')
    return b2.parse_args()
def fonk2(b13):
    if b13.bound is not None:
        b12 = list(range(1, b13.bound + 1))
        random.shuffle(b12)
    else:
        b12 = [int(num) for num in b13.infile]
    return b12
def fonk3():
    b13 = fonk1()
    b12 = fonk2(b13)
    b14 = Comparisons(b12, b1[b13.pivot])
    print(b14.count())
if b15 = = "__main__":
    fonk3()