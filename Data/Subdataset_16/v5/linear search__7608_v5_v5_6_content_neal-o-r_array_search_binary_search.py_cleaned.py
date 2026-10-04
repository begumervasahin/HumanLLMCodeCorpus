import numpy as np
import timeit
import matplotlib.pyplot as plt
plt.style.use('ggplot')
def fonk1(b8):
    a1 = 0
    b1 = float('-inf')
    for current_element in b8:
        if current_element < b1:
            return a1
        a1 += 1
        b1 = current_element
    return a1
def fonk2(b8, b2 = 0):
    if len(b8) == 1:
        return b2 + 1
    b3 = len(b8)
    b4 = b8[b3]
    if b4 = = b8[0]:
        return b2 + 1
    if b4 < b8[0]:
        return fonk2(b8[:b3], b2)
    else:
        return fonk2(b8[b3:], b2 + b3)
def fonk3(func, *args, **kwargs):
    def fonk4():
        return func(*args, **kwargs)
    return wrapped
def fonk5(b15, b5 = 10, num_trials=100):
    b6 = []
    b7 = []
    for n in b15:
        a2 = 0
        a3 = 0
        for _ in range(num_trials):
            b8 = np.roll(np.arange(n), np.random.randint(n))
            b9 = fonk3(linear_search, b8)
            b10 = fonk3(binary_search, b8)
            a2 += timeit.timeit(b10, b11 = b5)
            a3 += timeit.timeit(b9, b11 = b5)
        b6.append(a2 / num_trials)
        b7.append(a3 / num_trials)
    return b6, b7
def fonk6(b15, b16, binary_times):
    b12 = max(b16)
    b13 = max(b15)
    plt.plot(b15, np.array(b16) / b12, '-o', b14 = 'Linear Search')
    plt.plot(b15, np.array(binary_times) / b12, '-o', b14 = 'Binary Search')
    plt.plot(b15, np.array(b15) / b13, '--k', b14 = 'Linear')
    plt.plot(b15, np.log2(np.array(b15)) / np.log2(b13), '--k', b14 = 'Logarithmic')
    plt.xlabel('Array Size (n)')
    plt.ylabel('Normalized Time')
    plt.title('Comparison of Linear and Binary Search Times')
    plt.legend()
    plt.show()
def fonk7():
    b15 = [10, 50, 100, 200, 500, 1000, 5000, 10000]
    binary_times, b16 = fonk5(b15)
    fonk6(b15, b16, binary_times)
if b17 = = '__main__':
    fonk7()