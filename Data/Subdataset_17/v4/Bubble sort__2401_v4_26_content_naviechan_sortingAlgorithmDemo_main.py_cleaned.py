import sys
import argparse
import quickSort
import bubbleSort
import selectionSort
import mergeSort
class_names = {
    'bubble': bubbleSort.BubbleSort,
    'selection': selectionSort.SelectionSort,
    'merge': mergeSort.MergeSort,
    'quick': quickSort.QuickSort
}
def display_list(lst):
    lst_str = [str(i) for i in lst]
    if not lst_str:
        print('| |')
    else:
        output = '|' + ' | '.join(lst_str) + ' |'
        print(output)
    input("Press Enter to continue...")
def main(argv):
    parser = argparse.ArgumentParser(description="Sort a list using the specified algorithm.")
    parser.add_argument("input_list", nargs='+', type=int, help="List of integers separated by space")
    parser.add_argument("alg", type=str, choices=class_names.keys(), help="Sorting algorithm to use: bubble, selection, merge, or quick")
    parser.add_argument("-t", "--trace", action="store_true", help="Print the sorting algorithm step-by-step")
    args = parser.parse_args()
    print('Input:', args.input_list)
    sorting_class = class_names[args.alg]
    sorter = sorting_class(args.input_list, args.trace)
    sorted_list = sorter.sort()
    print('Result:', sorted_list)
if __name__ == '__main__':
    main(sys.argv[1:])