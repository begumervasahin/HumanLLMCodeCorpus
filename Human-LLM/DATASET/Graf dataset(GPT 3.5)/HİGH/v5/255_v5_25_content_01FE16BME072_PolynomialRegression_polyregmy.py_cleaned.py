import numpy as np
import matplotlib.pyplot as plt
b1 = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])
b2 = np.array([4, 5, 6, 8, 11, 15, 20, 30, 50, 100])
plt.scatter(b1, b2, b3 = 50, b10='red')
b4 = {
    'b0': 0,
    'b1': -10,
    'b2': -50,
    'b3': -10,
    'b4': 50
}
b5 = len(b2)
a1 = 0.001
b6 = {
    'a': b1,
    'b': b1 ** 2,
    'c': b1 ** 3,
    'd': b1 ** 4
}
for _ in range(1000):
    b7 = sum(b4[key] * value for key, value in b6.items())
    b8 = {}
    for key in b4.keys():
        b8[key] = (-2/b5) * sum(b6[key] * (b2 - b7))
    for key in b4.keys():
        b4[key] -= b8[key] * a1
b9 = sum(b4[key] * value for key, value in b6.items())
plt.plot(b1, b9, b10 = 'blue')
plt.show()