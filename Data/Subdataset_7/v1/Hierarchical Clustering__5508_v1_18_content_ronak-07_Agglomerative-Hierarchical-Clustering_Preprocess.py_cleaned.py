import time
import numpy as np
import distance
def fonk1(b2, b4):
    b1 = np.zeros(shape=(len(b2), len(b2)))
    for i in range(len(b2)):
        for j in range(i):
            if i != j:
                b1[i][j] = distance.levenshtein(b2[i], b2[j])
                b1[j][i] = b1[i][j]
    return b1
def fonk2(b4):
    b2 = []
    a1 = -1
    for line in b4:
        if line.startswith('>'):
            b2.append('')
            a1 += 1
        else:
            b2[a1] += line
    return b2
if b3 = = "__main__":
    with open("data_amino2.txt", "r") as file:
        b4 = file.readlines()
    b5 = time.time()
    b6 = fonk2(b4)
    print("Preprocessing done in:", time.time() - b5, "seconds")
    b7 = time.time()
    b8 = fonk1(b6, b4)
    print("Distance Matrix Calculation done in:", time.time() - b7, "seconds")
    np.save('b8.npy', b8)