import matplotlib.pyplot as plt
import numpy as np
def fonk1(signal_chunks, b12, b13):
    b1 = b12.copy()
    b1[:len(b1)
    b2 = np.abs(b1) + (5 * b13)
    b3 = b12.mean() * np.ones(len(b12)) - (7 * b13)
    b4 = np.repeat(b2, 2)
    b5 = int(len(b4) / (4 / 1.5)) + int(4 * 1.5)
    b6 = b4[b5:b5 + len(b2)]
    return b6, b3
def fonk2(b12, b2, b3):
    plt.plot(b12, b7 = 'Signal Average')
    plt.plot(b2, 'r--', b7 = 'Upper Limit')
    plt.plot(b3, 'r--', b7 = 'Lower Limit')
    plt.legend()
    plt.show()
def fonk3(signal_chunks, b2, b3):
    b8 = []
    for signal in signal_chunks:
        b9 = np.logical_and(signal > b3, signal < b2)
        b8.append(np.all(b9))
    b10 = np.where(b8)[0]
    return b10
def fonk4(signal_chunks, showtemplate):
    b11 = len(signal_chunks)
    b12 = np.mean(signal_chunks, axis=0)
    b13 = np.mean(np.std(signal_chunks[:b11
    b2, b3 = fonk1(signal_chunks, b12, b13)
    if showtemplate:
        fonk2(b12, b2, b3)
    b10 = fonk3(signal_chunks, b2, b3)
    print(f'{b11} signals have been reduced to {len(b10)}.\n')
    return b10
