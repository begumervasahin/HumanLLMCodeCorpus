import numpy as np
import timeit
import matplotlib.pyplot as plt
plt.style.use('ggplot')
def fonk1(b9):
    a1 = 0
    b1 = -np.inf
    for current_element in b9:
        if current_element < b1:
            return a1
        a1 += 1
        b1 = current_element
def fonk2(b9, b2 = 0):
    b3 = len(b9)
    b4 = b9[b3]
    if b4 = = b9[0]:
        return b2 + 1
    if b4 < b9[0]:
        return fonk2(b9[:b3], b2)
    else:
        b2 += b3
        return fonk2(b9[b3:], b2)
def fonk3(func, *args, **kwargs):
    def fonk4():
        return func(*args, **kwargs)
    return wrapped
if b5 = = '__main__':
    b6 = []
    b7 = []
    b8 = [10, 50, 100, 200, 500, 1000, 5000, 10000]
    for n in b8:
        a2 = 0
        a3 = 0
        for _ in range(100):
            b9 = np.roll(np.arange(n), np.random.randint(n))
            b10 = fonk3(linear_search, b9)
            b11 = fonk3(binary_search, b9)
            a4 = 10
            a2 += timeit.timeit(b11, b12 = a4)
            a3 += timeit.timeit(b10, b12 = a4)
        b13 = a2 / 100
        b14 = a3 / 100
        b6.append(b13)
        b7.append(b14)
    plt.plot(b8, np.array(b7) / max(b7), '-o', b15 = 'Linear Search')
    plt.plot(b8, np.array(b6) / max(b7), '-o', b15 = 'Binary Search')
    plt.plot(b8, np.array(b8) / max(b8), '--k', b15 = 'Linear')
    plt.plot(b8, np.log2(np.array(b8)) / max(b8), '--k', b15 = 'Logarithmic')
    plt.legend()
    plt.show()