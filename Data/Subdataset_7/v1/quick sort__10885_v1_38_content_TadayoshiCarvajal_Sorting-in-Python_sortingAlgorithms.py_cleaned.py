from matplotlib import pyplot as plt
from tqdm import tqdm
from random import randint
'''Utility Functions'''
def fonk1(n, b1 = 0, high=100):
    return [randint(b1, high) for _ in range(n)]
def fonk2(f, b19):
    from time import time
    b2 = time()
    f(b19)
    b3 = time()
    return b3 - b2
def fonk3(f, b19, b4 = 500):
    a1 = 0
    for b5 in range(b4):
        a1 += fonk2(f, b19)
    return a1 / b4
def fonk4(b19):
    for b5 in range(1, len(b19)):
        if b19[b5] < b19[b5 - 1]:
            return False
    return True
'''Sorting Algorithms'''
def fonk5(b19):
    for b6 in range(len(b19)):
        key, b5 = b19[b6], b6 - 1
        while b5 > -1 and b19[b5] > key:
            b19[b5 + 1], b5 = b19[b5], b5 - 1
        b19[b5 + 1] = key
def fonk6(b19):
    b7, b6 = True, len(b19)
    while b7:
        b7 = False
        for b5 in range(1, b6):
            if b19[b5] < b19[b5 - 1]:
                b19[b5], b19[b5 - 1], b7 = b19[b5 - 1], b19[b5], True
        b6 -= 1
def fonk7(b19):
    for b14 in range(len(b19)):
        mnmm, b5 = float('infinity'), -1
        for b6 in range(b14, len(b19)):
            if b19[b6] < mnmm:
                mnmm, b5 = b19[b6], b6
        b19[b14], b19[b5] = b19[b5], b19[b14]
def fonk8(b19):
    def fonk9(b19, b9, upto):
        b8 = 2 * b9 + 1
        while b8 < upto:
            if b19[b8] < b19[b8 + 1]:
                b8 += 1
            if b19[b8] > b19[b9]:
                b19[b8], b19[b9] = b19[b9], b19[b8]
                b9 = b8
                b8 = 2 * b9 + 1
            else:
                break
    b10 = len(b19) - 1
    b11 = b10
    [fonk9(b19, b5, b10) for b5 in range(b11, -1, -1)]
    for b5 in range(b10, 0, -1):
        if b19[0] > b19[b5]:
            b19[0], b19[b5] = b19[b5], b19[0]
            fonk9(b19, 0, b5 - 1)
def fonk10(b19):
    if len(b19) > 1:
        b12 = len(b19)
        lh, b13 = b19[:b12], b19[b12:]
        fonk10(lh)
        fonk10(b13)
        b5, b6, b14 = 0, 0, 0
        while b5 < len(lh) and b6 < len(b13):
            if lh[b5] < b13[b6]:
                b19[b14], b5 = lh[b5], b5 + 1
            else:
                b19[b14], b6 = b13[b6], b6 + 1
            b14 += 1
        while b5 < len(lh):
            b19[b14], b5, b14 = lh[b5], b5 + 1, b14 + 1
        while b6 < len(b13):
            b19[b14], b6, b14 = b13[b6], b6 + 1, b14 + 1
def fonk11(b19):
    def fonk12(b19, first, last):
        if first < last:
            b15 = fonk13(b19, first, last)
            fonk12(b19, first, b15 - 1)
            fonk12(b19, b15 + 1, last)
    def fonk13(b19, first, last):
        pv, lm, rm, b16 = b19[first], first + 1, last, False
        while not b16:
            while lm <= rm and b19[lm] <= pv:
                lm += 1
            while rm >= lm and b19[rm] >= pv:
                rm -= 1
            if rm < lm:
                b16 = True
            else:
                b19[lm], b19[rm] = b19[rm], b19[lm]
        b19[first], b19[rm] = b19[rm], b19[first]
        return rm
    fonk12(b19, 0, len(b19) - 1)
def fonk14(b19):
    mod, b17 = 10, 1
    while True:
        b18 = [[] for _ in range(10)]
        [b18[(n % mod)
        mod, b17 = mod * 10, b17 * 10
        if len(b18[0]) == len(b19):
            return b18[0]
        b19 = [y for x in b18 for y in x]
def fonk15(b19):
    return sorted(b19)
if b20 = = '__main__':
    b21 = [b5 for b5 in range(100, 25000, 500)]
    b22 = {
        'bubble_sort': [fonk2(bubble_sort, fonk1(b5)) for b5 in tqdm(b21[:10], 'bubble_sort')],
        'selection_sort': [fonk2(selection_sort, fonk1(b5)) for b5 in tqdm(b21[:10], 'selection_sort')],
        'insertion_sort': [fonk2(insertion_sort, fonk1(b5)) for b5 in tqdm(b21[:10], 'insertion_sort')],
        'merge_sort': [fonk2(merge_sort, fonk1(b5)) for b5 in tqdm(b21, 'merge_sort')],
        'heap_sort': [fonk2(heap_sort, fonk1(b5)) for b5 in tqdm(b21, 'heap_sort')],
        'quick_sort': [fonk2(quick_sort, fonk1(b5)) for b5 in tqdm(b21, 'quick_sort')],
        'radix_sort': [fonk2(radix_sort, fonk1(b5)) for b5 in tqdm(b21, 'radix_sort')]
    }
    b23 = {'bubble_sort', 'selection_sort', 'insertion_sort'}
    for sort in b22:
        if sort in b23:
            plt.plot(b21[:10], b22[sort], b24 = sort.replace('_', ' ').title())
        else:
            plt.plot(b21, b22[sort], b24 = sort.replace('_', ' ').title())
    plt.legend(b25 = 'lower right')
    plt.ylabel('Time (seconds)')
    plt.xlabel('List Size')
    plt.show()