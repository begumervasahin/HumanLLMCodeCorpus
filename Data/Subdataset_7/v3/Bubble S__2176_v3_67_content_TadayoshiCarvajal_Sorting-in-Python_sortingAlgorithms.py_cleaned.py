from matplotlib import pyplot as plt
from tqdm import tqdm
import random
import time
def fonk1(b8, b1 = 0, high=100):
    return [random.randint(1, b8) for _ in range(b8)]
def fonk2(sort_function, array):
    b2 = array.copy()
    random.shuffle(b2)
    b3 = time.time()
    sort_function(b2)
    b4 = time.time()
    return b4 - b3
def fonk3(sort_function, array, b5 = 500):
    a1 = 0
    for _ in range(b5):
        a1 += fonk2(sort_function, array)
    return a1 / b5
def fonk4(array):
    for b7 in range(1, len(array)):
        if array[b7] < array[b7 - 1]:
            return False
    return True
def fonk5(array):
    for b16 in range(len(array)):
        b6 = array[b16]
        b7 = b16 - 1
        while b7 >= 0 and array[b7] > b6:
            array[b7 + 1] = array[b7]
            b7 -= 1
        array[b7 + 1] = b6
    return array
def fonk6(array):
    b8 = len(array)
    for _ in range(b8):
        for b16 in range(1, b8):
            if array[b16] < array[b16 - 1]:
                array[b16], array[b16 - 1] = array[b16 - 1], array[b16]
    return array
def fonk7(array):
    b8 = len(array)
    for b7 in range(b8):
        b9 = b7
        for b16 in range(b7 + 1, b8):
            if array[b16] < array[b9]:
                b9 = b16
        array[b7], array[b9] = array[b9], array[b7]
    return array
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
    for start in range(b8
        fonk9(array, start, b8 - 1)
    for end in range(b8 - 1, 0, -1):
        array[end], array[0] = array[0], array[end]
        fonk9(array, 0, end - 1)
    return array
def fonk10(array):
    if len(array) <= 1:
        return array
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
    return array
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
    return array
def fonk14(array):
    a2 = 10
    a3 = 1
    b18 = max(array)
    while a3 < b18:
        b19 = [[] for _ in range(a2)]
        for num in array:
            b20 = int((num / a3) % a2)
            b19[b20].append(num)
        a4 = 0
        for b in range(a2):
            for b7 in b19[b]:
                array[a4] = b7
                a4 += 1
        a3 *= a2
    return array
def fonk15(array):
    return sorted(array)
if b21 = = '__main__':
    b22 = list(range(100, 25000, 500))
    b23 = {
        'Bubble Sort': [fonk3(bubble_sort, fonk1(b7)) for b7 in tqdm(b22[:10], 'Bubble Sort')],
        'Selection Sort': [fonk3(selection_sort, fonk1(b7)) for b7 in tqdm(b22[:10], 'Selection Sort')],
        'Insertion Sort': [fonk3(insertion_sort, fonk1(b7)) for b7 in tqdm(b22[:10], 'Insertion Sort')],
        'Merge Sort': [fonk3(merge_sort, fonk1(b7)) for b7 in tqdm(b22, 'Merge Sort')],
        'Heap Sort': [fonk3(heap_sort, fonk1(b7)) for b7 in tqdm(b22, 'Heap Sort')],
        'Quick Sort': [fonk3(quick_sort, fonk1(b7)) for b7 in tqdm(b22, 'Quick Sort')],
        'Radix Sort': [fonk3(radix_sort, fonk1(b7)) for b7 in tqdm(b22, 'Radix Sort')]
    }
    b24 = {'Bubble Sort', 'Selection Sort', 'Insertion Sort'}
    for sort_name, sort_times_list in b23.items():
        if sort_name in b24:
            plt.plot(b22[:10], sort_times_list, b25 = sort_name)
        else:
            plt.plot(b22, sort_times_list, b25 = sort_name)
    plt.legend(b26 = 'lower right')
    plt.ylabel('Time (seconds)')
    plt.xlabel('List Size')
    plt.show()