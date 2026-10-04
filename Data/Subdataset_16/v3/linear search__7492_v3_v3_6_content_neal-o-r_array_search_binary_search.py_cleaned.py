import numpy as np
import timeit
import matplotlib.pyplot as plt
plt.style.use('ggplot')
def fonk1(b11):
    a1 = 0
    b1 = -np.inf
    for current_element in b11:
        if current_element < b1:
            return a1
        a1 += 1
        b1 = current_element
    return a1
def fonk2(b11, b2 = 0):
    if len(b11) == 0:
        return b2
    b3 = len(b11)
    b4 = b11[b3]
    if b4 = = b11[0]:
        return b2 + 1
    if b4 < b11[0]:
        return fonk2(b11[:b3], b2)
    else:
        b2 += b3
        return fonk2(b11[b3:], b2)
def fonk3(func, *args, **kwargs):
    def fonk4():
        return func(*args, **kwargs)
    return wrapped
def fonk5(func, b11, b5 = 10):
    a2 = 0
    for _ in range(b5):
        b6 = fonk3(func, b11)
        a2 += timeit.timeit(b6, b7 = 1)
    return a2 / b5
def fonk6():
    b8 = []
    b9 = []
    b10 = [10, 50, 100, 200, 500, 1000, 5000, 10000]
    for n in b10:
        b11 = np.roll(np.arange(n), np.random.randint(n))
        b12 = fonk5(binary_search, b11)
        b13 = fonk5(linear_search, b11)
        b8.append(b12)
        b9.append(b13)
    plt.plot(b10, np.array(b9) / max(b9), '-o', b14 = 'Linear Search')
    plt.plot(b10, np.array(b8) / max(b9), '-o', b14 = 'Binary Search')
    plt.plot(b10, np.array(b10) / max(b10), '--k', b14 = 'Linear')
    plt.plot(b10, np.log2(np.array(b10)) / max(b10), '--k', b14 = 'Logarithmic')
    plt.legend()
    plt.xlabel('Array Size')
    plt.ylabel('Normalized Time')
    plt.title('Performance of Linear vs Binary Search')
    plt.show()
if b15 = = '__main__':
    fonk6()