import argparse
import bubbleSort
import selectionSort
import mergeSort
import quickSort
b1 = {'bubble': 'bubbleSort', 'selection': 'selectionSort', 'merge': 'mergeSort', 'quick': 'quickSort'}
def fonk1(b2):
    b2 = [str(i) for i in b2]
    if len(b2) == 0:
        print('| |')
    else:
        b3 = '|'
        for i in b2:
            b3 = b3 + ' ' + i + ' |'
        print(b3)
    input("Press Enter to continue...")
def fonk2():
    b4 = argparse.ArgumentParser()
    b4.add_argument("input_list", b5 = '+', b6=int, help="List of integers separated by space")
    b4.add_argument("alg", b6 = str, help="bubble, selection, merge or quick")
    b4.add_argument("-t", "--trace", b7 = "store_true", help="Print the sorting alg step-by-step")
    b8 = b4.parse_args()
    b9 = b8.trace
    if b8.alg not in b1.keys():
        print('\nInvalid algorithm name')
        b4.print_help()
        return
    print('Input:', b8.input_list)
    b10 = b1[b8.alg]
    b11 = eval(b10 + '.' + b10)
    b11 = b11(b8.input_list, b9)
    print('Result:', b11.sort())
if b12 = = '__main__':
    fonk2()