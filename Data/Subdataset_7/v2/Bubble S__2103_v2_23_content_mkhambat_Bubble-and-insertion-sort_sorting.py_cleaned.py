import random
import pickle
import time
import matplotlib.pyplot as plt
def fonk1(arr):
    b1 = len(arr)
    for b3 in range(b1):
        for j in range(b1 - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
def fonk2(arr):
    b1 = len(arr)
    for j in range(1, b1):
        b2 = arr[j]
        b3 = j - 1
        while b3 >= 0 and arr[b3] > b2:
            arr[b3 + 1] = arr[b3]
            b3 -= 1
        arr[b3 + 1] = b2
def fonk3():
    b4 = random.sample(range(1, 300000), 200000)
    with open("b4.txt", 'wb') as file:
        pickle.dump(b4, file)
def fonk4():
    with open("b4.txt", 'rb') as file:
        b4 = pickle.load(file)
    b5 = []
    b6 = []
    b7 = []
    a1 = 2000
    for _ in range(25):
        a2 = 0.0
        a3 = 0.0
        for _ in range(10):
            b8 = random.sample(b4, a1)
            b9 = random.sample(b4, a1)
            b10 = time.time()
            fonk1(b8)
            b11 = time.time()
            a2 += b11 - b10
            b10 = time.time()
            fonk2(b9)
            b11 = time.time()
            a3 += b11 - b10
        b5.append(a2 / 10)
        b6.append(a3 / 10)
        b7.append(a1)
        a1 += 2000
    fonk5(b7, b5, b6)
def fonk5(b7, bubble_sort_times, insertion_sort_times):
    plt.plot(b7, bubble_sort_times, 'r--', b12 = 'Bubble Sort')
    plt.plot(b7, insertion_sort_times, 'b--', b12 = 'Insertion Sort')
    plt.xlabel('Input Size')
    plt.ylabel('Average Time (seconds)')
    plt.title('Bubble Sort vs Insertion Sort')
    plt.legend()
    plt.grid(True)
    plt.show()
def fonk6():
    fonk3()
    fonk4()
if b13 = = "__main__":
    fonk6()