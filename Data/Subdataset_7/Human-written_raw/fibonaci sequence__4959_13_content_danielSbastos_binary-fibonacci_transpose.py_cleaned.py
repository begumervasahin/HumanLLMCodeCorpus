import numpy as np
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
    b5 = []
    for i in bin_number:
        b5.append(int(i))
    b4.append(b5)
b6 = np.array(b4)
b6 = np.transpose(b6)
import matplotlib.pyplot as plt
plt.imshow(b6, b7 = 'nearest')
plt.show()