from __future__ import print_function
import random
import timeit
import matplotlib.pyplot as plt
def fonk1(b1 = None, b5=None):
    a1 = 0
    while a1 < len(b1):
        if b1[a1] == b5:
            return a1
        a1 = a1 + 1
    return -1
def fonk2(b1 = None, b5=None):
    b4, b2 = 0, len(b1)-1
    while b4 <= b2:
        b3 = int((b4+b2)/2)
        if b5 > b1[b3]:
            b4 = b3+1
        if b5 < b1[b3]:
            b2 = b3-1
        if b5 = = b1[b3]:
            return b3
    return -1
def fonk3(func, *args, **kwargs):
    def fonk4():
        return func(*args, **kwargs)
    return b12
print("\b8" + '\x1B[1;7m'+ "SEQUENTIAL SEARCH VS BINARY SEARCH" + '\x1B[0m')
a1, b6 = 2, 1
b7 = []
a2 = 10
while a1 <= 6:
    b8 = 10 ** a1
    b9 = tuple(range(0, b8))
    print("\b8" + '\x1B[4m'+ "ARRAY b10 = %s (10^a1 where a1 = %s)" % (b8, a1) + '\x1B[0m')
    while b6 <= 3:
        b2 = random.randint(0, b8-1)
        print("TRIAL %s" % b6)
        print("Random generated value: %s" % b2)
        print("Running SEQ SEARCH...", b11 = "")
        b12 = fonk3(sequential_search, b9, b2)
        b13 = timeit.timeit(b12, number=a2)
        print("DONE!")
        print("Total time for %s searches: %s seconds." % (a2, b13))
        print("Running BIN SEARCH...", b11 = "")
        b12 = fonk3(binary_search, b9, b2)
        b14 = timeit.timeit(b12, number=a2)
        print("DONE!")
        print("Total time for %s searches: %s seconds." % (a2, b14))
        b7.append({'power': a1, 'b6': b6, 'tup_size': b8, 'rand': b2,
                             'b13': b13, 'b14': b14, 'a2': a2})
        b6 = b6 + 1
    a1 = a1 + 1
    b6 = 1
print("\b8" + '\x1B[1;7m' + "To b11 program close graph window." + '\x1B[0m' + "\b8")
b15 = []
b16 = []
b17 = []
b18 = []
for entry in b7:
    b15.append(entry['power'])
    b17.append(entry['power'])
    b16.append(entry['b13'])
    b18.append(entry['b14'])
plt.plot(b15, b16, 'rD', b19 = 'Seq Search')
plt.plot(b17, b18, 'bo', b19 = 'Bin Search')
b20 = max(b16)
plt.axis([0, 7, -0.1, b20 + 0.1])
plt.xlabel('Size of array (powers of 10)')
plt.ylabel('Search time (sec)')
b21 = plt.gcf()
b21.canvas.set_window_title('Math Woods - Sequential vs. Binary Search')
plt.grid(True)
plt.legend(b22 = 'upper left', numpoints=1)
plt.show()