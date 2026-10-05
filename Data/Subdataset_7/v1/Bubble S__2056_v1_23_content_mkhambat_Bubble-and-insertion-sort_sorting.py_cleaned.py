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
    with open("data.txt", 'wb') as fp:
        pickle.dump(b4, fp)
def fonk4():
    with open("data.txt", 'rb') as fp:
        b4 = pickle.load(fp)
    b5 = []
    b6 = []
    b7 = []
    b8 = []
    b9 = []
    a1 = 2000
    for _ in range(25):
        b5.clear()
        b6.clear()
        a2 = 0.0
        a3 = 0.0
        for _ in range(10):
            b10 = random.sample(b4, a1)
            b11 = random.sample(b4, a1)
            b12 = time.time()
            fonk1(b10)
            b13 = time.time()
            b14 = b13 - b12
            b5.append(b14)
            a2 += b14
            b15 = time.time()
            fonk2(b11)
            b16 = time.time()
            b17 = b16 - b15
            b6.append(b17)
            a3 += b17
        b7.append(a2 / 10)
        b8.append(a3 / 10)
        a1 += 2000
    for b3 in range(1, 26):
        b9.append(2000 * b3)
    plt.plot(b9, b7, 'r--', b9, b8, 'b--')
    plt.xlabel('Input Size')
    plt.ylabel('Average Time')
    plt.title('Bubble Sort vs Insertion Sort')
    plt.legend(['Bubble Sort', 'Insertion Sort'])
    plt.show()
def fonk5():
    fonk3()
    fonk4()
if b18 = = "__main__":
    fonk5()