import argparse
from quickSort import quickSort
from bubbleSort import bubbleSort
from selectionSort import selectionSort
from mergeSort import mergeSort
b1 = {'bubble': bubbleSort, 'selection': selectionSort, 'merge': mergeSort, 'quick': quickSort}
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
    b3.add_argument("alg", b5 = str, choices=b1.keys(), help="Sorting algorithm: bubble, selection, merge, or quick")
    b3.add_argument("-t", "--trace", b6 = "store_true", help="Print the sorting algorithm step-by-step")
    b7 = b3.parse_args()
    print('Input:', b7.input_list)
    b8 = b1[b7.alg]
    b9 = b8(b7.input_list, trace=b7.trace)
    print('Result:', b9.sort())
if b10 = = '__main__':
    fonk2()