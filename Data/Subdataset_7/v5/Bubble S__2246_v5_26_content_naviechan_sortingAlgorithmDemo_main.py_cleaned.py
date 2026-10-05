import sys
import argparse
from sorting_algorithms import bubbleSort, selectionSort, mergeSort, quickSort
b1 = {'bubble': 'bubbleSort', 'selection': 'selectionSort', 'merge': 'mergeSort', 'quick': 'quickSort'}
def fonk1(b2):
    b2 = [str(i) for i in b2]
    if not b2:
        print('| |')
    else:
        b3 = '|' + ' | '.join(b2) + ' |'
        print(b3)
    input("Press Enter to continue...")
def fonk2(argv):
    b4 = False
    b5 = argparse.ArgumentParser()
    b5.add_argument("input_list", b6 = '+', b7=int, help="List of integers separated by space")
    b5.add_argument("alg", b7 = str, help="bubble, selection, merge, or quick")
    b5.add_argument("-t", "--trace", b8 = "store_true", help="Print the sorting algorithm step-by-step")
    b9 = b5.parse_args()
    if b9.trace:
        b4 = True
    if b9.alg not in b1:
        print('\nInvalid algorithm name')
        b5.print_help()
        return
    print('Input: ' + str(b9.input_list))
    b10 = b1[b9.alg]
    b11 = getattr(globals()[b10], b10)
    b12 = b11(b9.input_list, b4)
    print('Result: ' + str(b12.sort()))
if b13 = = '__main__':
    fonk2(sys.argv[1:])