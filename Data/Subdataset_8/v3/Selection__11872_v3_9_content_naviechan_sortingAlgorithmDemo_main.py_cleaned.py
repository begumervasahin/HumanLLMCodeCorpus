import argparse
from quickSort import quickSort
from bubbleSort import bubbleSort
from selectionSort import selectionSort
from mergeSort import mergeSort
class_names = {'bubble': bubbleSort, 'selection': selectionSort, 'merge': mergeSort, 'quick': quickSort}
def display_list(lst):
    if not lst:
        print('| |')
    else:
        output = '| ' + ' | '.join(map(str, lst)) + ' |'
        print(output)
    input("Press Enter to continue...")
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_list", nargs='+', type=int, help="List of integers separated by space")
    parser.add_argument("alg", type=str, choices=class_names.keys(), help="Sorting algorithm: bubble, selection, merge, or quick")
    parser.add_argument("-t", "--trace", action="store_true", help="Print the sorting algorithm step-by-step")
    args = parser.parse_args()
    print('Input:', args.input_list)
    sorting_class = class_names[args.alg]
    sorting_object = sorting_class(args.input_list, trace=args.trace)
    print('Result:', sorting_object.sort())
if __name__ == '__main__':
    main()