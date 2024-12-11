import string
from timeit import Timer
def fonk1(left, b9):
    b1 = []
    a1 = 0
    i, b2 = 0, 0
    while i < len(left) and b2 < len(b9):
        if left[i] > b9[b2]:
            b1.append(b9[b2])
            a1 += len(left) - i
            b2 += 1
        else:
            b1.append(left[i])
            i += 1
    b1.extend(left[i:])
    b1.extend(b9[b2:])
    return b1, a1
def fonk2(b13):
    a2 = 0
    b3 = len(b13)
    if b3 <= 1:
        return b13, a2
    b4 = b3
    left_half, b5 = b13[:b4], b13[b4:]
    sorted_left, b6 = fonk2(left_half)
    sorted_right, b7 = fonk2(b5)
    sorted_numbers, b8 = fonk1(sorted_left, sorted_right)
    a2 = b6 + b7 + b8
    return sorted_numbers, a2
def fonk3(b13):
    a2 = 0
    left, b9 = [], []
    b10 = b13[0]
    for num in b13[1:]:
        if num < b10:
            left.append(num)
        else:
            b9.append(num)
            a2 += len(left)
    return left, b9, a2
def fonk4(b13):
    a2 = 0
    b3 = len(b13)
    if b3 <= 1:
        return b13, a2
    left, b9, b11 = fonk3(b13)
    left_sorted, b6 = fonk4(left)
    right_sorted, b7 = fonk4(b9)
    a2 = b6 + b7 + b11
    return left_sorted + [b13[0]] + right_sorted, a2
def fonk5(filename, b12 = 100000):
    with open(filename, 'r') as file:
        b13 = file.readlines()
    return [string.atoi(n.strip()) for n in b13[:b12]]
def fonk6():
    b13 = fonk5('Q8.txt')
    sorted_numbers, a1 = fonk2(b13)
    print('Number of Inversions:')
    print(a1)
def fonk7():
    b13 = fonk5('Q8.txt')
    sorted_numbers, a1 = fonk4(b13)
    print('Number of Inversions:')
    print(a1)
if b14 = = '__main__':
    a3 = 1
    b15 = Timer("fonk6()", "from __main__ import run_count_inversion_merge_sort")
    print(b15.timeit(a3) / a3)
    b16 = Timer("fonk7()", "from __main__ import run_count_inversion_quick_sort")
    print(b16.timeit(a3) / a3)