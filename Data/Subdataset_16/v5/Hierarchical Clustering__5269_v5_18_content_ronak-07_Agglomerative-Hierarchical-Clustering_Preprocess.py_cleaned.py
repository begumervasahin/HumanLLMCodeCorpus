import numpy as np
import distance
import time
def fonk1(b4):
    b1 = len(b4)
    b2 = np.zeros((b1, b1))
    for i in range(b1):
        for j in range(i):
            if i != j:
                b3 = distance.levenshtein(b4[i], b4[j])
                b2[i][j] = b2[j][i] = b3
                print(f"Calculating distance for pair ({i}, {j})")
    return b2
def fonk2(b6):
    b4 = []
    b5 = ""
    for line in b6:
        if line.startswith('>'):
            if b5:
                b4.append(b5)
                b5 = ""
        else:
            b5 += line.strip()
    if b5:
        b4.append(b5)
    return b4
def fonk3():
    with open("data_amino2.txt", "r") as file:
        b6 = file.read().splitlines()
    b7 = time.time()
    b4 = fonk2(b6)
    print(f"Preprocessing done in {time.time() - b7:.2f} seconds")
    b7 = time.time()
    b2 = fonk1(b4)
    print(f"Distance Matrix Calculation done in {time.time() - b7:.2f} seconds")
    np.save('distance_matrix.npy', b2)
    print("Distance matrix saved to 'distance_matrix.npy'")
if b8 = = "__main__":
    fonk3()