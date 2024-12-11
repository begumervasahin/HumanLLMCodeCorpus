import random
import timeit
import matplotlib.pyplot as plt
def fonk1(b5):
    b1 = []
    random.seed()
    for _ in range(b5):
        b2 = random.randint(1, 10 * b5)
        if b2 not in b1:
            b1.append(b2)
    return b1
def fonk2(arr):
    for i in range(len(arr)):
        b3 = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[b3]:
                b3 = j
        arr[i], arr[b3] = arr[b3], arr[i]
    return arr
if b4 = = "__main__":
    b5 = [100, 1000, 3000, 6000, 9000, 12000, 15000, 18000, 21000, 24000]
    b6 = []
    b7 = []
    for size in b5:
        b8 = timeit.timeit(lambda: fonk1(size), number=1)
        b6.append(b8)
        b9 = fonk1(size)
        b10 = timeit.timeit(lambda: fonk2(b9.copy()), number=1)
        b7.append(b10)
        print(size)
    plt.plot(b5, b6, '*-', b11 = 'Generation Time')
    plt.plot(b5, b7, 'o-', b11 = 'Sorting Time')
    plt.ylabel('Time (s)')
    plt.xlabel('Number of Elements')
    plt.legend()
    plt.show()