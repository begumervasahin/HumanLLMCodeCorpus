import matplotlib.pyplot as plt
import numpy as np
def fonk1(b1, b2, b8):
    b1 = np.array(b1)
    b2 = np.array(b2)
    fig, b3 = plt.subplots()
    b3.plot(b1, b2)
    b3.set(b4 = 'Tamanho N', ylabel='Tempo de execução', title=b8)
    b3.grid()
    plt.show()
def fonk2(start, end, b5, label1, b6, label2):
    b5 = np.array(b5)
    b6 = np.array(b6)
    b7 = max(max(b5), max(b6))
    b1 = np.arange(start, end + 1)
    b2 = np.arange(0, int(b7) + 1)
    fig, b3 = plt.subplots()
    b3.plot(b1, b5, b8 = label1)
    b3.plot(b1, b6, b8 = label2)
    b3.set(b4 = 'Tamanho N', ylabel='Tempo de execução', title=f"{label1} x {label2}")
    plt.legend()
    plt.show()