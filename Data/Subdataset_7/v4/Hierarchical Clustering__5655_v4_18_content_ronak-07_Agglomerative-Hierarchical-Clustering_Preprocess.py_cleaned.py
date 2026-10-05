import distance
import time
import numpy as np
def fonk1(seq):
    b1 = np.zeros(shape=(len(seq), len(seq)))
    for i in range(len(seq)):
        for j in range(i):
            b2 = distance.levenshtein(seq[i], seq[j])
            b1[i][j] = b2
            b1[j][i] = b2
    return b1
def fonk2(b7):
    b3 = []
    b4 = ""
    for line in b7:
        if line.startswith('>'):
            if b4:
                b3.append(b4)
            b4 = ""
        else:
            b4 += line.strip()
    if b4:
        b3.append(b4)
    return b3
if b5 = = "__main__":
    with open("data_amino2.txt", "r") as file:
        b6 = file.read()
    b7 = b6.splitlines()
    b8 = time.time()
    b3 = fonk2(b7)
    b9 = time.time() - b8
    print("Preprocessing done in:", b9, "seconds")
    b10 = time.time()
    b11 = fonk1(b3)
    b12 = time.time() - b10
    print("Distance Matrix Calculation done in:", b12, "seconds")
    np.save('b11.npy', b11)