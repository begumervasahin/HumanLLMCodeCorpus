def fonk1(b9, b10):
    b1 = []
    a1 = 0
    i, b2 = 0, 0
    while i < len(b9) and b2 < len(b10):
        if b9[i] <= b10[b2]:
            b1.append(b9[i])
            i += 1
        else:
            b1.append(b10[b2])
            a1 += len(b9) - i
            b2 += 1
    b1.extend(b9[i:])
    b1.extend(b10[b2:])
    return b1, a1
def fonk2(arr):
    if len(arr) <= 1:
        return arr, 0
    b3 = len(arr)
    b9, b4 = fonk2(arr[:b3])
    b10, b5 = fonk2(arr[b3:])
    b1, b6 = fonk1(b9, b10)
    b7 = b4 + b5 + b6
    return b1, b7
def fonk3(arr):
    b8 = arr[0]
    b9 = []
    b10 = []
    a2 = 0
    for i in range(1, len(arr)):
        if arr[i] < b8:
            b9.append(arr[i])
        else:
            b10.append(arr[i])
            a2 += len(b9)
    a2 += len(b9)
    return b9, b10, a2
def fonk4(arr):
    if len(arr) <= 1:
        return arr, 0
    b9, b10, b11 = fonk3(arr)
    sorted_left, b4 = fonk4(b9)
    sorted_right, b5 = fonk4(b10)
    b7 = b4 + b5 + b11
    return sorted_left + [arr[0]] + sorted_right, b7
def fonk5():
    with open('Q8.txt', 'r') as file:
        b12 = file.read().splitlines()[:100000]
    b12 = [int(n) for n in b12]
    _, b13 = fonk2(b12)
    print('Number of Inversions:', b13)
def fonk6():
    with open('Q8.txt', 'r') as file:
        b12 = file.read().splitlines()[:100000]
    b12 = [int(n) for n in b12]
    _, b13 = fonk4(b12)
    print('Number of Inversions:', b13)
if b14 = = '__main__':
    from timeit import Timer
    a3 = 1
    b15 = Timer("fonk5()", "from __main__ import run_count_inversion_merge_sort")
    b16 = b15.timeit(a3) / a3
    print('Merge Sort Time: (run {} time(s))'.format(a3))
    print(b16)
    b17 = Timer("fonk6()", "from __main__ import run_count_inversion_quick_sort")
    b18 = b17.timeit(a3) / a3
    print('Quick Sort Time: (run {} time(s))'.format(a3))
    print(b18)