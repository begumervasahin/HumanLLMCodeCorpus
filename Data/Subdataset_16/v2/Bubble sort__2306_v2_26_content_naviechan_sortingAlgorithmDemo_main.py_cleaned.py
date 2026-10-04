import sys
import argparse
import quickSort
import bubbleSort
import selectionSort
import mergeSort
b1 = {
    'bubble': 'bubbleSort',
    'selection': 'selectionSort',
    'merge': 'mergeSort',
    'quick': 'quickSort'
}
def fonk1(b2):
    b2 = [str(i) for i in b2]
    if len(b2) == 0:
        print('| |')
    else:
        b3 = '|'
        for i in b2:
            b3 += ' ' + i + ' |'
        print(b3)
    input("Press Enter to continue...")
def fonk2(argv):
    b4 = argparse.ArgumentParser(description="Sort a list of integers using the specified algorithm.")
    b4.add_argument("input_list", b5 = '+', b6=int, help="List of integers separated by space")
    b4.add_argument("alg", b6 = str, choices=b1.keys(), help="Sorting algorithm: bubble, selection, merge, or quick")
    b4.add_argument("-t", "--trace", b7 = "store_true", help="Print the sorting algorithm step-by-step")
    b8 = b4.parse_args()
    b9 = b8.trace
    print('Input:', b8.input_list)
    b10 = b1[b8.alg]
    b11 = eval(b10)
    b12 = getattr(b11, b10)
    b13 = b12(b8.input_list, b9)
    b14 = b13.sort()
    print('Result:', b14)
if b15 = = '__main__':
    fonk2(sys.argv[1:])