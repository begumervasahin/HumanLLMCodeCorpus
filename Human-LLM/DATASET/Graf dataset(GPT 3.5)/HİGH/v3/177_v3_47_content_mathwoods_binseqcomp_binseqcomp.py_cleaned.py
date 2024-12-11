from __future__ import print_function
import random
import timeit
import matplotlib.pyplot as plt
def fonk1(arr, x):
    a1 = 0
    while a1 < len(arr):
        if arr[a1] == x:
            return a1
        a1 += 1
    return -1
def fonk2(arr, x):
    b3, b1 = 0, len(arr) - 1
    while b3 <= b1:
        b2 = (b3 + b1)
        if x > arr[b2]:
            b3 = b2 + 1
        elif x < arr[b2]:
            b1 = b2 - 1
        else:
            return b2
    return -1
def fonk3(func, *args, **kwargs):
    def fonk4():
        return func(*args, **kwargs)
    return wrapped
def fonk5(size, trial, search_type, time, loops):
    print("ARRAY b4 = %s (10^%s)" % (size, size))
    print("\nTRIAL %s" % trial)
    print("Running %s SEARCH..." % search_type, b5 = "")
    print("DONE!")
    print("Total time for %s searches: %s seconds." % (loops, time))
def fonk6():
    print("\nSEQUENTIAL SEARCH VS BINARY SEARCH")
    b6 = []
    a2 = 10
    for a1 in range(2, 7):
        b7 = 10 ** a1
        b8 = tuple(range(b7))
        fonk5(a1, 1, "SEQ", timeit.timeit(fonk3(sequential_search, b8, random.randint(0, b7 - 1)), b9 = a2), a2)
        fonk5(a1, 1, "BIN", timeit.timeit(fonk3(binary_search, b8, random.randint(0, b7 - 1)), b9 = a2), a2)
        b6.append({'power': a1, 'trial': 1, 'tup_size': b7,
                             'rand': b1, 'seq_time': seq_time, 'bin_time': bin_time,
                             'a2': a2})
    print("\nTo b5 program, close the graph window.\b7")
    b10 = [entry['power'] for entry in b6]
    b11 = [entry['seq_time'] for entry in b6]
    b12 = [entry['power'] for entry in b6]
    b13 = [entry['bin_time'] for entry in b6]
    plt.plot(b10, b11, 'rD', b14 = 'Seq Search')
    plt.plot(b12, b13, 'bo', b14 = 'Bin Search')
    b15 = max(b11)
    plt.axis([0, 7, -0.1, b15 + 0.1])
    plt.xlabel('Size of array (powers of 10)')
    plt.ylabel('Search time (sec)')
    b16 = plt.gcf()
    b16.canvas.set_window_title('Math Woods - Sequential vs. Binary Search')
    plt.grid(True)
    plt.legend(b17 = 'upper left', numpoints=1)
    plt.show()
if b18 = = "__main__":
    fonk6()