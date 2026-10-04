import argparse
import math
import os
def bubble_sort(decks, log):
    n = 0
    not_done = True
    while not_done:
        not_done = False
        for i in range(len(decks) - 1 - n):
            os.write(log, '{} {} {}\n'.format(i, i + 1, n).encode())
            if decks[i] > decks[i + 1]:
                os.write(log, '{} {} {} s\n'.format(i, i + 1, n).encode())
                decks[i], decks[i + 1] = decks[i + 1], decks[i]
                not_done = True
                print(*decks)
        n += 1
def insertion_sort(decks, log):
    def check_back_insertion(decks, log, i):
        for j in range(i, -1, -1):
            os.write(log, '{} {}\n'.format(j, i + 1).encode())
            if j > 0 and decks[i + 1] >= decks[j - 1]:
                os.write(log, '{} {} s\n'.format(j, i + 1).encode())
                decks.insert(j, decks[i + 1])
                decks.pop(i + 2)
                break
            elif j == 0:
                os.write(log, '{} {} s\n'.format(0, i + 1).encode())
                decks.insert(0, decks[i + 1])
                decks.pop(i + 2)
        print(*decks)
    for i in range(len(decks) - 1):
        if decks[i] > decks[i + 1]:
            check_back_insertion(decks, log, i)
        else:
            os.write(log, '{} {}\n'.format(i, i + 1).encode())
def merge_out_place(decks):
    if len(decks) > 2:
        mid = len(decks)
        left_sorted = merge_out_place(decks[:mid])
        right_sorted = merge_out_place(decks[mid:])
        result = merge(left_sorted, right_sorted)
        print(*result)
        return result
    elif len(decks) == 2:
        if decks[0] > decks[1]:
            decks[0], decks[1] = decks[1], decks[0]
        print(*decks)
        return decks
def merge(decks, left, right, log):
    def arrange_sorted_lists():
        i = left
        j = center
        os.write(log, '{} {} {}\n'.format(left, right, center).encode())
        while i < j and j <= right:
            os.write(log, '{} {} '.format(left, right).encode())
            if decks[i] > decks[j]:
                os.write(log, '{} {} s\n'.format(i, j).encode())
                decks.insert(i, decks[j])
                decks.pop(j + 1)
                i += 1
                j += 1
            else:
                os.write(log, '{} {} s\n'.format(i, i).encode())
                i += 1
        print(*decks[left:right + 1])
    center = math.ceil((right + left) / 2)
    if right - left > 1:
        merge(decks, left, center - 1, log)
        merge(decks, center, right, log)
        arrange_sorted_lists()
    elif right - left == 1:
        arrange_sorted_lists()
    else:
        os.write(log, '{} {}\n'.format(left, right).encode())
def quick_sort(decks, left, right, log):
    def partition(i, pivot):
        for j in range(left, right):
            os.write(log, '{} {} {} {}\n'.format(left, right, i, j).encode())
            if decks[j] < pivot:
                i += 1
                os.write(log, '{} {} {} {} s\n'.format(left, right, i, j).encode())
                decks[i], decks[j] = decks[j], decks[i]
        i += 1
        os.write(log, '{} {} {} {} s\n'.format(left, right, i, right).encode())
        return i
    if left < right:
        i = left - 1
        pivot = decks[right]
        i = partition(i, pivot)
        decks[i], decks[right] = decks[right], decks[i]
        print("P:", pivot)
        print(*decks)
        quick_sort(decks, left, i - 1, log)
        quick_sort(decks, i + 1, right, log)
def heap_sort(decks, n):
    def heapify(i, n, decks):
        max_i = i
        left = i * 2 + 1
        right = i * 2 + 2
        if left < n and decks[max_i] < decks[left]:
            max_i = left
        if right < n and decks[max_i] < decks[right]:
            max_i = right
        if i != max_i:
            decks[i], decks[max_i] = decks[max_i], decks[i]
            heapify(max_i, n, decks)
    for i in range(n
        heapify(i, n, decks)
    for i in range(n - 1, 0, -1):
        decks[i], decks[0] = decks[0], decks[i]
        heapify(0, i, decks)
    print(decks)
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
            heap_sort(args.decks, len(args.decks))
        os.close(log)
        if args.gui:
            import sorting_gui
            sorting_gui.main()
if __name__ == "__main__":
    main()