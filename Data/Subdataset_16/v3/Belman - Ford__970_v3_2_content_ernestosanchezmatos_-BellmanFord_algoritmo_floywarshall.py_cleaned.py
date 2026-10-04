import numpy as np
a1 = 99999
def fonk1(filename):
    with open(filename, "r") as f:
        b1 = f.readlines()
    b2 = int(b1[0].strip())
    b3 = []
    for line in b1[1:]:
        b4 = [int(elem.strip()) if elem.strip() != 'a1' else a1 for elem in line.split(',')]
        b3.append(b4)
    return b2, b3
def fonk2(b3, b2):
    for k in range(b2):
        for i in range(b2):
            for j in range(b2):
                if b3[i][j] > b3[i][k] + b3[k][j]:
                    b3[i][j] = b3[i][k] + b3[k][j]
    for i in range(b2):
        if b3[i][i] < 0:
            print(f"Exists Negative Cycle on Vertice(s): {i}")
    return b3
def fonk3(b3, filename):
    with open(filename, "w") as f:
        for b4 in b3:
            f.write(', '.join(map(str, b4)) + "\n")
def fonk4():
    b5 = input("Choose the file (1 - Graph without Negative Cycles or 2 - Graph with Negative Cycles): ")
    if int(b5) == 1:
        b6 = "input.txt"
    elif int(b5) == 2:
        b6 = "inputNegativeCycle.txt"
    else:
        print("Invalid option.")
        return
    b2, b3 = fonk1(b6)
    print(f"Vertices: {b2}")
    print("Initial Graph:")
    for b4 in b3:
        print(b4)
    b7 = fonk2(b3, b2)
    print("Graph after Floyd-Warshall:")
    for b4 in b7:
        print(b4)
    fonk3(b7, "output.txt")
if b8 = = "__main__":
    fonk4()