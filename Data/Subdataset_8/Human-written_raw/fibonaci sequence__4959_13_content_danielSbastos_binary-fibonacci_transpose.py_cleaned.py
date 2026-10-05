import numpy as np
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
    bin_list = []
    for i in bin_number:
        bin_list.append(int(i))
    fib_list_bin_splited.append(bin_list)
splited_binary_table = np.array(fib_list_bin_splited)
splited_binary_table = np.transpose(splited_binary_table)
import matplotlib.pyplot as plt
plt.imshow(splited_binary_table, interpolation='nearest')
plt.show()