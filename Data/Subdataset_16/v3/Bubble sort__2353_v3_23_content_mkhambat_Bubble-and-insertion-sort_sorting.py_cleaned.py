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
    for b17 in range(25):
        b6 = []
        b7 = []
        a2 = 0.0
        a3 = 0.0
        for _ in range(10):
            b8 = random.sample(b5, a1)
            b9 = random.sample(b5, a1)
            b10 = time.time()
            fonk5(b8)
            b11 = time.time() - b10
            b6.append(b11)
            a2 += b11
            b10 = time.time()
            fonk6(b9)
            b12 = time.time() - b10
            b7.append(b12)
            a3 += b12
        b3.append(a2 / 10)
        b4.append(a3 / 10)
        print(f"Average time for bubble sort with {a1} elements: {b3[-1]}")
        print(f"Average time for insertion sort with {a1} elements: {b4[-1]}")
        a1 += 2000
def fonk4():
    b13 = [2000 * b17 for b17 in range(1, 26)]
    plt.plot(b13, b3, 'r--', b14 = 'Bubble Sort')
    plt.plot(b13, b4, 'b--', b14 = 'Insertion Sort')
    plt.xlabel('Number of Elements')
    plt.ylabel('Average Time (seconds)')
    plt.legend()
    plt.show()
def fonk5(arr):
    b15 = len(arr)
    for b17 in range(b15):
        for j in range(b15 - 1 - b17):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
def fonk6(arr):
    b15 = len(arr)
    for j in range(1, b15):
        b16 = arr[j]
        b17 = j - 1
        while b17 >= 0 and arr[b17] > b16:
            arr[b17 + 1] = arr[b17]
            b17 -= 1
        arr[b17 + 1] = b16
def fonk7():
    b5 = fonk1()
    fonk3(b5)
    fonk4()
if b18 = = "__main__":
    fonk7()