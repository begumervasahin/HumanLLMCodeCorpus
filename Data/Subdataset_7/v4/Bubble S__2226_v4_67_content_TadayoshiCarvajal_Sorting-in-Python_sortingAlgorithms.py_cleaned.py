from matplotlib import pyplot as plt
from tqdm import tqdm
import random
from time import time
def fonk1(b7, b1 = 0, high=100):
    return [random.randint(b1, high) for _ in range(b7)]
def fonk2(sort_func, b20):
    b2 = time()
    sort_func(b20)
    b3 = time()
    return b3 - b2
def fonk3(sort_func, b20, b4 = 500):
    b5 = sum(fonk2(sort_func, b20) for _ in range(b4))
    return b5 / b4
def fonk4(b20):
    return all(b20[b6] <= b20[b6+1] for b6 in range(len(b20)-1))
def fonk5(b20):
    for j in range(len(b20)):
        key, b6 = b20[j], j - 1
        while b6 >= 0 and b20[b6] > key:
            b20[b6 + 1] = b20[b6]
            b6 -= 1
        b20[b6 + 1] = key
    return b20
def fonk6(b20):
    b7 = len(b20)
    for b6 in range(b7):
        for j in range(0, b7-b6-1):
            if b20[j] > b20[j+1]:
                b20[j], b20[j+1] = b20[j+1], b20[j]
    return b20
def fonk7(b20):
    for b6 in range(len(b20)):
        b8 = b6
        for j in range(b6+1, len(b20)):
            if b20[j] < b20[b8]:
                b8 = j
        b20[b6], b20[b8] = b20[b8], b20[b6]
    return b20
def fonk8(b20):
    def fonk9(b20, b2, end):
        b9 = b2
        while True:
            b10 = b9 * 2 + 1
            if b10 > end:
                break
            if b10 + 1 <= end and b20[b10] < b20[b10 + 1]:
                b10 += 1
            if b20[b9] < b20[b10]:
                b20[b9], b20[b10] = b20[b10], b20[b9]
                b9 = b10
            else:
                break
    for b2 in range(len(b20)
        fonk9(b20, b2, len(b20) - 1)
    for end in range(len(b20) - 1, 0, -1):
        b20[end], b20[0] = b20[0], b20[end]
        fonk9(b20, 0, end - 1)
    return b20
def fonk10(b20):
    if len(b20) <= 1:
        return b20
    b11 = len(b20)
    b12 = b20[:b11]
    b13 = b20[b11:]
    fonk10(b12)
    fonk10(b13)
    b6 = j = k = 0
    while b6 < len(b12) and j < len(b13):
        if b12[b6] < b13[j]:
            b20[k] = b12[b6]
            b6 += 1
        else:
            b20[k] = b13[j]
            j += 1
        k += 1
    while b6 < len(b12):
        b20[k] = b12[b6]
        b6 += 1
        k += 1
    while j < len(b13):
        b20[k] = b13[j]
        j += 1
        k += 1
    return b20
def fonk11(b20):
    if len(b20) <= 1:
        return b20
    b14 = b20[len(b20)
    b15 = [x for x in b20 if x < b14]
    b16 = [x for x in b20 if x == b14]
    b17 = [x for x in b20 if x > b14]
    return fonk11(b15) + b16 + fonk11(b17)
def fonk12(b20):
    mod, b18 = 10, 1
    while True:
        b19 = [[] for _ in range(10)]
        for num in b20:
            b19[(num % mod)
        mod *= 10
        b18 *= 10
        b20 = [num for bucket in b19 for num in bucket]
        if len(b19[0]) == len(b20):
            return b20
def fonk13(b20):
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
    plt.legend(b26 = 'lower b17')
    plt.ylabel('Time (seconds)')
    plt.xlabel('List Size')
    plt.show()