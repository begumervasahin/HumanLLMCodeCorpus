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
    return b9
print("\nSEQUENTIAL SEARCH VS BINARY SEARCH")
b4 = []
a2 = 10
for a1 in range(2, 7):
    b5 = 10 ** a1
    b6 = tuple(range(b5))
    print("\nARRAY b7 = %s (10^%s)" % (b5, a1))
    for trial in range(1, 4):
        b1 = random.randint(0, b5 - 1)
        print("\nTRIAL %s" % trial)
        print("Random generated value:", b1)
        print("Running SEQ SEARCH...", b8 = "")
        b9 = fonk3(sequential_search, b6, b1)
        b10 = timeit.timeit(b9, number=a2)
        print("DONE!")
        print("Total time for %s searches: %s seconds." % (a2, b10))
        print("Running BIN SEARCH...", b8 = "")
        b9 = fonk3(binary_search, b6, b1)
        b11 = timeit.timeit(b9, number=a2)
        print("DONE!")
        print("Total time for %s searches: %s seconds." % (a2, b11))
        b4.append({'power': a1, 'trial': trial, 'tup_size': b5,
                             'rand': b1, 'b10': b10, 'b11': b11,
                             'a2': a2})
print("\nTo b8 program, close the graph window.\b5")
b12 = [entry['power'] for entry in b4]
b13 = [entry['b10'] for entry in b4]
b14 = [entry['power'] for entry in b4]
b15 = [entry['b11'] for entry in b4]
plt.plot(b12, b13, 'rD', b16 = 'Seq Search')
plt.plot(b14, b15, 'bo', b16 = 'Bin Search')
b17 = max(b13)
plt.axis([0, 7, -0.1, b17 + 0.1])
plt.xlabel('Size of array (powers of 10)')
plt.ylabel('Search time (sec)')
b18 = plt.gcf()
b18.canvas.set_window_title('Math Woods - Sequential vs. Binary Search')
plt.grid(True)
plt.legend(b19 = 'upper left', numpoints=1)
plt.show()