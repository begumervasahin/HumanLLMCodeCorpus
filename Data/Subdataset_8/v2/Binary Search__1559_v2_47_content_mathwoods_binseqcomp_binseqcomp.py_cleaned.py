from __future__ import print_function
import random
import timeit
import matplotlib.pyplot as plt
def sequential_search(arr, x):
    i = 0
    while i < len(arr):
        if arr[i] == x:
            return i
        i += 1
    return -1
def binary_search(arr, x):
    l, r = 0, len(arr) - 1
    while l <= r:
        m = (l + r)
        if x > arr[m]:
            l = m + 1
        elif x < arr[m]:
            r = m - 1
        else:
            return m
    return -1
def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped
print("\nSEQUENTIAL SEARCH VS BINARY SEARCH")
list_results = []
timeit_loops = 10
for i in range(2, 7):
    n = 10 ** i
    tup_num = tuple(range(n))
    print("\nARRAY SIZE = %s (10^%s)" % (n, i))
    for trial in range(1, 4):
        r = random.randint(0, n - 1)
        print("\nTRIAL %s" % trial)
        print("Random generated value:", r)
        print("Running SEQ SEARCH...", end="")
        wrapped = wrapper(sequential_search, tup_num, r)
        seq_time = timeit.timeit(wrapped, number=timeit_loops)
        print("DONE!")
        print("Total time for %s searches: %s seconds." % (timeit_loops, seq_time))
        print("Running BIN SEARCH...", end="")
        wrapped = wrapper(binary_search, tup_num, r)
        bin_time = timeit.timeit(wrapped, number=timeit_loops)
        print("DONE!")
        print("Total time for %s searches: %s seconds." % (timeit_loops, bin_time))
        list_results.append({'power': i, 'trial': trial, 'tup_size': n,
                             'rand': r, 'seq_time': seq_time, 'bin_time': bin_time,
                             'timeit_loops': timeit_loops})
print("\nTo end program, close the graph window.\n")
lst_xcoordseq = [entry['power'] for entry in list_results]
lst_ycoordseq = [entry['seq_time'] for entry in list_results]
lst_xcoordbin = [entry['power'] for entry in list_results]
lst_ycoordbin = [entry['bin_time'] for entry in list_results]
plt.plot(lst_xcoordseq, lst_ycoordseq, 'rD', label='Seq Search')
plt.plot(lst_xcoordbin, lst_ycoordbin, 'bo', label='Bin Search')
ymax = max(lst_ycoordseq)
plt.axis([0, 7, -0.1, ymax + 0.1])
plt.xlabel('Size of array (powers of 10)')
plt.ylabel('Search time (sec)')
fig = plt.gcf()
fig.canvas.set_window_title('Math Woods - Sequential vs. Binary Search')
plt.grid(True)
plt.legend(loc='upper left', numpoints=1)
plt.show()