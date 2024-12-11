from matplotlib import pyplot as plt
from tqdm import tqdm
import random
from time import time
'''Utility Functions'''
def fonk1(b8, b1 = 0, high=100):
    return [random.randint(b1, high) for _ in range(b8)]
def fonk2(sort_func, array):
    b2 = time()
    sort_func(array)
    b3 = time()
    return b3 - b2
def fonk3(sort_func, array, b4 = 500):
    b5 = sum(fonk2(sort_func, array) for _ in range(b4))
    return b5 / b4
def fonk4(array):
    return all(array[b7] <= array[b7 + 1] for b7 in range(len(array) - 1))
'''Sorting Algorithms'''
def fonk5(array):
    for b16 in range(len(array)):
        b6 = array[b16]
        b7 = b16 - 1
        while b7 >= 0 and array[b7] > b6:
            array[b7 + 1] = array[b7]
            b7 -= 1
        array[b7 + 1] = b6
def fonk6(array):
    b8 = len(array)
    for b7 in range(b8):
        for b16 in range(1, b8 - b7):
            if array[b16] < array[b16 - 1]:
                array[b16], array[b16 - 1] = array[b16 - 1], array[b16]
def fonk7(array):
    b8 = len(array)
    for b7 in range(b8):
        b9 = b7
        for b16 in range(b7 + 1, b8):
            if array[b16] < array[b9]:
                b9 = b16
        array[b7], array[b9] = array[b9], array[b7]
def fonk8(array):
    def fonk9(array, start, end):
        b10 = start
        while True:
            b11 = 2 * b10 + 1
            if b11 > end:
                break
            if b11 + 1 <= end and array[b11] < array[b11 + 1]:
                b11 += 1
            if array[b10] < array[b11]:
                array[b10], array[b11] = array[b11], array[b10]
                b10 = b11
            else:
                break
    b8 = len(array)
    for start in range((b8 - 2)
        fonk9(array, start, b8 - 1)
    for end in range(b8 - 1, 0, -1):
        array[end], array[0] = array[0], array[end]
        fonk9(array, 0, end - 1)
def fonk10(array):
    if len(array) > 1:
        b12 = len(array)
        b13 = array[:b12]
        b14 = array[b12:]
        fonk10(b13)
        fonk10(b14)
        b7 = b16 = k = 0
        while b7 < len(b13) and b16 < len(b14):
            if b13[b7] < b14[b16]:
                array[k] = b13[b7]
                b7 += 1
            else:
                array[k] = b14[b16]
                b16 += 1
            k += 1
        while b7 < len(b13):
            array[k] = b13[b7]
            b7 += 1
            k += 1
        while b16 < len(b14):
            array[k] = b14[b16]
            b16 += 1
            k += 1
def fonk11(array):
    def fonk12(array, b1, high):
        b15 = array[(b1 + high)
        b7 = b1 - 1
        b16 = high + 1
        while True:
            b7 += 1
            while array[b7] < b15:
                b7 += 1
            b16 -= 1
            while array[b16] > b15:
                b16 -= 1
            if b7 >= b16:
                return b16
            array[b7], array[b16] = array[b16], array[b7]
    def fonk13(array, b1, high):
        if b1 < high:
            b17 = fonk12(array, b1, high)
            fonk13(array, b1, b17)
            fonk13(array, b17 + 1, high)
    fonk13(array, 0, len(array) - 1)
def fonk14(array):
    a1 = 10
    a2 = 1
    b18 = max(array)
    while a2 < b18:
        b19 = [[] for _ in range(a1)]
        for b7 in array:
            b20 = int((b7 / a2) % a1)
            b19[b20].append(b7)
        a3 = 0
        for b in range(a1):
            b21 = b19[b]
            for b7 in b21:
                array[a3] = b7
                a3 += 1
        a2 *= a1
def fonk15(array):
    return sorted(array)
if b22 = = '__main__':
    b23 = list(range(100, 25000, 500))
    b24 = {
        'bubble_sort': [fonk2(bubble_sort, fonk1(b7)) for b7 in tqdm(b23[:10], 'bubble_sort')],
        'selection_sort': [fonk2(selection_sort, fonk1(b7)) for b7 in tqdm(b23[:10], 'selection_sort')],
        'insertion_sort': [fonk2(insertion_sort, fonk1(b7)) for b7 in tqdm(b23[:10], 'insertion_sort')],
        'merge_sort': [fonk2(merge_sort, fonk1(b7)) for b7 in tqdm(b23, 'merge_sort')],
        'heap_sort': [fonk2(heap_sort, fonk1(b7)) for b7 in tqdm(b23, 'heap_sort')],
        'quick_sort': [fonk2(quick_sort, fonk1(b7)) for b7 in tqdm(b23, 'quick_sort')],
        'radix_sort': [fonk2(radix_sort, fonk1(b7)) for b7 in tqdm(b23, 'radix_sort')]
    }
    b25 = {'bubble_sort', 'selection_sort', 'insertion_sort'}
    for sort in b24:
        if sort in b25:
            plt.plot(b23[:10], b24[sort], b26 = sort.replace('_', ' ').title())
        else:
            plt.plot(b23, b24[sort], b26 = sort.replace('_', ' ').title())
    plt.legend(b27 = 'lower right')
    plt.ylabel('Time (seconds)')
    plt.xlabel('List Size')
    plt.show()