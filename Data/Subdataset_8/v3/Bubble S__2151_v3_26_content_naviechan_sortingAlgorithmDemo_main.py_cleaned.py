import argparse
from bubbleSort import BubbleSort
from selectionSort import SelectionSort
from mergeSort import MergeSort
from quickSort import QuickSort
SORT_ALGORITHMS = {
    'bubble': BubbleSort,
    'selection': SelectionSort,
    'merge': MergeSort,
    'quick': QuickSort
}
def display_list(lst):
    if not lst:
        print('| |')
    else:
        formatted_list = '| ' + ' | '.join(map(str, lst)) + ' |'
        print(formatted_list)
    input("Press Enter to continue...")
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_list", nargs='+', type=int, help="List of integers separated by space")
    parser.add_argument("algorithm", type=str, help="Algorithm name: bubble, selection, merge, or quick")
    parser.add_argument("-t", "--trace", action="store_true", help="Print the sorting algorithm step-by-step")
    args = parser.parse_args()
    trace_mode = args.trace
    if args.algorithm not in SORT_ALGORITHMS:
        print('\nInvalid algorithm name')
        parser.print_help()
        return
    print('Input:', args.input_list)
    sorting_algorithm = SORT_ALGORITHMS[args.algorithm](args.input_list, trace_mode)
    result = sorting_algorithm.sort()
    print('Result:', result)
if __name__ == '__main__':
    main()