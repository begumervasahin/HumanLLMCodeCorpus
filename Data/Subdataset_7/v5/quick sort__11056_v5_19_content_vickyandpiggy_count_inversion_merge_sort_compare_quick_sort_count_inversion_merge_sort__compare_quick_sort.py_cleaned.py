def fonk1(b8, b9):
    b1 = []
    a1 = 0
    i, b2 = 0, 0
    while i < len(b8) and b2 < len(b9):
        if b8[i] <= b9[b2]:
            b1.append(b8[i])
            i += 1
        else:
            b1.append(b9[b2])
            b2 += 1
            a1 += len(b8) - i
    b1.extend(b8[i:])
    b1.extend(b9[b2:])
    return b1, a1
def fonk2(b11):
    if len(b11) <= 1:
        return b11, 0
    b3 = len(b11)
    left_sorted, b4 = fonk2(b11[:b3])
    right_sorted, b5 = fonk2(b11[b3:])
    merged_sorted, b6 = fonk1(left_sorted, right_sorted)
    b7 = b4 + b5 + b6
    return merged_sorted, b7
def fonk3(b11):
    b8 = []
    b9 = []
    b10 = b11[0]
    b11 = b11[::-1]
    a2 = 0
    for num in b11[1:]:
        if num < b10:
            b8.append(num)
        else:
            b9.append(num)
            a2 += len(b8)
    a2 += len(b8)
    b8.reverse()
    b9.reverse()
    return b8, b9, a2
def fonk4(b11):
    if len(b11) <= 1:
        return b11, 0
    b8, b9, b12 = fonk3(b11)
    left_sorted, b4 = fonk4(b8)
    right_sorted, b5 = fonk4(b9)
    b7 = b4 + b5 + b12
    return left_sorted + [b11[0]] + right_sorted, b7
def fonk5():
    with open('Q8.txt', 'r') as file:
        b13 = [int(line.strip()) for line in file.readlines()[:100000]]
    sorted_numbers, b14 = fonk2(b13)
    print('Number of Inversions:')
    print(b14)
def fonk6():
    with open('Q8.txt', 'r') as file:
        b13 = [int(line.strip()) for line in file.readlines()[:100000]]
    sorted_numbers, b14 = fonk4(b13)
    print('Number of Inversions:')
    print(b14)
if b15 = = '__main__':
    from timeit import Timer
    b16 = Timer("fonk5()", "from __main__ import run_count_inversions_merge_sort")
    a3 = 1
    print('Time: (ran %d time(s))' % a3)
    print(b16.timeit(a3) / a3)
    b17 = Timer("fonk6()", "from __main__ import run_count_inversions_quick_sort")
    a3 = 1
    print('Time: (ran %d time(s))' % a3)
    print(b17.timeit(a3) / a3)