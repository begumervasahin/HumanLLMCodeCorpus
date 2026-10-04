import argparse
import math
import os
def swap(arr, index_1, index_2):
    arr[index_1], arr[index_2] = arr[index_2], arr[index_1]
def bubble_sort(arr, log):
    n = 0
    not_done = True
    while not_done:
        not_done = False
        for i in range(len(arr) - 1 - n):
            os.write(log, f'{i} {i + 1} {n}\n'.encode())
            if arr[i] > arr[i + 1]:
                os.write(log, f'{i} {i + 1} {n} s\n'.encode())
                swap(arr, i, i + 1)
                not_done = True
                print(*arr)
        n += 1
def insertion_sort(arr, log):
    def check_back_insertion(arr, log, i):
        for j in range(i, -1, -1):
            os.write(log, f'{j} {i + 1}\n'.encode())
            if j > 0 and arr[i + 1] >= arr[j - 1]:
                os.write(log, f'{j} {i + 1} s\n'.encode())
                arr.insert(j, arr.pop(i + 1))
                break
            elif j == 0:
                os.write(log, f'{0} {i + 1} s\n'.encode())
                arr.insert(0, arr.pop(i + 1))
        print(*arr)
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            check_back_insertion(arr, log, i)
        else:
            os.write(log, f'{i} {i + 1}\n'.encode())
def merge_sort_out_place(arr):
    if len(arr) > 2:
        mid = len(arr)
        left_sorted = merge_sort_out_place(arr[:mid])
        right_sorted = merge_sort_out_place(arr[mid:])
        result = merge(left_sorted, right_sorted)
        print(*result)
        return result
    elif len(arr) == 2:
        if arr[0] > arr[1]:
            swap(arr, 0, 1)
        print(*arr)
        return arr
def merge(arr, left, right, log):
    def arrange_sorted_lists():
        i, j = left, center
        os.write(log, f'{left} {right} {center}\n'.encode())
        while i < j and j <= right:
            os.write(log, f'{left} {right} '.encode())
            if arr[i] > arr[j]:
                os.write(log, f'{i} {j} s\n'.encode())
                arr.insert(i, arr.pop(j))
                i += 1
                j += 1
            else:
                os.write(log, f'{i} {i} s\n'.encode())
                i += 1
        print(*arr[left:right + 1])
    center = math.ceil((right + left) / 2)
    if right - left > 1:
        merge(arr, left, center - 1, log)
        merge(arr, center, right, log)
        arrange_sorted_lists()
    elif right - left == 1:
        arrange_sorted_lists()
    else:
        os.write(log, f'{left} {right}\n'.encode())
def quick_sort(arr, left, right, log):
    def partition(i, pivot):
        for j in range(left, right):
            os.write(log, f'{left} {right} {i} {j}\n'.encode())
            if arr[j] < pivot:
                i += 1
                os.write(log, f'{left} {right} {i} {j} s\n'.encode())
                swap(arr, i, j)
        i += 1
        os.write(log, f'{left} {right} {i} {right} s\n'.encode())
        return i
    if left < right:
        i = left - 1
        pivot = arr[right]
        i = partition(i, pivot)
        swap(arr, i, right)
        print("P:", pivot)
        print(*arr)
        quick_sort(arr, left, i - 1, log)
        quick_sort(arr, i + 1, right, log)
def heap_sort(arr):
    def heapify(i, n):
        max_i = i
        left, right = 2 * i + 1, 2 * i + 2
        if left < n and arr[max_i] < arr[left]:
            max_i = left
        if right < n and arr[max_i] < arr[right]:
            max_i = right
        if i != max_i:
            swap(arr, i, max_i)
            heapify(max_i, n)
    n = len(arr)
    for i in range(n
        heapify(i, n)
    for i in range(n - 1, 0, -1):
        swap(arr, i, 0)
        heapify(0, i)
    print(*arr)
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('decks', type=int, nargs='+', help="List of integers to sort")
    parser.add_argument("--algo", type=str, default="bubble", help="Algorithm to use for sorting")
    parser.add_argument("--gui", action="store_true", help="GUI mode")
    args = parser.parse_args()
    if len(args.decks) > 1:
        try:
            os.unlink("log")
        except FileNotFoundError:
            pass
        log = os.open("log", os.O_RDWR | os.O_CREAT)
        os.write(log, ' '.join(map(str, args.decks)).encode() + b'\n')
        os.write(log, args.algo.encode() + b'\n')
        if args.algo == "bubble":
            bubble_sort(args.decks, log)
        elif args.algo == "insert":
            insertion_sort(args.decks, log)
        elif args.algo == "merge":
            merge(args.decks, 0, len(args.decks) - 1, log)
        elif args.algo == "quick":
            quick_sort(args.decks, 0, len(args.decks) - 1, log)
        elif args.algo == "heap":
            heap_sort(args.decks)
        os.close(log)
        if args.gui:
            import sorting_gui
            sorting_gui.main()
if __name__ == "__main__":
    main()