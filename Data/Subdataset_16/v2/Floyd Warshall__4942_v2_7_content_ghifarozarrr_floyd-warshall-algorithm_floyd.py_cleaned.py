import numpy as np
def fonk1(b4, b3, b5):
    for k in range(b3):
        for b7 in range(b3):
            for j in range(b3):
                if b4[b7][j] > b4[b7][k] + b4[k][j]:
                    b4[b7][j] = b4[b7][k] + b4[k][j]
                    b5[b7][j] = b5[b7][k]
    return b4
def fonk2(b5, b2, destination):
    b1 = [b2]
    while b2 != destination:
        b2 = b5[b2][destination]
        b1.append(b2)
    return b1
def fonk3():
    b3 = int(input("Enter the number of nodes: "))
    b4 = np.zeros((b3, b3), dtype=int)
    b5 = np.zeros((b3, b3), dtype=int)
    for b7 in range(b3):
        for j in range(b3):
            b6 = input(f"Distance from node {b7} to node {j} (use '-' for infinity): ")
            if b7 = = j:
                b6 = 0
            elif b6 = = "-":
                b6 = 9999
            else:
                b6 = int(b6)
            b4[b7][j] = b6
            b5[b7][j] = j
    print("\nInitial Distance Matrix (Iteration 0):\n", b4)
    b8 = fonk1(b4, b3, b5)
    print("\nShortest paths and distances:\n")
    for b7 in range(b3):
        for j in range(b3):
            if b7 != j:
                b1 = fonk2(b5, b7, j)
                b6 = b8[b7][j]
                print(f"Path from node {b7} to node {j}: {b1}, Total b6: {b6}")
if b9 = = '__main__':
    fonk3()