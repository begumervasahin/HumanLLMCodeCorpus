import numpy as np
import timeit
import matplotlib.pyplot as plt
plt.style.use('ggplot')
def fonk1(b8):
    a1 = 0
    b1 = -np.inf
    for current_element in b8:
        if current_element < b1:
            return a1
        a1 += 1
        b1 = current_element
def fonk2(b8, b2 = 0):
    b3 = len(b8)
    b4 = b8[b3]
    if b4 = = b8[0]:
        return b2 + 1
    elif b4 < b8[0]:
        return fonk2(b8[:b3], b2)
    else:
        return fonk2(b8[b3:], b2 + b3)
def fonk3(func, *args, **kwargs):
    def fonk4():
        return func(*args, **kwargs)
    return wrapped
def fonk5(b21, b5 = 10, num_trials=100):
    b6 = []
    b7 = []
    for size in b21:
        a2 = 0
        a3 = 0
        for _ in range(num_trials):
            b8 = np.roll(np.arange(size), np.random.randint(size))
            b9 = fonk3(linear_search, b8)
            b10 = fonk3(binary_search, b8)
            a2 += timeit.timeit(b10, b11 = b5)
            a3 += timeit.timeit(b9, b11 = b5)
        b12 = a2 / num_trials
        b13 = a3 / num_trials
        b7.append(b12)
        b6.append(b13)
    return b6, b7
def fonk6(times, max_value):
    return np.array(times) / max_value
def fonk7(b21, b6, b7):
    b14 = max(b6)
    b15 = fonk6(b6, b14)
    b16 = fonk6(b7, b14)
    b17 = fonk6(b21, max(b21))
    b18 = fonk6(np.log2(b21), max(b21))
    plt.plot(b21, b15, '-o', b19 = 'Linear Search')
    plt.plot(b21, b16, '-o', b19 = 'Binary Search')
    plt.plot(b21, b17, '--k', b19 = 'Linear')
    plt.plot(b21, b18, '--k', b19 = 'Logarithmic')
    plt.legend()
    plt.xlabel('Array Size (n)')
    plt.ylabel('Normalized Time')
    plt.title('Linear Search vs Binary Search Time Complexity')
    plt.show()
if b20 = = '__main__':
    b21 = [10, 50, 100, 200, 500, 1000, 5000, 10000]
    b6, b7 = fonk5(b21)
    fonk7(b21, b6, b7)