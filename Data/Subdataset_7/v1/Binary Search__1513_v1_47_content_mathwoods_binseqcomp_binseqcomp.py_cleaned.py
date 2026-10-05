from __future__ import print_function
import random
import timeit
import matplotlib.pyplot as plt
def fonk1(arr, x):
    a1 = 0
    while a1 < len(arr):
        if arr[a1] == x:
            return a1
        a1 = a1 + 1
    return -1
def fonk2(arr, x):
    b3, b1 = 0, len(arr)-1
    while b3 <= b1:
        b2 = int((b3+b1)/2)
        if x > arr[b2]:
            b3 = b2+1
        elif x < arr[b2]:
            b1 = b2-1
        else:
            return b2
    return -1
def fonk3(func, *args, **kwargs):
    def fonk4():
        return func(*args, **kwargs)
    return b10
print("\nSEQUENTIAL SEARCH VS BINARY SEARCH")
a1, b4 = 2, 1
b5 = []
a2 = 10
while a1 <= 6:
    b6 = 10**a1
    b7 = tuple(range(0, b6))
    print("\nARRAY b8 = %s (10^a1 where a1 = %s)" % (b6, a1))
    while b4 <= 3:
        b1 = random.randint(0, b6-1)
        print("TRIAL %s" % b4)
        print("Random generated value: %s" % b1)
        print("Running SEQ SEARCH...", b9 = "")
        b10 = fonk3(seq_search, b7, b1)
        b11 = timeit.timeit(b10, number=a2)
        print("DONE!")
        print("Total time for %s searches: %s seconds." % (a2, b11))
        print("Running BIN SEARCH...", b9 = "")
        b10 = fonk3(bin_search, b7, b1)
        b12 = timeit.timeit(b10, number=a2)
        print("DONE!")
        print("Total time for %s searches: %s seconds." % (a2, b12))
        b5.append({'power': a1, 'b4': b4, 'tup_size': b6,
                             'rand': b1, 'b11': b11, 'b12': b12,
                             'a2': a2})
        b4 = b4 + 1
    a1 = a1 + 1
    b4 = 1
print("\nTo b9 program close graph window.\b6")
b13 = []
b14 = []
b15 = []
b16 = []
for entry in b5:
    b13.append(entry['power'])
    b15.append(entry['power'])
    b14.append(entry['b11'])
    b16.append(entry['b12'])
plt.plot(b13, b14, 'rD', b17 = 'Seq Search')
plt.plot(b15, b16, 'bo', b17 = 'Bin Search')
b18 = max(b14)
plt.axis([0, 7, -0.1, b18 + 0.1])
plt.xlabel('Size of array (powers of 10)')
plt.ylabel('Search time (sec)')
b19 = plt.gcf()
b19.canvas.set_window_title('Math Woods - Sequential vs. Binary Search')
plt.grid(True)
plt.legend(b20 = 'upper left', numpoints=1)
plt.show()