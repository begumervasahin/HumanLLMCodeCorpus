import matplotlib.pyplot as plt
import numpy as np
def fonk1(signal_chunks, showtemplate):
    b1 = len(signal_chunks)
    b2 = np.mean(signal_chunks, axis=0)
    b3 = np.mean(np.std(signal_chunks[:b1
    b4 = b2.copy()
    b4[:len(b4)
    b5 = abs(b4) + (5 * b3)
    b6 = b2 - (7 * b3)
    b7 = np.repeat(b5, 4)
    b8 = len(b7)
    b9 = b7[b8:b8 + len(b5)]
    if showtemplate:
        plt.plot(b2, b10 = 'Signal Average')
        plt.plot(b9, 'r--', b10 = 'Upper Limit')
        plt.plot(b6, 'r--', b10 = 'Lower Limit')
        plt.legend()
        plt.show()
    b11 = [
        np.all((chunk > b6) & (chunk < b9))
        for chunk in signal_chunks
    ]
    b12 = np.where(b11)[0]
    print(f'{b1} signals have been reduced to {len(b12)}.')
    return b12