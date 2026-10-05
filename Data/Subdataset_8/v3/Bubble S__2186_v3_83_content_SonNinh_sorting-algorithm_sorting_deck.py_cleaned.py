import argparse
import os
import math
def bubble_sort(decks, log):
    n = 0
    not_done = True
    while not_done:
        not_done = False
        for i in range(0, len(decks) - 1 - n):
            os.write(log, f'{i} {i + 1} {n}\n'.encode())
            if decks[i] > decks[i + 1]:
                os.write(log, f'{i} {i + 1} {n} s\n'.encode())
                decks[i], decks[i + 1] = decks[i + 1], decks[i]
                not_done = True
                print(*decks)
        n += 1
def insertion_sort(decks, log):
    def insert_element_back(i):
        for j in range(i, -1, -1):
            os.write(log, f'{j} {i + 1}\n'.encode())
            if j > 0:
                if decks[i + 1] >= decks[j - 1]:
                    os.write(log, f'{j} {i + 1} s\n'.encode())
                    decks.insert(j, decks[i + 1])
                    decks.pop(i + 2)
                    break
            else:
                os.write(log, f'0 {i + 1} s\n'.encode())
                decks.insert(0, decks[i + 1])
                decks.pop(i + 2)
        print(*decks)
    for i in range(0, len(decks) - 1):
        if decks[i] > decks[i + 1]:
            insert_element_back(i)
        else:
            os.write(log, f'{i} {i + 1}\n'.encode())
def merge_sort(decks, left, right, log):
    def merge_2_sorted_lists():
        i = left
        j = center
        os.write(log, f'{left} {right} {center}\n'.encode())
        while i < j and j <= right:
            os.write(log, f'{left} {right} {i} {j}\n'.encode())
            if decks[i] > decks[j]:
                os.write(log, f'{left} {right} {i} {j} s\n'.encode())
                decks.insert(i, decks[j])
                decks.pop(j + 1)
                i += 1
                j += 1
            else:
                os.write(log, f'{left} {right} {i} {i} s\n'.encode())
                i += 1
        print(*decks[left:right + 1])
    center = math.ceil((right + left) / 2)
    if right - left > 1:
        merge_sort(decks, left, center - 1, log)
        merge_sort(decks, center, right, log)
        merge_2_sorted_lists()
    elif right - left == 1:
        merge_2_sorted_lists()
    else:
        os.write(log, f'{left} {right}\n'.encode())
def quick_sort(decks, left, right, log):
    def partition(i, pivot):
        for j in range(left, right):
            os.write(log, f'{left} {right} {i} {j}\n'.encode())
            if decks[j] < pivot:
                i += 1
                os.write(log, f'{left} {right} {i} {j} s\n'.encode())
                decks[i], decks[j] = decks[j], decks[i]
        i += 1
        os.write(log, f'{left} {right} {i} {right} s\n'.encode())
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
    for i in range(n - 1, -1, -1):
        heapify(i, n)
    for ite in range(n - 1, 0, -1):
        decks[ite], decks[0] = decks[0], decks[ite]
        heapify(0, ite, decks)
    print(decks)
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('decks', type=int, nargs='+', help="")
    parser.add_argument("--algo", type=str, default="bubble", help="algorithm")
    parser.add_argument("--gui", action="store_true", help="GUI mode")
    args = parser.parse_args()
    if len(args.decks) > 1:
        try:
            os.unlink("log")
        except Exception:
            pass
        log = os.open("log", os.O_RDWR | os.O_CREAT)
        os.write(log, ' '.join(str(e) for e in args.decks).encode())
        os.write(log, '\n'.encode())
        os.write(log, args.algo.encode())
        os.write(log, '\n'.encode())
        if args.algo == "bubble":
            res = bubble_sort(args.decks, log)
        elif args.algo == "insert":
            res = insertion_sort(args.decks, log)
        elif args.algo == "merge":
            res = merge_sort(args.decks, 0, len(args.decks) - 1, log)
        elif args.algo == "quick":
            res = quick_sort(args.decks, 0, len(args.decks) - 1, log)
        elif args.algo == "heap":
            heap_sort(args.decks, len(args.decks))
        os.close(log)
        if args.gui is True:
            import sorting_gui
            sorting_gui.main()
if __name__ == "__main__":
    main()