import argparse
import os
def swap(arr, index_1, index_2):
    arr[index_1], arr[index_2] = arr[index_2], arr[index_1]
def bubble_sort(decks, log):
    n = 0
    not_done = True
    while not_done:
        not_done = False
        for i in range(len(decks) - 1 - n):
            os.write(log, f'{i} {i+1} {n}\n'.encode())
            if decks[i] > decks[i + 1]:
                os.write(log, f'{i} {i+1} {n} s\n'.encode())
                swap(decks, i, i + 1)
                not_done = True
                print(*decks)
        n += 1
def insertion_sort(decks, log):
    def check_back_insertion(decks, log, i):
        for j in range(i, -1, -1):
            os.write(log, f'{j} {i+1}\n'.encode())
            if j > 0 and decks[i + 1] >= decks[j - 1]:
                os.write(log, f'{j} {i+1} s\n'.encode())
                decks.insert(j, decks.pop(i + 1))
                break
            elif j == 0:
                os.write(log, f'{0} {i+1} s\n'.encode())
                decks.insert(0, decks.pop(i + 1))
        print(*decks)
    for i in range(len(decks) - 1):
        if decks[i] > decks[i + 1]:
            check_back_insertion(decks, log, i)
        else:
            os.write(log, f'{i} {i+1}\n'.encode())
def merge_sort(decks):
    if len(decks) <= 1:
        return decks
    middle_index = len(decks)
    left_split = merge_sort(decks[:middle_index])
    right_split = merge_sort(decks[middle_index:])
    return merge(left_split, right_split)
def merge(left, right):
    result = []
    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result.extend(left)
    result.extend(right)
    return result
def merge_sort_in_place(decks, left, right, log):
    def arrange_2_sorted_lists():
        i, j = left, center
        os.write(log, f'{left} {right} {center}\n'.encode())
        while i < j and j <= right:
            if decks[i] > decks[j]:
                os.write(log, f'{i} {j} s\n'.encode())
                decks.insert(i, decks.pop(j))
                i += 1
                j += 1
            else:
                os.write(log, f'{i} {i} s\n'.encode())
                i += 1
        print(*decks[left:right + 1])
    if right - left > 1:
        center = (right + left)
        merge_sort_in_place(decks, left, center - 1, log)
        merge_sort_in_place(decks, center, right, log)
        arrange_2_sorted_lists()
    elif right - left == 1:
        arrange_2_sorted_lists()
    else:
        os.write(log, f'{left} {right}\n'.encode())
def quick_sort(decks, left, right, log):
    def partition(i, pivot):
        for j in range(left, right):
            if decks[j] < pivot:
                i += 1
                swap(decks, i, j)
        return i
    if left < right:
        pivot_index = partition(left - 1, decks[right])
        swap(decks, pivot_index + 1, right)
        quick_sort(decks, left, pivot_index, log)
        quick_sort(decks, pivot_index + 2, right, log)
def heap_sort(decks, n):
    def heapify(i, n):
        max_i = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and decks[left] > decks[max_i]:
            max_i = left
        if right < n and decks[right] > decks[max_i]:
            max_i = right
        if max_i != i:
            swap(decks, i, max_i)
            heapify(max_i, n)
    for i in range(n
        heapify(i, n)
    for i in range(n - 1, 0, -1):
        swap(decks, i, 0)
        heapify(0, i)
    print(decks)
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('decks', type=int, nargs='+', help="List of integers to be sorted.")
    parser.add_argument("--algo", type=str, default="bubble", help="Sorting algorithm to use.")
    parser.add_argument("--gui", action="store_true", help="Enable GUI mode.")
    args = parser.parse_args()
    if len(args.decks) > 1:
        log_file = "log"
        try:
            os.unlink(log_file)
        except Exception:
            pass
        log = os.open(log_file, os.O_RDWR | os.O_CREAT)
        os.write(log, ' '.join(map(str, args.decks)).encode() + b'\n')
        os.write(log, args.algo.encode() + b'\n')
        if args.algo == "bubble":
            bubble_sort(args.decks, log)
        elif args.algo == "insert":
            insertion_sort(args.decks, log)
        elif args.algo == "merge":
            merge_sort_in_place(args.decks, 0, len(args.decks) - 1, log)
        elif args.algo == "quick":
            quick_sort(args.decks, 0, len(args.decks) - 1, log)
        elif args.algo == "heap":
            heap_sort(args.decks, len(args.decks))
        os.close(log)
        if args.gui:
            import sorting_gui
            sorting_gui.main()
if __name__ == "__main__":
    main()