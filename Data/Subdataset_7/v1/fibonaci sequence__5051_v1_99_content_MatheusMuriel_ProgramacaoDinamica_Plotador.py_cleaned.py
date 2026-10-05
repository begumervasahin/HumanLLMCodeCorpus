import matplotlib.pyplot as plt
import numpy as np
def fonk1(b9, b10, b11):
    b1 = np.array(b9)
    b2 = np.array(b10)
    fig, b3 = plt.subplots()
    b3.plot(b1, b2)
    b3.set(b4 = 'Size N', ylabel='Execution Time',
           b5 = b11)
    b3.grid()
    plt.show()
def fonk2(start, end, y1, label1, y2, label2):
    b6 = np.array(y1)
    b7 = np.array(y2)
    b8 = max(max(y1), max(y2))
    b9 = range(start, end+1)
    b10 = range(0, int(b8) + 1)
    fig, b3 = plt.subplots()
    b3.plot(b9, b6, b11 = label1)
    b3.plot(b9, b7, b11 = label2)
    b3.set(b4 = 'Size N', ylabel='Execution Time',
           b5 = "{} vs {}".format(label1, label2))
    plt.legend()
    plt.show()
b12 = [1, 2, 3, 4, 5]
b13 = [10, 15, 20, 25, 30]
b14 = [8, 13, 18, 23, 28]
fonk1(b12, b13, "Simple Plot")
fonk2(0, 5, b13, "First Line", b14, "Second Line")