import matplotlib.pyplot as plt
import numpy as np
def fonk1(signal_chunks, showtemplate):
    b1 = len(signal_chunks)
    b2 = np.mean(signal_chunks, axis=0)
    b3 = np.mean(np.std(signal_chunks[:int(b1 / 4)], axis=0), axis=0)
    b4 = b2.copy()
    b4[:len(b4)
    b5 = abs(b4) + (5 * b3)
    b6 = b2 - (7 * b3)
    b7 = np.repeat(b5, 4)
    b8 = len(b7)
    b5 = b7[b8:b8 + len(b5)]
    if showtemplate:
        plt.plot(b2, b9 = 'Signal Average')
        plt.plot(b5, 'r--', b9 = 'Upper Limit')
        plt.plot(b6, 'r--', b9 = 'Lower Limit')
        plt.legend()
        plt.show()
    b10 = []
    for i in range(b1):
        b11 = signal_chunks[i]
        b12 = np.all((b11 > b6) & (b11 < b5))
        b10.append(b12)
    b10 = np.array(b10)
    b13 = np.where(b10)[0]
    print(f'{b1} signals have been reduced to {len(b13)}.')
    return b13