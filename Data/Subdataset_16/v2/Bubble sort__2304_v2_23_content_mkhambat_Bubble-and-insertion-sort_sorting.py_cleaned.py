import random
import pickle
import time
import matplotlib.pyplot as plt
b1 = []
b2 = []
b3 = []
b4 = []
def fonk1():
    b5 = random.sample(range(1, 300000), 200000)
    with open("data.txt", 'wb') as fp:
        pickle.dump(b5, fp)
    return b5
def fonk2():
    with open("data.txt", 'rb') as fp:
        b5 = pickle.load(fp)
    return b5
def fonk3(b5):
    a1 = 2000
    for b18 in range(25):
        b1 = []
        b2 = []
        a2 = 0.0
        a3 = 0.0
        for _ in range(10):
            b6 = random.sample(b5, a1)
            b7 = random.sample(b5, a1)
            b8 = time.time()
            fonk5(b6)
            b9 = time.time()
            b10 = b9 - b8
            b1.append(b10)
            a2 += b10
            b11 = time.time()
            fonk6(b7)
            b12 = time.time()
            b13 = b12 - b11
            b2.append(b13)
            a3 += b13
        b3.append(a2 / 10)
        b4.append(a3 / 10)
        print(f"Average time for bubble sort with {a1} elements: {b3[-1]}")
        print(f"Average time for insertion sort with {a1} elements: {b4[-1]}")
        a1 += 2000
def fonk4():
    b14 = [2000 * b18 for b18 in range(1, 26)]
    plt.plot(b14, b3, 'r--', b15 = 'Bubble Sort')
    plt.plot(b14, b4, 'b--', b15 = 'Insertion Sort')
    plt.xlabel('Number of Elements')
    plt.ylabel('Average Time (seconds)')
    plt.legend()
    plt.show()
def fonk5(arr):
    b16 = len(arr)
    for b18 in range(b16):
        for j in range(b16 - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
def fonk6(arr):
    b16 = len(arr)
    for j in range(1, b16):
        b17 = arr[j]
        b18 = j - 1
        while b18 >= 0 and arr[b18] > b17:
            arr[b18 + 1] = arr[b18]
            b18 -= 1
        arr[b18 + 1] = b17
def fonk7():
    b5 = fonk1()
    fonk3(b5)
    fonk4()
if b19 = = "__main__":
    fonk7()