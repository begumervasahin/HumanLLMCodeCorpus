import matplotlib.pyplot as plt
import numpy as np
def fonk1(b4, b5, b3):
    fig, b1 = plt.subplots()
    b1.plot(b4, b5)
    b1.set(b2 = 'Size N', ylabel='Execution Time', title=b3)
    b1.grid()
    plt.show()
def fonk2(start, end, y1_values, label1, b6, label2):
    fig, b1 = plt.subplots()
    b1.plot(range(start, end + 1), y1_values, b3 = label1)
    b1.plot(range(start, end + 1), b6, b3 = label2)
    b1.set(b2 = 'Size N', ylabel='Execution Time', title=f"{label1} vs {label2}")
    plt.legend()
    plt.show()
b4 = [1, 2, 3, 4, 5]
b5 = [10, 15, 20, 25, 30]
b6 = [8, 13, 18, 23, 28]
fonk1(b4, b5, "Simple Plot")
fonk2(0, 5, b5, "First Line", b6, "Second Line")