import numpy as np
import matplotlib.pyplot as plt
def fonk1(a1):
    a, b1 = 0, 1
    for _ in range(a1):
        a, b1 = b1, a + b1
    return a
def fonk2(number):
    return format(number, '080b')
a1 = 100
b2 = [fonk1(i) for i in range(a1 + 1)]
b3 = [fonk2(num) for num in b2]
b4 = [[int(bit) for bit in binary] for binary in b3]
b5 = np.array(b4)
plt.imshow(b5, b6 = 'nearest')
plt.show()
b7 = [np.sum(column) for column in b5.T]
b8 = [len(b5) - ones for ones in b7]
b9 = list(range(len(b7)))
plt.bar(b9, b7, 0.6, b10 = 'r')
plt.bar(b9, b8, 0.6, b10 = 'y', bottom=b7)
plt.show()