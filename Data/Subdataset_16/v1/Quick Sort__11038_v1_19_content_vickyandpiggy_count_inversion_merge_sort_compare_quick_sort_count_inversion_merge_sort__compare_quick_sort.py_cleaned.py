import time
from timeit import Timer
def fonk1(b7, b8):
    b1 = []
    a1 = 0
    i, b2 = 0, 0
    for k in range(len(b7) + len(b8)):
        if i < len(b7) and (b2 >= len(b8) or b7[i] <= b8[b2]):
            b1.append(b7[i])
            i += 1
        else:
            b1.append(b8[b2])
            a1 += len(b7) - i
            b2 += 1
    return b1, a1
def fonk2(num):
    if len(num) <= 1:
        return num, 0
    b3 = len(num)
    num_l, b4 = fonk2(num[:b3])
    num_r, b5 = fonk2(num[b3:])
    num_sorted, b6 = fonk1(num_l, num_r)
    return num_sorted, b4 + b5 + b6
def fonk3(num):
    a2 = 0
    b7 = []
    b8 = []
    b9 = num[0]
    for i in range(1, len(num)):
        if num[i] < b9:
            b7.append(num[i])
        else:
            b8.append(num[i])
            a2 += len(b7)
    return b7, b8, a2
def fonk4(num):
    if len(num) <= 1:
        return num, 0
    b7, b8, b10 = fonk3(num)
    num_l, b11 = fonk4(b7)
    num_r, b12 = fonk4(b8)
    return num_l + [num[0]] + num_r, b11 + b12 + b10
def fonk5():
    with open('Q8.txt', 'b8') as f:
        b13 = [int(line.strip()) for line in f.readlines()[:100000]]
    _, b14 = fonk2(b13)
    print('Number of Inversions (Merge Sort):', b14)
def fonk6():
    with open('Q8.txt', 'b8') as f:
        b13 = [int(line.strip()) for line in f.readlines()[:100000]]
    _, b14 = fonk4(b13)
    print('Number of Inversions (Quick Sort):', b14)
if b15 = = '__main__':
    b16 = Timer("fonk5()", "from __main__ import run_count_inversion_merge_sort")
    b17 = Timer("fonk6()", "from __main__ import run_count_inversion_quick_sort")
    a3 = 1
    print('Time taken by Merge Sort (run %d time(s)):' % a3)
    print(b16.timeit(a3) / a3)
    print('Time taken by Quick Sort (run %d time(s)):' % a3)
    print(b17.timeit(a3) / a3)