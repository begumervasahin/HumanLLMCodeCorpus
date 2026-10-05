import matplotlib.pyplot as plt
import numpy as np
def fonk1(b1, b2, b8):
    b1 = np.array(b1)
    b2 = np.array(b2)
    fig, b3 = plt.subplots()
    b3.plot(b1, b2)
    b3.set(b4 = 'Size N', ylabel='Execution Time', title=b8)
    b3.grid()
    plt.show()
def fonk2(start, end, b5, label1, b6, label2):
    b5 = np.array(b5)
    b6 = np.array(b6)
    b7 = max(max(b5), max(b6))
    b1 = range(start, end + 1)
    b2 = range(0, int(b7) + 1)
    fig, b3 = plt.subplots()
    b3.plot(b1, b5, b8 = label1)
    b3.plot(b1, b6, b8 = label2)
    b3.set(b4 = 'Size N', ylabel='Execution Time', title=f"{label1} vs {label2}")
    plt.legend()
    plt.show()
b1 = [1, 2, 3, 4, 5]
b2 = [10, 15, 20, 25, 30]
b6 = [8, 13, 18, 23, 28]
fonk1(b1, b2, "Simple Plot")
fonk2(0, 5, b2, "First Line", b6, "Second Line")