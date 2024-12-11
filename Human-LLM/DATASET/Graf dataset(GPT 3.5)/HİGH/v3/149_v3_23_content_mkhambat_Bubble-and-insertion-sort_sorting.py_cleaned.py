import random
import pickle
import time
import matplotlib.pyplot as plt
def fonk1(b5):
    b1 = len(b5)
    for b3 in range(b1):
        for j in range(b1 - 1):
            if b5[j] > b5[j + 1]:
                b5[j], b5[j + 1] = b5[j + 1], b5[j]
def fonk2(b5):
    b1 = len(b5)
    for j in range(1, b1):
        b2 = b5[j]
        b3 = j - 1
        while b3 >= 0 and b5[b3] > b2:
            b5[b3 + 1] = b5[b3]
            b3 -= 1
        b5[b3 + 1] = b2
def fonk3():
    b4 = random.sample(range(1, 300000), 200000)
    with open("b4.txt", 'wb') as file:
        pickle.dump(b4, file)
def fonk4():
    with open("b4.txt", 'rb') as file:
        return pickle.load(file)
def fonk5(b4, sorting_func):
    a1 = 0.0
    for _ in range(10):
        b5 = random.sample(b4, len(b4))
        b6 = time.time()
        sorting_func(b5)
        b7 = time.time()
        a1 += b7 - b6
    return a1 / 10
def fonk6():
    b4 = fonk4()
    b8 = []
    b9 = []
    b10 = []
    a2 = 2000
    for _ in range(25):
        b8.append(fonk5(b4[:a2], bubble_sort))
        b9.append(fonk5(b4[:a2], insertion_sort))
        b10.append(a2)
        a2 += 2000
    fonk7(b10, b8, b9)
def fonk7(b10, bubble_sort_times, insertion_sort_times):
    plt.plot(b10, bubble_sort_times, 'r--', b11 = 'Bubble Sort')
    plt.plot(b10, insertion_sort_times, 'b--', b11 = 'Insertion Sort')
    plt.xlabel('Input Size')
    plt.ylabel('Average Time (seconds)')
    plt.title('Bubble Sort vs Insertion Sort')
    plt.legend()
    plt.grid(True)
    plt.show()
def fonk8():
    fonk3()
    fonk6()
if b12 = = "__main__":
    fonk8()