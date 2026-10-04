import random
import timeit
import matplotlib.pyplot as plt
def seq_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1
def bin_search(arr, x):
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
i, trial = 2, 1
list_results = []
timeit_loops = 10
while i <= 6:
    n = 10**i
    tup_num = tuple(range(0, n))
    print(f"\nARRAY SIZE = {n} (10^{i})")
    while trial <= 3:
        r = random.randint(0, n-1)
        print(f"TRIAL {trial}")
        print(f"Random generated value: {r}")
        print("Running SEQ SEARCH...", end="")
        wrapped = wrapper(seq_search, tup_num, r)
        seq_time = timeit.timeit(wrapped, number=timeit_loops)
        print("DONE!")
        print(f"Total time for {timeit_loops} searches: {seq_time:.6f} seconds.")
        print("Running BIN SEARCH...", end="")
        wrapped = wrapper(bin_search, tup_num, r)
        bin_time = timeit.timeit(wrapped, number=timeit_loops)
        print("DONE!")
        print(f"Total time for {timeit_loops} searches: {bin_time:.6f} seconds.")
        list_results.append({
            'power': i,
            'trial': trial,
            'tup_size': n,
            'rand': r,
            'seq_time': seq_time,
            'bin_time': bin_time,
            'timeit_loops': timeit_loops
        })
        trial += 1
    i += 1
    trial = 1
print("\nTo end program, close the graph window.\n")
lst_xcoordseq = []
lst_ycoordseq = []
lst_xcoordbin = []
lst_ycoordbin = []
for entry in list_results:
    lst_xcoordseq.append(entry['power'])
    lst_xcoordbin.append(entry['power'])
    lst_ycoordseq.append(entry['seq_time'])
    lst_ycoordbin.append(entry['bin_time'])
plt.plot(lst_xcoordseq, lst_ycoordseq, 'rD', label='Seq Search')
plt.plot(lst_xcoordbin, lst_ycoordbin, 'bo', label='Bin Search')
ymax = max(lst_ycoordseq)
plt.axis([0, 7, -0.1, ymax + 0.1])
plt.xlabel('Size of array (powers of 10)')
plt.ylabel('Search time (sec)')
plt.title('Sequential vs. Binary Search Performance')
plt.grid(True)
plt.legend(loc='upper left', numpoints=1)
plt.show()