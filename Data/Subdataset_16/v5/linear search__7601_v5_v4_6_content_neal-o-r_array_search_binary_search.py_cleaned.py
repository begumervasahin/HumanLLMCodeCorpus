import numpy as np
import timeit
import matplotlib.pyplot as plt
plt.style.use('ggplot')
def fonk1(b7):
    a1 = 0
    b1 = -np.inf
    for current_element in b7:
        if current_element < b1:
            return a1
        a1 += 1
        b1 = current_element
    return a1
def fonk2(b7, b2 = 0):
    b3 = b7[len(b7)
    if b3 = = b7[0]:
        return b2 + 1
    if b3 < b7[0]:
        return fonk2(b7[:len(b7)
    else:
        b2 += len(b7)
        return fonk2(b7[len(b7)
def fonk3(func, *args, **kwargs):
    def fonk4():
        return func(*args, **kwargs)
    return wrapped
def fonk5(b13, b4 = 100, num_timings=10):
    b5 = []
    b6 = []
    for n in b13:
        a2 = 0
        a3 = 0
        for _ in range(b4):
            b7 = np.roll(np.arange(n), np.random.randint(n))
            b8 = fonk3(linear_search, b7)
            b9 = fonk3(binary_search, b7)
            a2 += timeit.timeit(b9, b10 = num_timings)
            a3 += timeit.timeit(b8, b10 = num_timings)
        b5.append(a2 / b4)
        b6.append(a3 / b4)
    return b5, b6
def fonk6(b13, b6, b5):
    plt.plot(b13, np.array(b6) / max(b6), '-o', b11 = 'Linear Search')
    plt.plot(b13, np.array(b5) / max(b6), '-o', b11 = 'Binary Search')
    plt.plot(b13, np.array(b13) / max(b13), '--k', b11 = 'Linear')
    plt.plot(b13, np.log2(np.array(b13)) / max(np.log2(np.array(b13))), '--r', b11 = 'Logarithmic')
    plt.xlabel('Array Size (n)')
    plt.ylabel('Normalized Time')
    plt.legend()
    plt.title('Performance Comparison of Search Algorithms')
    plt.show()
if b12 = = '__main__':
    b13 = [10, 50, 100, 200, 500, 1000, 5000, 10000]
    b5, b6 = fonk5(b13)
    fonk6(b13, b6, b5)