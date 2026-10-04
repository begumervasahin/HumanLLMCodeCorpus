import matplotlib.pyplot as plt
import numpy as np
def fonk1(signal_chunks, showtemplate):
    b1 = len(signal_chunks)
    b2 = np.mean(signal_chunks, b4=0)
    b3 = np.mean(np.std(signal_chunks[0:int(len(signal_chunks) / 4)],
                                 b4 = 0), b4=0)
    b5 = b2.copy()
    b5[0:(len(b5)/2)] = abs(b5[0:(len(b5)/2)])
    b6 = abs(b5) + (5 * b3)
    b7 = (np.mean(b2, b4=0) *
                   np.ones(len(b2)) - (7 * b3))
    b8 = b6
    b9 = []
    for k in xrange(0, len(b8)):
        b9.append(b6[k])
        b9.append(b8[k])
        b9.append(b6[k])
        b9.append(b8[k])
    b10 = int(len(b9) / (4 / 1.5)) + int(4 * 1.5)
    b6 = b9[b10:b10 + len(b8)]
    if(showtemplate):
        plt.plot(b2)
        plt.hold(True)
        plt.plot(b6, 'r--')
        plt.plot(b7, 'r--')
        plt.show()
    b11 = []
    for i in xrange(0, b1):
        b12 = signal_chunks[i]
        b13 = (b12 > b7)
        b14 = (b12 < b6)
        b15 = list(b13) and list(b14)
        b8 = True
        for k in b15:
            b8 = b8 and k
        b11.append(b8)
    b11 = np.array(b11)
    b16 = np.where(b11 is True)
    print ('%.0f signals have been reduced to %.0f.\n'
           % (len(signal_chunks), len(signal_chunks[b16])))
    return b16