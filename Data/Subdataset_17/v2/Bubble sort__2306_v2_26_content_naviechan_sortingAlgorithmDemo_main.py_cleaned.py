import sys
import argparse
import quickSort
import bubbleSort
import selectionSort
import mergeSort
class_names = {
    'bubble': 'bubbleSort',
    'selection': 'selectionSort',
    'merge': 'mergeSort',
    'quick': 'quickSort'
}
def display_list(lst):
    lst = [str(i) for i in lst]
    if len(lst) == 0:
        print('| |')
    else:
        output = '|'
        for i in lst:
            output += ' ' + i + ' |'
        print(output)
    input("Press Enter to continue...")
def main(argv):
    parser = argparse.ArgumentParser(description="Sort a list of integers using the specified algorithm.")
    parser.add_argument("input_list", nargs='+', type=int, help="List of integers separated by space")
    parser.add_argument("alg", type=str, choices=class_names.keys(), help="Sorting algorithm: bubble, selection, merge, or quick")
    parser.add_argument("-t", "--trace", action="store_true", help="Print the sorting algorithm step-by-step")
    args = parser.parse_args()
    trace_mode = args.trace
    print('Input:', args.input_list)
    class_name = class_names[args.alg]
    module = eval(class_name)
    sorter_class = getattr(module, class_name)
    sorter = sorter_class(args.input_list, trace_mode)
    result = sorter.sort()
    print('Result:', result)
if __name__ == '__main__':
    main(sys.argv[1:])