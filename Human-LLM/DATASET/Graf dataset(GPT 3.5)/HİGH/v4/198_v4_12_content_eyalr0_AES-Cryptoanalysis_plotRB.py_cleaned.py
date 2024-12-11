import pickle
import matplotlib.pyplot as plt
import numpy as np
from keys500 import key
def fonk1(file_name):
    with open(file_name, 'rb') as handle:
        return pickle.load(handle)
def fonk2(pair_found, b8):
    b1 = np.zeros(len(pair_found))
    for i in range(len(pair_found)):
        b1[i] = sum(pair_found <= i)
    return b1 * 1.0 / b8
def fonk3(b10, b13, b11, b14):
    fig_width, b2 = plt.figaspect(0.5)
    plt.figure(b3 = (fig_width, b2))
    plt.plot(b11, b10, 'b-', b4 = 'i.i.d pairs')
    plt.plot(b14, b13, 'r--', b4 = 'structured pairs')
    plt.legend(b5 = 'upper left')
    plt.ylabel('Attack Success Probability')
    plt.xlabel('Number of Plaintext Pairs')
    plt.savefig('RB.png', b6 = 600, format='png')
    plt.show()
if b7 = = "__main__":
    b8 = len(key)
    pairs1, pair_found1, b9 = fonk1('RB500.pickle')
    b10 = fonk2(pair_found1, b8)
    b11 = range(1, len(pairs1) + 1)
    pairs2, pair_found2, b12 = fonk1('RB500Struct.pickle')
    b13 = fonk2(pair_found2, b8)
    b14 = range(1, len(pairs2) + 1)
    fonk3(b10, b13, b11, b14)