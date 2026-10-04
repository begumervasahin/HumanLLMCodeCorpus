import matplotlib.pyplot as plt
import numpy as np
def fonk1(b8, y, title):
    b1 = np.array(b8)
    b2 = np.array(y)
    fig, b3 = plt.subplots()
    b3.plot(b1, b2, b4 = 'o', linestyle='-')
    b3.set_xlabel('Tamanho N')
    b3.set_ylabel('Tempo de execução')
    b3.set_title(title)
    b3.grid(True)
    plt.show()
def fonk2(start, end, y1, label1, y2, label2):
    b1 = range(start, end + 1)
    b5 = np.array(y1)
    b6 = np.array(y2)
    fig, b3 = plt.subplots()
    b3.plot(b1, b5, b4 = 'o', linestyle='-', label=label1)
    b3.plot(b1, b6, b4 = 's', linestyle='--', label=label2)
    b3.set_xlabel('Tamanho N')
    b3.set_ylabel('Tempo de execução')
    b3.set_title(f"{label1} vs {label2}")
    b3.legend()
    b3.grid(True)
    plt.show()
if b7 = = "__main__":
    b8 = [1, 2, 3, 4, 5]
    b9 = [2, 3, 5, 7, 11]
    fonk1(b8, b9, "Simple Plot")
    b10 = [1, 4, 9, 16, 25]
    b11 = [2, 6, 12, 20, 30]
    fonk2(1, 5, b10, "Quadratic", b11, "Linear")