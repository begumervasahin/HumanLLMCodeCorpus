import argparse
import math
import os
def bubble(decks, log):
    n = 0
    not_done = True
    while not_done:
        not_done = False
        for i in range(len(decks) - 1 - n):
            os.write(log, f'{i} {i+1} {n}\n'.encode())
            if decks[i] > decks[i + 1]:
                os.write(log, f'{i} {i+1} {n} s\n'.encode())
                decks[i], decks[i + 1] = decks[i + 1], decks[i]
                not_done = True
                print(*decks)
        n += 1
def insertion(decks, log):
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
def merge_out_place(decks):
    if len(decks) > 2:
        p = len(decks)
        left_sorted = merge_out_place(decks[:p])
        right_sorted = merge_out_place(decks[p:])
        res = []
        left = right = 0
        while left < len(left_sorted) and right < len(right_sorted):
            if left_sorted[left] <= right_sorted[right]:
                res.append(left_sorted[left])
                left += 1
            else:
                res.append(right_sorted[right])
                right += 1
        res += left_sorted[left:]
        res += right_sorted[right:]
        print(*res)
        return res
    else:
        if len(decks) == 2 and decks[0] > decks[1]:
            decks[0], decks[1] = decks[1], decks[0]
            print(*decks)
        return decks
def merge(decks, left, right, log):
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
        merge(decks, left, center - 1, log)
        merge(decks, center, right, log)
        arrange_2_sorted_lists()
    elif right - left == 1:
        arrange_2_sorted_lists()
    else:
        os.write(log, f'{left} {right}\n'.encode())
def quick(decks, left, right, log):
    def partition(i, pivot):
        for j in range(left, right):
            if decks[j] < pivot:
                i += 1
                decks[i], decks[j] = decks[j], decks[i]
        return i
    if left < right:
        pivot_index = partition(left - 1, decks[right])
        decks[pivot_index + 1], decks[right] = decks[right], decks[pivot_index + 1]
        quick(decks, left, pivot_index, log)
        quick(decks, pivot_index + 2, right, log)
def heap(decks, n):
    def heapify(i, n):
        max_i = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and decks[left] > decks[max_i]:
            max_i = left
        if right < n and decks[right] > decks[max_i]:
            max_i = right
        if max_i != i:
            decks[i], decks[max_i] = decks[max_i], decks[i]
            heapify(max_i, n)
    for i in range(n
        heapify(i, n)
    for i in range(n - 1, 0, -1):
        decks[i], decks[0] = decks[0], decks[i]
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
            bubble(args.decks, log)
        elif args.algo == "insert":
            insertion(args.decks, log)
        elif args.algo == "merge":
            merge(args.decks, 0, len(args.decks) - 1, log)
        elif args.algo == "quick":
            quick(args.decks, 0, len(args.decks) - 1, log)
        elif args.algo == "heap":
            heap(args.decks, len(args.decks))
        os.close(log)
        if args.gui:
            import sorting_gui
            sorting_gui.main()
if __name__ == "__main__":
    main()