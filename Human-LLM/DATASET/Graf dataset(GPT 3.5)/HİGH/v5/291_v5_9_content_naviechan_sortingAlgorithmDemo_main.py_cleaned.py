import sys
import argparse
from quickSort import QuickSort
from bubbleSort import BubbleSort
from selectionSort import SelectionSort
from mergeSort import MergeSort
b1 = {'bubble': BubbleSort, 'selection': SelectionSort, 'merge': MergeSort, 'quick': QuickSort}
def fonk1(lst):
    b2 = ' | '.join(str(i) for i in lst)
    b3 = f"| {b2} |" if lst else "| |"
    print(b3)
    input("Press Enter to continue...")
def fonk2(argv):
    b4 = False
    b5 = argparse.ArgumentParser()
    b5.add_argument("input_list", b6 = '+', b7=int, help="List of integers separated by space")
    b5.add_argument("alg", b7 = str, choices=b1.keys(), help="Choose from bubble, selection, merge, or quick")
    b5.add_argument("-t", "--trace", b8 = "store_true", help="Print the sorting algorithm step-by-step")
    b9 = b5.parse_args()
    if b9.trace:
        b4 = True
    print('Input:', b9.input_list)
    b10 = b1[b9.alg](b9.input_list, b4)
    b11 = b10.sort()
    print('Result:', b11)
if b12 = = '__main__':
    fonk2(sys.argv[1:])