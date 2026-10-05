import argparse
import quickSort
import bubbleSort
import selectionSort
import mergeSort
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
    b4 = False
    b5 = argparse.ArgumentParser()
    b5.add_argument("input_list", b6 = '+', b8=int,
                        b7 = "List of integers separated by space")
    b5.add_argument("alg", b8 = str,
                        b7 = "bubble, selection, merge or quick")
    b5.add_argument("-t", "--trace", b9 = "store_true",
                        b7 = "Print the sorting alg step-by-step")
    b10 = b5.parse_args()
    if b10.trace:
        b4 = True
    if b10.alg not in b1.keys():
        print('\nInvalid algorithm name')
        b5.print_help()
        return
    print('Input: ' + str(b10.input_list))
    b11 = b1[b10.alg]
    b12 = eval(b11 + '.' + b11)
    b12 = b12(b10.input_list, b4)
    print('Result: ' + str(b12.sort()))
if b13 = = '__main__':
    fonk2()