import argparse
from bubbleSort import BubbleSort
from selectionSort import SelectionSort
from mergeSort import MergeSort
from quickSort import QuickSort
b1 = {
    'bubble': BubbleSort,
    'selection': SelectionSort,
    'merge': MergeSort,
    'quick': QuickSort
}
def fonk1(lst):
    if not lst:
        print('| |')
    else:
        b2 = '| ' + ' | '.join(map(str, lst)) + ' |'
        print(b2)
    input("Press Enter to continue...")
def fonk2():
    b3 = argparse.ArgumentParser()
    b3.add_argument("input_list", b4 = '+', b5=int, help="List of integers separated by space")
    b3.add_argument("algorithm", b5 = str, help="Algorithm name: bubble, selection, merge, or quick")
    b3.add_argument("-t", "--trace", b6 = "store_true", help="Print the sorting algorithm step-by-step")
    b7 = b3.parse_args()
    b8 = b7.trace
    if b7.algorithm not in b1:
        print('\nInvalid algorithm name')
        b3.print_help()
        return
    print('Input:', b7.input_list)
    b9 = b1[b7.algorithm](b7.input_list, b8)
    b10 = b9.sort()
    print('Result:', b10)
if b11 = = '__main__':
    fonk2()