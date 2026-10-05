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
b3 = [fonk2(i) for i in b2]
b4 = []
for bin_number in b3:
    b5 = [int(i) for i in bin_number]
    b4.append(b5)
b6 = np.array(b4)
plt.imshow(b6, b7 = 'nearest')
plt.show()
b8 = [sum(x) for x in b6]
b9 = [101 - sum(x) for x in b6]
b10 = list(range(len(b8)))
b11 = plt.bar(b10, b8, 0.6, color='r')
b12 = plt.bar(b10, b9, 0.6, color='y', bottom=b8)
plt.show()