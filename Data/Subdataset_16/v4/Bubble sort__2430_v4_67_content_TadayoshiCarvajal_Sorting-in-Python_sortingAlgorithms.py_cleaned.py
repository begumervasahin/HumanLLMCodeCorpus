from matplotlib import pyplot as plt
from tqdm import tqdm
from random import randint, shuffle
from time import time
def fonk1(b11, b1 = 0, high=100):
    return [randint(b1, high) for _ in range(b11)]
def fonk2(sort_function, b19):
    shuffle(b19)
    b2 = time()
    sort_function(b19)
    b3 = time()
    return b3 - b2
def fonk3(sort_function, b19, b4 = 500):
    a1 = 0
    for _ in range(b4):
        a1 += fonk2(sort_function, b19)
    return a1 / b4
def fonk4(b19):
    for b5 in range(1, len(b19)):
        if b19[b5] < b19[b5-1]:
            return False
    return True
def fonk5(b19):
    for b7 in range(len(b19)):
        key, b5 = b19[b7], b7 - 1
        while b5 >= 0 and b19[b5] > key:
            b19[b5 + 1], b5 = b19[b5], b5 - 1
        b19[b5 + 1] = key
    return b19
def fonk6(b19):
    b6 = True
    b7 = len(b19)
    while b6:
        b6 = False
        for b5 in range(1, b7):
            if b19[b5] < b19[b5-1]:
                b19[b5], b19[b5-1] = b19[b5-1], b19[b5]
                b6 = True
        b7 -= 1
    return b19
def fonk7(b19):
    for k in range(len(b19)):
        min_value, b8 = float('inf'), -1
        for b7 in range(k, len(b19)):
            if b19[b7] < min_value:
                min_value, b8 = b19[b7], b7
        b19[k], b19[b8] = b19[b8], b19[k]
    return b19
def fonk8(b19):
    def fonk9(b19, b10, upto):
        b9 = 2 * b10 + 1
        while b9 < upto:
            if b9 + 1 < upto and b19[b9] < b19[b9 + 1]:
                b9 += 1
            if b19[b9] > b19[b10]:
                b19[b9], b19[b10] = b19[b10], b19[b9]
                b10 = b9
                b9 = 2 * b10 + 1
            else:
                break
    b11 = len(b19)
    for b5 in range(b11
        fonk9(b19, b5, b11)
    for b5 in range(b11 - 1, 0, -1):
        b19[0], b19[b5] = b19[b5], b19[0]
        fonk9(b19, 0, b5)
    return b19
def fonk10(b19):
    if len(b19) > 1:
        b12 = len(b19)
        left_half, b13 = b19[:b12], b19[b12:]
        fonk10(left_half)
        fonk10(b13)
        b5 = b7 = k = 0
        while b5 < len(left_half) and b7 < len(b13):
            if left_half[b5] < b13[b7]:
                b19[k] = left_half[b5]
                b5 += 1
            else:
                b19[k] = b13[b7]
                b7 += 1
            k += 1
        while b5 < len(left_half):
            b19[k] = left_half[b5]
            b5 += 1
            k += 1
        while b7 < len(b13):
            b19[k] = b13[b7]
            b7 += 1
            k += 1
    return b19
def fonk11(b19):
    def fonk12(b19, first, last):
        if first < last:
            b14 = fonk13(b19, first, last)
            fonk12(b19, first, b14 - 1)
            fonk12(b19, b14 + 1, last)
    def fonk13(b19, first, last):
        pivot, left_mark, b15 = b19[first], first + 1, last
        b16 = False
        while not b16:
            while left_mark <= b15 and b19[left_mark] <= pivot:
                left_mark += 1
            while b15 >= left_mark and b19[b15] >= pivot:
                b15 -= 1
            if b15 < left_mark:
                b16 = True
            else:
                b19[left_mark], b19[b15] = b19[b15], b19[left_mark]
        b19[first], b19[b15] = b19[b15], b19[first]
        return b15
    fonk12(b19, 0, len(b19) - 1)
    return b19
def fonk14(b19):
    mod, b17 = 10, 1
    while True:
        b18 = [[] for _ in range(10)]
        for b11 in b19:
            b18[(b11 % mod)
        mod, b17 = mod * 10, b17 * 10
        if len(b18[0]) == len(b19):
            return b18[0]
        b19 = [y for x in b18 for y in x]
def fonk15(b19):
    return sorted(b19)
if b20 = = '__main__':
    b21 = [b5 for b5 in range(100, 25000, 500)]
    b22 = {
        'Bubble Sort': bubble_sort,
        'Selection Sort': selection_sort,
        'Insertion Sort': insertion_sort,
        'Merge Sort': merge_sort,
        'Heap Sort': heap_sort,
        'Quick Sort': quick_sort,
        'Radix Sort': radix_sort
    }
    b23 = {}
    for name, func in b22.items():
        if name in {'Bubble Sort', 'Selection Sort', 'Insertion Sort'}:
            b23[name] = [fonk2(func, fonk1(size)) for size in tqdm(b21[:10], b24 = name)]
        else:
            b23[name] = [fonk2(func, fonk1(size)) for size in tqdm(b21, b24 = name)]
    for name, times in b23.items():
        if name in {'Bubble Sort', 'Selection Sort', 'Insertion Sort'}:
            plt.plot(b21[:10], times, b25 = name)
        else:
            plt.plot(b21, times, b25 = name)
    plt.legend(b26 = 'lower right')
    plt.ylabel('Time (seconds)')
    plt.xlabel('List Size')
    plt.title('Sorting Algorithm Performance')
    plt.show()