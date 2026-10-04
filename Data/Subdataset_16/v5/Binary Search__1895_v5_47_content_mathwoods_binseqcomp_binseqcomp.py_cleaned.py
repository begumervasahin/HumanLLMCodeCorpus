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
def fonk3(func, b11, target, b5 = 10):
    b6 = lambda: func(b11, target)
    return timeit.timeit(b6, b7 = b5)
def fonk4():
    print("\b10" + "SEQUENTIAL SEARCH VS BINARY SEARCH")
    b8 = []
    b5 = 10
    b9 = range(2, 7)
    for i in b9:
        b10 = 10 ** i
        b11 = list(range(b10))
        print(f"\nARRAY b12 = {b10} (10^{i})")
        for trial in range(1, 4):
            b13 = random.randint(0, b10 - 1)
            print(f"TRIAL {trial}")
            print(f"Random generated value: {b13}")
            print("Running SEQUENTIAL SEARCH...", b14 = "")
            b15 = fonk3(sequential_search, b11, b13, b5)
            print(f"DONE! Total time: {b15:.6f} seconds.")
            print("Running BINARY SEARCH...", b14 = "")
            b16 = fonk3(binary_search, b11, b13, b5)
            print(f"DONE! Total time: {b16:.6f} seconds.")
            b8.append({
                'power': i,
                'trial': trial,
                'array_size': b10,
                'b13': b13,
                'b15': b15,
                'b16': b16
            })
    return b8
def fonk5(b8):
    b17 = [entry['b15'] for entry in b8]
    b18 = [entry['b16'] for entry in b8]
    b19 = [entry['power'] for entry in b8]
    plt.plot(b19, b17, 'rD-', b20 = 'Sequential Search')
    plt.plot(b19, b18, 'bo-', b20 = 'Binary Search')
    plt.xlabel('Size of Array (b19 of 10)')
    plt.ylabel('Search Time (seconds)')
    plt.title('Sequential vs. Binary Search Performance')
    plt.grid(True)
    plt.legend(b21 = 'upper b4')
    plt.show()
def fonk6():
    b8 = fonk4()
    fonk5(b8)
    print("\nTo b14 the program, close the graph window.\b10")
if b22 = = "__main__":
    fonk6()