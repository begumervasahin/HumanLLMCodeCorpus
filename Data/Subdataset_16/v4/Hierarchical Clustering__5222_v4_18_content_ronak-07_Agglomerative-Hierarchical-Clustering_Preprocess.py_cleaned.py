import numpy as np
import distance
import time
def fonk1(b3, b9):
    b1 = np.zeros((b9, b9))
    for a2 in range(b9):
        for j in range(a2):
            if a2 != j:
                b2 = distance.levenshtein(b3[a2], b3[j])
                b1[a2][j] = b1[j][a2] = b2
                print(f"Calculating distance for pair ({a2}, {j})")
    return b1
def fonk2(b7):
    b3 = {}
    a1 = -1
    b4 = len(b7)
    a2 = 0
    while a2 < b4:
        b5 = b7[a2]
        if b5.startswith('>'):
            a1 += 1
            b6 = ""
            a2 += 1
            while a2 < b4 and not b7[a2].startswith('>'):
                b6 += b7[a2]
                a2 += 1
            b3[a1] = b6
    return b3, a1 + 1
def fonk3():
    with open("data_amino2.txt", "r") as file:
        b7 = file.read().splitlines()
    b8 = time.time()
    b3, b9 = fonk2(b7)
    print(f"Preprocessing done in {time.time() - b8:.2f} seconds")
    b8 = time.time()
    b1 = fonk1(b3, b9)
    print(f"Distance Matrix Calculation done in {time.time() - b8:.2f} seconds")
    np.save('distance_matrix.npy', b1)
    print("Distance matrix saved to 'distance_matrix.npy'")
if b10 = = "__main__":
    fonk3()