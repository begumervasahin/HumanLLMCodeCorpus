import numpy as np
import timeit
import matplotlib.pyplot as plt
plt.style.use('ggplot')
def fonk1(b10):
    a1 = 0
    b1 = -np.inf
    for current_element in b10:
        if current_element < b1:
            return a1
        a1 += 1
        b1 = current_element
    return a1
def fonk2(b10, b2 = 0):
    if len(b10) == 0:
        return b2
    b3 = len(b10)
    b4 = b10[b3]
    if b4 = = b10[0]:
        return b2 + 1
    if b4 < b10[0]:
        return fonk2(b10[:b3], b2)
    else:
        return fonk2(b10[b3:], b2 + b3)
def fonk3(func, b10, b5 = 10):
    b6 = timeit.timeit(lambda: func(b10), number=b5)
    return b6 / b5
def fonk4():
    b7 = [10, 50, 100, 200, 500, 1000, 5000, 10000]
    b8 = []
    b9 = []
    for size in b7:
        b10 = np.roll(np.arange(size), np.random.randint(size))
        b11 = fonk3(linear_search, b10)
        b12 = fonk3(binary_search, b10)
        b8.append(b11)
        b9.append(b12)
    b13 = max(b8)
    b14 = np.array(b8) / b13
    b15 = np.array(b9) / b13
    plt.plot(b7, b14, '-o', b16 = 'Linear Search')
    plt.plot(b7, b15, '-o', b16 = 'Binary Search')
    plt.plot(b7, np.array(b7) / max(b7), '--k', b16 = 'Linear')
    plt.plot(b7, np.log2(np.array(b7)) / max(b7), '--k', b16 = 'Logarithmic')
    plt.xlabel('Array Size')
    plt.ylabel('Normalized Time')
    plt.title('Search Algorithm Performance')
    plt.legend()
    plt.show()
if b17 = = '__main__':
    fonk4()