from __future__ import print_function
import random
import timeit
import matplotlib.pyplot as plt
def fonk1(arr, x):
    for i, b1 in enumerate(arr):
        if b1 = = x:
            return i
    return -1
def fonk2(arr, x):
    b4, b2 = 0, len(arr) - 1
    while b4 <= b2:
        b3 = (b4 + b2)
        if x > arr[b3]:
            b4 = b3 + 1
        elif x < arr[b3]:
            b2 = b3 - 1
        else:
            return b3
    return -1
def fonk3(func, *args, **kwargs):
    def fonk4():
        return func(*args, **kwargs)
    return wrapped
def fonk5():
    print("\b7" + '\x1B[1;7m' + "SEQUENTIAL SEARCH VS BINARY SEARCH" + '\x1B[0m')
    b5 = []
    a1 = 10
    b6 = range(2, 7)
    for i in b6:
        b7 = 10 ** i
        b8 = tuple(range(0, b7))
        print("\b7" + '\x1B[4m' + f"ARRAY b9 = {b7} (10^{i})" + '\x1B[0m')
        for trial in range(1, 4):
            b10 = random.randint(0, b7 - 1)
            print(f"TRIAL {trial}")
            print(f"Random generated value: {b10}")
            print("Running SEQ SEARCH...", b11 = "")
            b12 = timeit.timeit(fonk3(sequential_search, b8, b10), number=a1)
            print("DONE!")
            print(f"Total time for {a1} searches: {b12} seconds.")
            print("Running BIN SEARCH...", b11 = "")
            b13 = timeit.timeit(fonk3(binary_search, b8, b10), number=a1)
            print("DONE!")
            print(f"Total time for {a1} searches: {b13} seconds.")
            b5.append({
                'power': i,
                'trial': trial,
                'array_size': b7,
                'b10': b10,
                'seq_time': b12,
                'bin_time': b13
            })
    return b5
def fonk6(b5):
    b14 = [entry['power'] for entry in b5]
    b15 = [entry['seq_time'] for entry in b5]
    b16 = [entry['power'] for entry in b5]
    b17 = [entry['bin_time'] for entry in b5]
    plt.plot(b14, b15, 'rD', b18 = 'Sequential Search')
    plt.plot(b16, b17, 'bo', b18 = 'Binary Search')
    plt.axis([0, 7, -0.1, max(b15) + 0.1])
    plt.xlabel('Size of Array (powers of 10)')
    plt.ylabel('Search Time (seconds)')
    plt.title('Sequential vs. Binary Search Performance')
    plt.grid(True)
    plt.legend(b19 = 'upper b4')
    plt.show()
def fonk7():
    b5 = fonk5()
    fonk6(b5)
    print("\b7" + '\x1B[1;7m' + "To b11 program, close graph window." + '\x1B[0m' + "\b7")
if b20 = = "__main__":
    fonk7()