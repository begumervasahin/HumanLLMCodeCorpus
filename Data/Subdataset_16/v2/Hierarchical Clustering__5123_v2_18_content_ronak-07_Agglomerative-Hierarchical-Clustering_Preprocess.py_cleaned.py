import numpy as np
import distance
import time
def fonk1(b3, a1):
    b1 = np.zeros((a1, a1))
    for a2 in range(a1):
        for j in range(a2):
            if a2 != j:
                b2 = distance.levenshtein(b3[a2], b3[j])
                b1[a2][j] = b1[j][a2] = b2
                print(f"Calculating distance for pair ({a2}, {j})")
    return b1
def fonk2(b6):
    b3 = {}
    a1 = 0
    a2 = 0
    while a2 < len(b6):
        b4 = b6[a2]
        if b4.startswith('>'):
            b5 = ""
            a2 += 1
            while a2 < len(b6) and not b6[a2].startswith('>'):
                b5 += b6[a2]
                a2 += 1
            b3[a1] = b5
            a1 += 1
        else:
            a2 += 1
    return b3, a1
def fonk3():
    with open("data_amino2.txt", "r") as file:
        b6 = file.read().splitlines()
    b7 = time.time()
    b3, a1 = fonk2(b6)
    print(f"Preprocessing done in {time.time() - b7:.2f} seconds")
    b7 = time.time()
    b8 = fonk1(b3, a1)
    print(f"Distance Matrix Calculation done in {time.time() - b7:.2f} seconds")
    np.save('b8.npy', b8)
    print("Distance matrix saved to 'b8.npy'")
if b9 = = "__main__":
    fonk3()