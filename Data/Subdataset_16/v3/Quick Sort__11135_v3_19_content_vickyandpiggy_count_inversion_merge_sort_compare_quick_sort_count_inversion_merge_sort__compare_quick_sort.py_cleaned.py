
import time
from timeit import Timer
def fonk1(left, b8):
    b1 = []
    a1 = 0
    i, b2 = 0, 0
    while i < len(left) and b2 < len(b8):
        if left[i] <= b8[b2]:
            b1.append(left[i])
            i += 1
        else:
            b1.append(b8[b2])
            a1 += len(left) - i
            b2 += 1
    b1.extend(left[i:])
    b1.extend(b8[b2:])
    return b1, a1
def fonk2(b10):
    if len(b10) <= 1:
        return b10, 0
    b3 = len(b10)
    left_sorted, b4 = fonk2(b10[:b3])
    right_sorted, b5 = fonk2(b10[b3:])
    sorted_list, b6 = fonk1(left_sorted, right_sorted)
    return sorted_list, b4 + b5 + b6
def fonk3(b10):
    b7 = b10[0]
    left, b8 = [], []
    a2 = 0
    for num in b10[1:]:
        if num < b7:
            left.append(num)
        else:
            b8.append(num)
            a2 += len(left)
    return left, b8, a2
def fonk4(b10):
    if len(b10) <= 1:
        return b10, 0
    left, b8, b9 = fonk3(b10)
    left_sorted, b4 = fonk4(left)
    right_sorted, b5 = fonk4(b8)
    return left_sorted + [b10[0]] + right_sorted, b4 + b5 + b9
def fonk5():
    with open('Q8.txt', 'r') as file:
        b10 = [int(line.strip()) for line in file.readlines()[:100000]]
    _, b11 = fonk2(b10)
    print('Number of Inversions (Merge Sort):', b11)
def fonk6():
    with open('Q8.txt', 'r') as file:
        b10 = [int(line.strip()) for line in file.readlines()[:100000]]
    _, b11 = fonk4(b10)
    print('Number of Inversions (Quick Sort):', b11)
if b12 = = '__main__':
    b13 = Timer("fonk5()", "from __main__ import run_count_inversion_merge_sort")
    b14 = Timer("fonk6()", "from __main__ import run_count_inversion_quick_sort")
    a3 = 1
    print('Time taken by Merge Sort (run %d time(s)):' % a3)
    print(b13.timeit(a3) / a3)
    print('Time taken by Quick Sort (run %d time(s)):' % a3)
    print(b14.timeit(a3) / a3)