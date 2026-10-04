import numpy as np
import timeit
import matplotlib.pyplot as plt
plt.style.use('ggplot')
def fonk1(b12):
    a1 = 0
    b1 = -np.inf
    for current_element in b12:
        if current_element < b1:
            return a1
        a1 += 1
        b1 = current_element
def fonk2(b12, b2 = 0):
    if len(b12) == 0:
        return b2
    b3 = len(b12)
    b4 = b12[b3]
    if b4 = = b12[0]:
        return b2 + 1
    if b4 < b12[0]:
        return fonk2(b12[:b3], b2)
    else:
        b2 += b3
        return fonk2(b12[b3:], b2)
def fonk3(func, *args, **kwargs):
    def fonk4():
        return func(*args, **kwargs)
    return wrapped
def fonk5(func, b12, b5 = 10):
    a2 = 0
    for _ in range(b5):
        b6 = fonk3(func, b12)
        a2 += timeit.timeit(b6, b7 = b5)
    return a2 / b5
if b8 = = '__main__':
    b9 = []
    b10 = []
    b11 = [10, 50, 100, 200, 500, 1000, 5000, 10000]
    for size in b11:
        b12 = np.roll(np.arange(size), np.random.randint(size))
        b13 = fonk5(binary_search, b12)
        b14 = fonk5(linear_search, b12)
        b10.append(b13)
        b9.append(b14)
    plt.plot(b11, np.array(b9) / max(b9), '-o', b15 = 'Linear Search')
    plt.plot(b11, np.array(b10) / max(b9), '-o', b15 = 'Binary Search')
    plt.plot(b11, np.array(b11) / max(b11), '--k', b15 = 'Linear')
    plt.plot(b11, np.log2(np.array(b11)) / max(b11), '--k', b15 = 'Logarithmic')
    plt.legend()
    plt.xlabel('Array Size')
    plt.ylabel('Normalized Time')
    plt.title('Search Algorithm Performance')
    plt.show()