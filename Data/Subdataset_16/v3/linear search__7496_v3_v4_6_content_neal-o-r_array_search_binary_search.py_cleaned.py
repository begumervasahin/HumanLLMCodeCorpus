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
def fonk5(b12, b4 = 100, num_iterations=10):
    b5 = []
    b6 = []
    for n in b12:
        a2 = 0
        a3 = 0
        for _ in range(b4):
            b7 = np.roll(np.arange(n), np.random.randint(n))
            b8 = fonk3(linear_search, b7)
            b9 = fonk3(binary_search, b7)
            a2 += timeit.timeit(b8, b10 = num_iterations)
            a3 += timeit.timeit(b9, b10 = num_iterations)
        b5.append(a2 / b4)
        b6.append(a3 / b4)
    return b5, b6
def fonk6(b12, b5, b6):
    plt.plot(b12, np.array(b5) / max(b5), '-o', b11 = 'Linear Search')
    plt.plot(b12, np.array(b6) / max(b5), '-o', b11 = 'Binary Search')
    plt.plot(b12, np.array(b12) / max(b12), '--k', b11 = 'Linear')
    plt.plot(b12, np.log2(np.array(b12)) / max(np.log2(b12)), '--r', b11 = 'Logarithmic')
    plt.xlabel('Array Size (n)')
    plt.ylabel('Normalized Time')
    plt.title('Performance Comparison of Linear and Binary Search on Rotated Arrays')
    plt.legend()
    plt.show()
def fonk7():
    b12 = [10, 50, 100, 200, 500, 1000, 5000, 10000]
    b5, b6 = fonk5(b12)
    fonk6(b12, b5, b6)
if b13 = = '__main__':
    fonk7()