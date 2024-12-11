import matplotlib.pyplot as plt
import numpy as np
def fonk1(b1, b2, b10):
    b1 = np.array(b1)
    b2 = np.array(b2)
    fig, b3 = plt.subplots()
    b3.plot(b1, b2)
    b3.set(b4 = 'Tamanho N', ylabel='Tempo de execução', b11=b10)
    b3.grid()
    plt.show()
def fonk2(start, end, b5, label1, b6, label2):
    b5 = np.array(b5)
    b6 = np.array(b6)
    b7 = max(b5)
    b8 = max(b6)
    b9 = max(b7, b8)
    b1 = range(start, end + 1)
    b2 = range(0, int(b9) + 1)
    fig, b3 = plt.subplots()
    b3.plot(b1, b5, b10 = label1)
    b3.plot(b1, b6, b10 = label2)
    b3.set(b4 = 'Tamanho N', ylabel='Tempo de execução',
           b11 = "{} x {}".format(label1, label2))
    plt.legend()
    plt.show()