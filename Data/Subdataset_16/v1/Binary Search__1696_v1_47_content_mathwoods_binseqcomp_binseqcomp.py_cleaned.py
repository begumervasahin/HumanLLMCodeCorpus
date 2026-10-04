import random
import timeit
import matplotlib.pyplot as plt
def fonk1(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
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
    return b10
print("\nSEQUENTIAL SEARCH VS BINARY SEARCH")
i, b4 = 2, 1
b5 = []
a1 = 10
while i <= 6:
    b6 = 10**i
    b7 = tuple(range(0, b6))
    print(f"\nARRAY b8 = {b6} (10^{i})")
    while b4 <= 3:
        b1 = random.randint(0, b6-1)
        print(f"TRIAL {b4}")
        print(f"Random generated value: {b1}")
        print("Running SEQ SEARCH...", b9 = "")
        b10 = fonk3(seq_search, b7, b1)
        b11 = timeit.timeit(b10, number=a1)
        print("DONE!")
        print(f"Total time for {a1} searches: {b11:.6f} seconds.")
        print("Running BIN SEARCH...", b9 = "")
        b10 = fonk3(bin_search, b7, b1)
        b12 = timeit.timeit(b10, number=a1)
        print("DONE!")
        print(f"Total time for {a1} searches: {b12:.6f} seconds.")
        b5.append({
            'power': i,
            'b4': b4,
            'tup_size': b6,
            'rand': b1,
            'b11': b11,
            'b12': b12,
            'a1': a1
        })
        b4 += 1
    i += 1
    b4 = 1
print("\nTo b9 program, close the graph window.\b6")
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
plt.title('Sequential vs. Binary Search Performance')
plt.grid(True)
plt.legend(b19 = 'upper left', numpoints=1)
plt.show()