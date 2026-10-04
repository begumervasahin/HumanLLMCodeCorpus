import matplotlib.pyplot as plt
import numpy as np
def fonk1(signal_chunks, showtemplate):
    b1 = len(signal_chunks)
    b2 = np.mean(signal_chunks, axis=0)
    b3 = np.mean(np.std(signal_chunks[0:int(len(signal_chunks) / 4)], axis=0), axis=0)
    b4 = b2.copy()
    b4[0:(len(b4)
    b5 = abs(b4) + (5 * b3)
    b6 = (np.mean(b2, axis=0) * np.ones(len(b2)) - (7 * b3))
    b7 = []
    for k in range(len(b5)):
        b7.extend([b5[k]] * 2)
    b8 = int(len(b7) / (4 / 1.5)) + int(4 * 1.5)
    b5 = b7[b8:b8 + len(b5)]
    if showtemplate:
        plt.plot(b2)
        plt.plot(b5, 'r--')
        plt.plot(b6, 'r--')
        plt.show()
    b9 = []
    for i in range(b1):
        b10 = signal_chunks[i]
        b11 = (b10 > b6)
        b12 = (b10 < b5)
        b13 = np.logical_and(b11, b12)
        b9.append(np.all(b13))
    b9 = np.array(b9)
    b14 = np.where(b9)[0]
    print(f'{len(signal_chunks)} signals have been reduced to {len(b14)}.\n')
    return b14
