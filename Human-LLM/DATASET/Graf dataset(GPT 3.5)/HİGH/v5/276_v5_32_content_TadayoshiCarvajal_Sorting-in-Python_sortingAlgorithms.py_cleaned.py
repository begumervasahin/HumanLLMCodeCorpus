from matplotlib import pyplot as plt
from tqdm import tqdm
from time import time
from random import randint, shuffle
def fonk1(b8, b1 = 0, high=100):
    return [randint(b1, high) for _ in range(b8)]
def fonk2(func, lst):
    b2 = lst.copy()
    shuffle(b2)
    b3 = time()
    func(b2)
    b4 = time()
    return b4 - b3
def fonk3(func, lst, b5 = 500):
    a1 = 0
    for _ in range(b5):
        a1 += fonk2(func, lst)
    return a1 / b5
def fonk4(lst):
    return all(lst[b7] <= lst[b7 + 1] for b7 in range(len(lst) - 1))
def fonk5(lst):
    for j in range(1, len(lst)):
        b6 = lst[j]
        b7 = j - 1
        while b7 >= 0 and lst[b7] > b6:
            lst[b7 + 1] = lst[b7]
            b7 -= 1
        lst[b7 + 1] = b6
def fonk6(lst):
    b8 = len(lst)
    for b7 in range(b8):
        for j in range(b8 - b7 - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
def fonk7(lst):
    for b7 in range(len(lst)):
        b9 = b7
        for j in range(b7 + 1, len(lst)):
            if lst[j] < lst[b9]:
                b9 = j
        lst[b7], lst[b9] = lst[b9], lst[b7]
def fonk8(lst):
    def fonk9(lst, start, end):
        b10 = start
        while True:
            b11 = 2 * b10 + 1
            if b11 > end:
                break
            if b11 + 1 <= end and lst[b11] < lst[b11 + 1]:
                b11 += 1
            if lst[b10] < lst[b11]:
                lst[b10], lst[b11] = lst[b11], lst[b10]
                b10 = b11
            else:
                break
    for start in range(len(lst)
        fonk9(lst, start, len(lst) - 1)
    for end in range(len(lst) - 1, 0, -1):
        lst[end], lst[0] = lst[0], lst[end]
        fonk9(lst, 0, end - 1)
def fonk10(lst):
    if len(lst) > 1:
        b12 = len(lst)
        b13 = lst[:b12]
        b14 = lst[b12:]
        fonk10(b13)
        fonk10(b14)
        b7 = j = k = 0
        while b7 < len(b13) and j < len(b14):
            if b13[b7] < b14[j]:
                lst[k] = b13[b7]
                b7 += 1
            else:
                lst[k] = b14[j]
                j += 1
            k += 1
        while b7 < len(b13):
            lst[k] = b13[b7]
            b7 += 1
            k += 1
        while j < len(b14):
            lst[k] = b14[j]
            j += 1
            k += 1
def fonk11(lst):
    def fonk12(lst, b1, high):
        b15 = lst[high]
        b7 = b1 - 1
        for j in range(b1, high):
            if lst[j] < b15:
                b7 += 1
                lst[b7], lst[j] = lst[j], lst[b7]
        lst[b7 + 1], lst[high] = lst[high], lst[b7 + 1]
        return b7 + 1
    def fonk13(lst, b1, high):
        if b1 < high:
            b16 = fonk12(lst, b1, high)
            fonk13(lst, b1, b16 - 1)
            fonk13(lst, b16 + 1, high)
    fonk13(lst, 0, len(lst) - 1)
def fonk14(lst):
    def fonk15(lst, a2):
        b17 = [0] * len(lst)
        b18 = [0] * 10
        for num in lst:
            b19 = num
            b18[b19 % 10] += 1
        for b7 in range(1, 10):
            b18[b7] += b18[b7 - 1]
        b7 = len(lst) - 1
        while b7 >= 0:
            b19 = lst[b7]
            b17[b18[b19 % 10] - 1] = lst[b7]
            b18[b19 % 10] -= 1
            b7 -= 1
        b7 = 0
        for b7 in range(len(lst)):
            lst[b7] = b17[b7]
    b20 = max(lst)
    a2 = 1
    while b20
        fonk15(lst, a2)
        a2 *= 10
def fonk16(lst):
    return sorted(lst)
if b21 = = '__main__':
    b22 = list(range(100, 25000, 500))
    b23 = {
        'bubble_sort': bubble_sort,
        'selection_sort': selection_sort,
        'insertion_sort': insertion_sort,
        'merge_sort': merge_sort,
        'heap_sort': heap_sort,
        'quick_sort': quick_sort,
        'radix_sort': radix_sort
    }
    b24 = {algo: [fonk3(b23[algo], fonk1(b7)) for b7 in tqdm(b22, desc=algo)] for algo in b23}
    for sort in b24:
        plt.plot(b22, b24[sort], b25 = sort.replace('_', ' ').title())
    plt.legend(b26 = 'lower right')
    plt.xlabel('List Size')
    plt.ylabel('Time (Seconds)')
    plt.show()