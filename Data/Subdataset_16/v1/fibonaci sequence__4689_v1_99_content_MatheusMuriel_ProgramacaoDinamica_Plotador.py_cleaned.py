import matplotlib.pyplot as plt
import numpy as np
def fonk1(b8, y, b9):
    b1 = np.array(b8)
    b2 = np.array(y)
    fig, b3 = plt.subplots()
    b3.plot(b1, b2)
    b3.set(b4 = 'Tamanho N', ylabel='Tempo de execução', title=b9)
    b3.grid()
    plt.show()
def fonk2(start, end, y1, label1, y2, label2):
    b5 = np.array(y1)
    b6 = np.array(y2)
    b7 = max(max(y1), max(y2))
    b8 = range(start, end + 1)
    fig, b3 = plt.subplots()
    b3.plot(b8, b5, b9 = label1)
    b3.plot(b8, b6, b9 = label2)
    b3.set(b4 = 'Tamanho N', ylabel='Tempo de execução', title=f"{label1} b8 {label2}")
    plt.legend()
    plt.show()
if b10 = = "__main__":
    b8 = [1, 2, 3, 4, 5]
    b11 = [2, 3, 5, 7, 11]
    fonk1(b8, b11, "Simple Plot")
    b12 = [1, 4, 9, 16, 25]
    b13 = [2, 6, 12, 20, 30]
    fonk2(1, 5, b12, "Quadratic", b13, "Linear")