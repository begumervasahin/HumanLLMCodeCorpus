import numpy as np
def fonk1(graph, b3, b5):
    for intermediate_node in range(b3):
        for b2 in range(b3):
            for end_node in range(b3):
                if graph[b2][end_node] > (graph[b2][intermediate_node] + graph[intermediate_node][end_node]):
                    graph[b2][end_node] = graph[b2][intermediate_node] + graph[intermediate_node][end_node]
                    b5[b2][end_node] = b5[b2][intermediate_node]
    return graph
def fonk2(b5, b2, end_node):
    b1 = [b2]
    while b2 != end_node:
        b2 = b5[b2][end_node]
        b1.append(b2)
    return b1
def fonk3():
    b3 = int(input("Enter the number of nodes: "))
    b4 = np.zeros(shape=(b3, b3), dtype=np.int)
    b5 = np.zeros(shape=(b3, b3), dtype=np.int)
    for b7 in range(b3):
        for j in range(b3):
            b6 = input(f"Distance from node {b7} to node {j}: ")
            if b7 = = j:
                b6 = 0
            if b6 = = "-":
                b6 = 9999
            else:
                b6 = int(b6)
            b4[b7][j] = b6
            b5[b7][j] = j
    print("\nInitial b4:\n", b4)
    b8 = fonk1(b4, b3, b5)
    print("\nShortest paths between nodes:")
    for b7 in range(b3):
        for j in range(b3):
            if b7 < j:
                b1 = fonk2(b5, b7, j)
                print(f"Node {b7} and node {j} are connected through nodes {b1}, total b9 = {b8[b7][j]}")
if b10 = = "__main__":
    fonk3()