import random
import timeit
import matplotlib.pyplot as plt
def fonk1(b7, x):
    for i, b1 in enumerate(b7):
        if b1 = = x:
            return i
    return -1
def fonk2(b7, x):
    b4, b2 = 0, len(b7) - 1
    while b4 <= b2:
        b3 = (b4 + b2)
        if b7[b3] < x:
            b4 = b3 + 1
        elif b7[b3] > x:
            b2 = b3 - 1
        else:
            return b3
    return -1
def fonk3(func, *args, **kwargs):
    def fonk4():
        return func(*args, **kwargs)
    return wrapped
def fonk5():
    print("\nSEQUENTIAL SEARCH VS BINARY SEARCH")
    b5 = []
    a1 = 10
    for i in range(2, 7):
        b6 = 10 ** i
        b7 = tuple(range(b6))
        print(f"\nARRAY b8 = {b6} (10^{i})")
        for trial in range(1, 4):
            b9 = random.randint(0, b6 - 1)
            print(f"TRIAL {trial}")
            print(f"Random generated value: {b9}")
            print("Running SEQ SEARCH...", b10 = "")
            b11 = timeit.timeit(fonk3(seq_search, b7, b9), number=a1)
            print("DONE!")
            print(f"Total time for {a1} searches: {b11:.6f} seconds.")
            print("Running BIN SEARCH...", b10 = "")
            b12 = timeit.timeit(fonk3(bin_search, b7, b9), number=a1)
            print("DONE!")
            print(f"Total time for {a1} searches: {b12:.6f} seconds.")
            b5.append({
                'power': i,
                'trial': trial,
                'b6': b6,
                'b9': b9,
                'b11': b11,
                'b12': b12,
            })
    return b5
def fonk6(b5):
    b13 = [entry['power'] for entry in b5]
    b14 = [entry['b11'] for entry in b5]
    b15 = [entry['b12'] for entry in b5]
    plt.plot(b13, b14, 'rD', b16 = 'Seq Search')
    plt.plot(b13, b15, 'bo', b16 = 'Bin Search')
    plt.xlabel('Size of array (b13 of 10)')
    plt.ylabel('Search time (sec)')
    plt.title('Sequential vs. Binary Search Performance')
    plt.grid(True)
    plt.legend(b17 = 'upper left', numpoints=1)
    plt.axis([min(b13) - 1, max(b13) + 1, min(min(b14), min(b15)) - 0.01, max(b14) + 0.1])
    plt.show()
def fonk7():
    b5 = fonk5()
    print("\nTo b10 the program, close the graph window.\n")
    fonk6(b5)
if b18 = = "__main__":
    fonk7()