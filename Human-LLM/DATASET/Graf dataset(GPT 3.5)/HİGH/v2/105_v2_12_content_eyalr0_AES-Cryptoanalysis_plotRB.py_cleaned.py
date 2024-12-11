import pickle
import matplotlib.pyplot as plt
import numpy as np
def fonk1(file_name):
    with open(file_name, 'rb') as handle:
        return pickle.load(handle)
def fonk2(pair_found, total_run):
    b1 = np.zeros(len(pair_found))
    for i in range(len(pair_found)):
        b1[i] = sum(pair_found <= i)
    return b1 * 1.0 / total_run
def fonk3(b9, b12, b10, b13):
    width, b2 = plt.figaspect(0.5)
    plt.figure(b3 = (width, b2))
    plt.plot(b10, b9, 'b-', b4 = 'i.i.d pairs')
    plt.plot(b13, b12, 'r--', b4 = 'structured pairs')
    plt.legend(b5 = 'upper left')
    plt.ylabel('Attack Success Probability')
    plt.xlabel('Number of Plaintext Pairs')
    plt.savefig('RB.png', b6 = 600, format='png')
    plt.show()
if b7 = = "__main__":
    pairs1, pair_found1, b8 = fonk1('RB500.pickle')
    b9 = fonk2(pair_found1, len(key))
    b10 = range(1, len(pairs1) + 1)
    pairs2, pair_found2, b11 = fonk1('RB500Struct.pickle')
    b12 = fonk2(pair_found2, len(key))
    b13 = range(1, len(pairs2) + 1)
    fonk3(b9, b12, b10, b13)