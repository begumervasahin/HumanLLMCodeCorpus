import sys
import argparse
import importlib
b1 = {
    'bubble': 'bubbleSort',
    'selection': 'selectionSort',
    'merge': 'mergeSort',
    'quick': 'quickSort'
}
def fonk1(lst):
    b2 = '| ' + ' | '.join(map(str, lst)) + ' |'
    print(b2 if lst else '| |')
    input("Press Enter to continue...")
def fonk2():
    b3 = argparse.ArgumentParser(description="Sort a list of integers using the specified algorithm.")
    b3.add_argument("input_list", b4 = '+', b5=int, help="List of integers separated by space")
    b3.add_argument("alg", b5 = str, choices=b1.keys(), help="Sorting algorithm: bubble, selection, merge, or quick")
    b3.add_argument("-t", "--trace", b6 = "store_true", help="Print the sorting algorithm step-by-step")
    return b3.parse_args()
def fonk3(argv):
    b7 = fonk2()
    print('Input:', b7.input_list)
    b8 = b1[b7.alg]
    b9 = importlib.import_module(b8)
    b10 = getattr(b9, b8)
    b11 = b10(b7.input_list, b7.trace)
    b12 = b11.sort()
    print('Result:', b12)
if b13 = = '__main__':
    fonk3(sys.argv[1:])