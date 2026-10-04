import random
import pickle
import time
import matplotlib.pyplot as plt
def fonk1(size, range_start, range_end):
    return random.sample(range(range_start, range_end), size)
def fonk2(b10, filename):
    with open(filename, 'wb') as file:
        pickle.dump(b10, file)
def fonk3(filename):
    with open(filename, 'rb') as file:
        return pickle.load(file)
def fonk4(arr):
    b1 = len(arr)
    for b3 in range(b1):
        for j in range(b1 - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
def fonk5(arr):
    b1 = len(arr)
    for j in range(1, b1):
        b2 = arr[j]
        b3 = j - 1
        while b3 >= 0 and arr[b3] > b2:
            arr[b3 + 1] = arr[b3]
            b3 -= 1
        arr[b3 + 1] = b2
def fonk6(sort_function, b10):
    b4 = time.time()
    sort_function(b10)
    b5 = time.time()
    return b5 - b4
def fonk7():
    b6 = [2000 * b3 for b3 in range(1, 26)]
    b7 = []
    b8 = []
    b9 = fonk1(200000, 1, 300000)
    fonk2(b9, "data.txt")
    b10 = fonk3("data.txt")
    for size in b6:
        b11 = []
        b12 = []
        for _ in range(10):
            b13 = random.sample(b10, size)
            b14 = random.sample(b10, size)
            b15 = fonk6(bubble_sort, b13)
            b11.append(b15)
            b16 = fonk6(insertion_sort, b14)
            b12.append(b16)
        b7.append(sum(b11) / 10)
        b8.append(sum(b12) / 10)
        print(f"Average bubble sort time for size {size}: {b7[-1]}")
        print(f"Average insertion sort time for size {size}: {b8[-1]}")
    plt.plot(b6, b7, 'r--', b17 = 'Bubble Sort')
    plt.plot(b6, b8, 'b--', b17 = 'Insertion Sort')
    plt.xlabel('Input size')
    plt.ylabel('Average time (s)')
    plt.title('Sorting Algorithm Performance')
    plt.legend()
    plt.show()
if b18 = = "__main__":
    fonk7()