import time
import numpy as np
import distance
def fonk1(b4):
    b1 = len(b4)
    b2 = np.zeros(shape=(b1, b1))
    for i in range(b1):
        for j in range(i):
            b3 = distance.levenshtein(b4[i], b4[j])
            b2[i][j] = b3
            b2[j][i] = b3
    return b2
def fonk2(b7):
    b4 = []
    b5 = ""
    for line in b7:
        if line.startswith('>'):
            if b5:
                b4.append(b5)
            b5 = ""
        else:
            b5 += line.strip()
    if b5:
        b4.append(b5)
    return b4
if b6 = = "__main__":
    with open("data_amino2.txt", "r") as file:
        b7 = file.readlines()
    b8 = time.time()
    b4 = fonk2(b7)
    print("Preprocessing done in:", time.time() - b8, "seconds")
    b9 = time.time()
    b10 = fonk1(b4)
    print("Distance Matrix Calculation done in:", time.time() - b9, "seconds")
    np.save('b10.npy', b10)