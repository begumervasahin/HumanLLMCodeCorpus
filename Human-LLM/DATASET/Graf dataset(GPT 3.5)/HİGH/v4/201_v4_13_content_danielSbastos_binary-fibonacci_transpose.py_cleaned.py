import numpy as np
import matplotlib.pyplot as plt
def fonk1(a1):
    a, b1 = 0, 1
    while a1 > 0:
        a, b1 = b1, a + b1
        a1 -= 1
    return a
def fonk2(number):
    return format(number, '080b')
a1 = 100
b2 = [fonk1(i) for i in range(a1 + 1)]
b3 = [fonk2(num) for num in b2]
b4 = [[int(bit) for bit in binary] for binary in b3]
b5 = np.array(b4)
b6 = np.transpose(b5)
plt.imshow(b6, b7 = 'nearest')
plt.show()