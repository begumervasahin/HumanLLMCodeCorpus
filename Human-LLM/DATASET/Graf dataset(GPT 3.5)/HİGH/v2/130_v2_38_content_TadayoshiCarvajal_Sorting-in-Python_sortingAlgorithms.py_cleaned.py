from matplotlib import pyplot as plt
from tqdm import tqdm
from random import randint
from time import time
def fonk1(n, b1 = 0, high=100):
    return [randint(b1, high) for _ in range(n)]
def fonk2(f, b20):
    b2 = time()
    f(b20)
    b3 = time()
    return b3 - b2
def fonk3(f, b20, b4 = 500):
    b5 = sum(fonk2(f, b20) for _ in range(b4))
    return b5 / b4
def fonk4(b20):
    for b6 in range(1, len(b20)):
        if b20[b6] < b20[b6 - 1]:
            return False
    return True
def fonk5(b20):
    for b7 in range(len(b20)):
        key, b6 = b20[b7], b7 - 1
        while b6 > -1 and b20[b6] > key:
            b20[b6 + 1], b6 = b20[b6], b6 - 1
        b20[b6 + 1] = key
def fonk6(b20):
    b8, b7 = True, len(b20)
    while b8:
        b8 = False
        for b6 in range(1, b7):
            if b20[b6] < b20[b6 - 1]:
                b20[b6], b20[b6 - 1], b8 = b20[b6 - 1], b20[b6], True
        b7 -= 1
def fonk7(b20):
    for b15 in range(len(b20)):
        mnmm, b6 = float('infinity'), -1
        for b7 in range(b15, len(b20)):
            if b20[b7] < mnmm:
                mnmm, b6 = b20[b7], b7
        b20[b15], b20[b6] = b20[b6], b20[b15]
def fonk8(b20):
    def fonk9(b20, b10, upto):
        b9 = 2 * b10 + 1
        while b9 < upto:
            if b20[b9] < b20[b9 + 1]:
                b9 += 1
            if b20[b9] > b20[b10]:
                b20[b9], b20[b10] = b20[b10], b20[b9]
                b10 = b9
                b9 = 2 * b10 + 1
            else:
                break
    b11 = len(b20) - 1
    b12 = b11
    [fonk9(b20, b6, b11) for b6 in range(b12, -1, -1)]
    for b6 in range(b11, 0, -1):
        if b20[0] > b20[b6]:
            b20[0], b20[b6] = b20[b6], b20[0]
            fonk9(b20, 0, b6 - 1)
def fonk10(b20):
    if len(b20) > 1:
        b13 = len(b20)
        lh, b14 = b20[:b13], b20[b13:]
        fonk10(lh)
        fonk10(b14)
        b6, b7, b15 = 0, 0, 0
        while b6 < len(lh) and b7 < len(b14):
            if lh[b6] < b14[b7]:
                b20[b15], b6 = lh[b6], b6 + 1
            else:
                b20[b15], b7 = b14[b7], b7 + 1
            b15 += 1
        while b6 < len(lh):
            b20[b15], b6, b15 = lh[b6], b6 + 1, b15 + 1
        while b7 < len(b14):
            b20[b15], b7, b15 = b14[b7], b7 + 1, b15 + 1
def fonk11(b20):
    def fonk12(b20, first, last):
        if first < last:
            b16 = fonk13(b20, first, last)
            fonk12(b20, first, b16 - 1)
            fonk12(b20, b16 + 1, last)
    def fonk13(b20, first, last):
        pv, lm, rm, b17 = b20[first], first + 1, last, False
        while not b17:
            while lm <= rm and b20[lm] <= pv:
                lm += 1
            while rm >= lm and b20[rm] >= pv:
                rm -= 1
            if rm < lm:
                b17 = True
            else:
                b20[lm], b20[rm] = b20[rm], b20[lm]
        b20[first], b20[rm] = b20[rm], b20[first]
        return rm
def fonk14(b20):
    mod, b18 = 10, 1
    while True:
        b19 = [[] for _ in range(10)]
        [b19[(n % mod)
        mod, b18 = mod * 10, b18 * 10
        if len(b19[0]) == len(b20):
            return b19[0]
        b20 = [y for x in b19 for y in x]
def fonk15(b20):
    return sorted(b20)
if b21 = = '__main__':
    b22 = [b6 for b6 in range(100, 25000, 500)]
    b23 = {
        'bubble_sort': [fonk2(bubble_sort, fonk1(b6)) for b6 in tqdm(b22[:10], 'bubble_sort')],
        'selection_sort': [fonk2(selection_sort, fonk1(b6)) for b6 in tqdm(b22[:10], 'selection_sort')],
        'insertion_sort': [fonk2(insertion_sort, fonk1(b6)) for b6 in tqdm(b22[:10], 'insertion_sort')],
        'merge_sort': [fonk2(merge_sort, fonk1(b6)) for b6 in tqdm(b22, 'merge_sort')],
        'heap_sort': [fonk2(heap_sort, fonk1(b6)) for b6 in tqdm(b22, 'heap_sort')],
        'quick_sort': [fonk2(quick_sort, fonk1(b6)) for b6 in tqdm(b22, 'quick_sort')],
        'radix_sort': [fonk2(radix_sort, fonk1(b6)) for b6 in tqdm(b22, 'radix_sort')]
    }
    b24 = {'bubble_sort', 'selection_sort', 'insertion_sort'}
    for sort in b23:
        if sort in b24:
            plt.plot(b22[:10], b23[sort], b25 = sort.replace('_', ' ').title())
        else:
            plt.plot(b22, b23[sort], b25 = sort.replace('_', ' ').title())
    plt.legend(b26 = 'lower right')
    plt.ylabel('Time (seconds)')
    plt.xlabel('List Size')
    plt.show()