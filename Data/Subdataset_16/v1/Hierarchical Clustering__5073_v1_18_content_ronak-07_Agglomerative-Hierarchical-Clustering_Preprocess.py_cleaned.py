import numpy as np
import distance
import time
def fonk1(b4, a1):
    b1 = np.zeros((a1 + 1, a1 + 1))
    b2 = []
    for a2 in range(a1 + 1):
        for j in range(a2):
            if a2 != j:
                b3 = distance.levenshtein(b4[a2], b4[j])
                b1[a2][j] = b1[j][a2] = b3
                b2.append(b3)
                print(f"Calculating distance for pair ({a2}, {j})")
    b2.sort()
    return b1
def fonk2(b8):
    b4 = {}
    a1 = -1
    b5 = len(b8)
    a2 = 0
    while a2 < b5:
        b6 = b8[a2]
        if b6.startswith('>'):
            b7 = ""
            a2 += 1
            while a2 < b5 and not b8[a2].startswith('>'):
                b7 += b8[a2]
                a2 += 1
            a1 += 1
            b4[a1] = b7
    return b4, a1
def fonk3():
    with open("data_amino2.txt", "b7") as f:
        b8 = f.read().splitlines()
    b9 = time.time()
    b4, a1 = fonk2(b8)
    print(f"Preprocessing done in {time.time() - b9:.2f} seconds")
    b9 = time.time()
    b10 = fonk1(b4, a1)
    print(f"Distance Matrix Calculation done in {time.time() - b9:.2f} seconds")
    np.save('b10.npy', b10)
    print("Distance matrix saved to 'b10.npy'")
if b11 = = "__main__":
    fonk3()