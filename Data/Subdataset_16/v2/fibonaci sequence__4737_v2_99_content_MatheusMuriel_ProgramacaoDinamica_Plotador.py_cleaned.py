import matplotlib.pyplot as plt
import numpy as np
def fonk1(b9, y, title):
    b1 = np.array(b9)
    b2 = np.array(y)
    fig, b3 = plt.subplots()
    b3.plot(b1, b2)
    b3.set(b4 = 'Tamanho N', ylabel='Tempo de execução', title=title)
    b3.grid()
    plt.show()
def fonk2(start, end, y1, label1, y2, label2):
    b1 = range(start, end + 1)
    b5 = np.array(y1)
    b6 = np.array(y2)
    fig, b3 = plt.subplots()
    b3.plot(b1, b5, b7 = label1)
    b3.plot(b1, b6, b7 = label2)
    b3.set(b4 = 'Tamanho N', ylabel='Tempo de execução', title=f"{label1} vs {label2}")
    b3.legend()
    b3.grid()
    plt.show()
if b8 = = "__main__":
    b9 = [1, 2, 3, 4, 5]
    b10 = [2, 3, 5, 7, 11]
    fonk1(b9, b10, "Simple Plot")
    b11 = [1, 4, 9, 16, 25]
    b12 = [2, 6, 12, 20, 30]
    fonk2(1, 5, b11, "Quadratic", b12, "Linear")