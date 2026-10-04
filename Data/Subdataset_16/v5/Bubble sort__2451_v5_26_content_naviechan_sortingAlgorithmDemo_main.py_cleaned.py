import sys
import argparse
import quickSort
import bubbleSort
import selectionSort
import mergeSort
b1 = {
    'bubble': bubbleSort.BubbleSort,
    'selection': selectionSort.SelectionSort,
    'merge': mergeSort.MergeSort,
    'quick': quickSort.QuickSort
}
def fonk1(lst):
    b2 = [str(i) for i in lst]
    if not b2:
        print('| |')
    else:
        b3 = '|' + ' | '.join(b2) + ' |'
        print(b3)
    input("Press Enter to continue...")
def fonk2(argv):
    b4 = argparse.ArgumentParser(description="Sort a list using the specified algorithm.")
    b4.add_argument("input_list", b5 = '+', b6=int, help="List of integers separated by space")
    b4.add_argument("alg", b6 = str, choices=b1.keys(), help="Sorting algorithm to use: bubble, selection, merge, or quick")
    b4.add_argument("-t", "--trace", b7 = "store_true", help="Print the sorting algorithm step-by-step")
    b8 = b4.parse_args()
    print('Input:', b8.input_list)
    b9 = b1[b8.alg]
    b10 = b9(b8.input_list, b8.trace)
    b11 = b10.sort()
    print('Result:', b11)
if b12 = = '__main__':
    fonk2(sys.argv[1:])