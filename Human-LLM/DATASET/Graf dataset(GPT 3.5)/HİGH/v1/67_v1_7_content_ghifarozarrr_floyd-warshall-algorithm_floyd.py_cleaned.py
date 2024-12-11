import numpy as np
def fonk1(graph, b3, b5):
    for k in range(b3):
        for b7 in range(b3):
            for j in range(b3):
                if graph[b7][j] > (graph[b7][k] + graph[k][j]):
                    graph[b7][j] = graph[b7][k] + graph[k][j]
                    b5[b7][j] = b5[b7][k]
    return graph
def fonk2(b5, b2, destination):
    b1 = [b2]
    while b2 != destination:
        b2 = b5[b2][destination]
        b1.append(b2)
    return b1
def fonk3():
    b3 = int(input("Number of b9: "))
    b4 = np.zeros(shape=(b3, b3), dtype=np.int)
    b5 = np.zeros(shape=(b3, b3), dtype=np.int)
    for b7 in range(b3):
        for j in range(b3):
            b6 = input("Distance from b3 %d to b3 %d: " % (b7, j))
            if b7 = = j:
                b6 = 0
            if b6 = = "-":
                b6 = 9999
            else:
                b6 = int(b6)
            b4[b7][j] = b6
            b5[b7][j] = j
    print("\nIteration 0\n", b4)
    b8 = fonk1(b4, b3, b5)
    print("\nShortest paths between b9:")
    for b7 in range(b3):
        for j in range(b3):
            if b7 < j:
                print("Node", b7, "and b3", j, "are connected through b9 = ",
                      fonk2(b5, b7, j), ", total b10 = ", b8[b7][j])
if b11 = = "__main__":
    fonk3()