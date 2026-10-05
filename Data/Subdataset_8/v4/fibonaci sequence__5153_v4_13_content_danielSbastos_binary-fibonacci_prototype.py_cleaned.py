import numpy as np
import matplotlib.pyplot as plt
def fib_iterative(n):
    a, b = 0, 1
    while n > 0:
        a, b = b, a + b
        n -= 1
    return a
def format_bin(number):
    return format(number, '080b')
n = 100
fib_list = [fib_iterative(i) for i in range(n + 1)]
fib_list_bin = [format_bin(i) for i in fib_list]
fib_list_bin_splited = []
for bin_number in fib_list_bin:
    bin_list = [int(i) for i in bin_number]
    fib_list_bin_splited.append(bin_list)
splited_binary_table = np.array(fib_list_bin_splited)
plt.imshow(splited_binary_table, interpolation='nearest')
plt.show()
hist_one = [sum(x) for x in splited_binary_table]
hist_zero = [101 - sum(x) for x in splited_binary_table]
indices = list(range(len(hist_one)))
p1 = plt.bar(indices, hist_one, 0.6, color='r')
p2 = plt.bar(indices, hist_zero, 0.6, color='y', bottom=hist_one)
plt.show()