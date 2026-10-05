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
def fonk2(b12):
    a2 = 0
    b3 = len(b12)
    if b3 <= 1:
        return b12, a2
    b4 = b3
    left_half, b5 = b12[:b4], b12[b4:]
    sorted_left, b6 = fonk2(left_half)
    sorted_right, b7 = fonk2(b5)
    sorted_numbers, b8 = fonk1(sorted_left, sorted_right)
    a2 = b6 + b7 + b8
    return sorted_numbers, a2
def fonk3(b12):
    a2 = 0
    left, b9 = [], []
    b10 = b12[0]
    for num in b12[1:]:
        if num < b10:
            left.append(num)
        else:
            b9.append(num)
            a2 += len(left)
    return left, b9, a2
def fonk4(b12):
    a2 = 0
    b3 = len(b12)
    if b3 <= 1:
        return b12, a2
    left, b9, b11 = fonk3(b12)
    left_sorted, b6 = fonk4(left)
    right_sorted, b7 = fonk4(b9)
    a2 = b6 + b7 + b11
    return left_sorted + [b12[0]] + right_sorted, a2
def fonk5():
    import string
    with open('Q8.txt', 'r') as file:
        b12 = file.readlines()
    b12 = [string.atoi(n.strip()) for n in b12[:100000]]
    sorted_numbers, a1 = fonk2(b12)
    print('Number of Inversions:')
    print(a1)
def fonk6():
    import string
    with open('Q8.txt', 'r') as file:
        b12 = file.readlines()
    b12 = [string.atoi(n.strip()) for n in b12[:100000]]
    sorted_numbers, a1 = fonk4(b12)
    print('Number of Inversions:')
    print(a1)
if b13 = = '__main__':
    from timeit import Timer
    b14 = Timer("fonk5()", "from __main__ import run_count_inversion_merge_sort")
    a3 = 1
    print(b14.timeit(a3) / a3)
    b15 = Timer("fonk6()", "from __main__ import run_count_inversion_quick_sort")
    print(b15.timeit(a3) / a3)