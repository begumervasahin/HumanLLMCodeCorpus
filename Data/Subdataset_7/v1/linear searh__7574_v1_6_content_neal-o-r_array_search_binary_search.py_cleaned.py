import numpy as np
import timeit
import matplotlib.pyplot as plt
plt.style.use('ggplot')
def fonk1(b8):
    a1 = 0
    b1 = -np.inf
    for a in b8:
        if a < b1:
            return a1
        a1 += 1
        b1 = a
def fonk2(b8, b2 = 0):
    b3 = b8[len(b8)
    if b3 = = b8[0]:
        return b2 + 1
    if b3 < b8[0]:
        return fonk2(b8[:len(b8)
    else:
        b2 += len(b8)
        return fonk2(b8[len(b8)
def fonk3(func, *args, **kwargs):
    def fonk4():
        return func(*args, **kwargs)
    return wrapped
if b4 = = '__main__':
    b5 = []
    b6 = []
    b7 = [10, 50, 100, 200, 500, 1000, 5000, 10000]
    for n in b7:
        a2 = 0
        a3 = 0
        for b2 in range(100):
            b8 = np.roll(np.arange(n), np.random.randint(n))
            b9 = fonk3(linear_search, b8)
            b10 = fonk3(binary_search, b8)
            a4 = 10
            a2 += timeit.timeit(b10, b11 = a4)
            a3 += timeit.timeit(b9, b11 = a4)
        b5.append(a2 / 100)
        b6.append(a3 / 100)
    plt.plot(b7, np.array(b6) / max(b6), '-o', b12 = 'Linear Search')
    plt.plot(b7, np.array(b5) / max(b6), '-o', b12 = 'Binary Search')
    plt.plot(b7, np.array(b7) / max(b7), '--k', b12 = 'Linear')
    plt.plot(b7, np.log2(np.array(b7)) / max(b7), '--k', b12 = 'Log')
    plt.legend()
    plt.show()