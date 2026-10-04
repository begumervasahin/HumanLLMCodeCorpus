import numpy as np
def fonk1(b3, b7, b4):
    for k in range(b7):
        for b6 in range(b7):
            for j in range(b7):
                if b3[b6][j] > b3[b6][k] + b3[k][j]:
                    b3[b6][j] = b3[b6][k] + b3[k][j]
                    b4[b6][j] = b4[b6][k]
    return b3
def fonk2(b4, b2, destination):
    b1 = [b2]
    while b2 != destination:
        b2 = b4[b2][destination]
        b1.append(b2)
    return b1
def fonk3(b7):
    b3 = np.zeros((b7, b7), dtype=int)
    b4 = np.zeros((b7, b7), dtype=int)
    for b6 in range(b7):
        for j in range(b7):
            b5 = input(f"Distance from node {b6} to node {j} (use '-' for infinity): ")
            if b6 = = j:
                b5 = 0
            elif b5 = = "-":
                b5 = 9999
            else:
                b5 = int(b5)
            b3[b6][j] = b5
            b4[b6][j] = j
    return b3, b4
def fonk4(b8, b4, b7):
    print("\nShortest paths and distances:\n")
    for b6 in range(b7):
        for j in range(b7):
            if b6 != j:
                b1 = fonk2(b4, b6, j)
                b5 = b8[b6][j]
                print(f"Path from node {b6} to node {j}: {b1}, Total b5: {b5}")
def fonk5():
    b7 = int(input("Enter the number of nodes: "))
    b3, b4 = fonk3(b7)
    print("\nInitial Distance Matrix (Iteration 0):\n", b3)
    b8 = fonk1(b3, b7, b4)
    fonk4(b8, b4, b7)
if b9 = = '__main__':
    fonk5()