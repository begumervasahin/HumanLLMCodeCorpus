import numpy as np
def fonk1(graph, b3, b5):
    for intermediate_node in range(b3):
        for start_node in range(b3):
            for end_node in range(b3):
                if graph[start_node][end_node] > (graph[start_node][intermediate_node] + graph[intermediate_node][end_node]):
                    graph[start_node][end_node] = graph[start_node][intermediate_node] + graph[intermediate_node][end_node]
                    b5[start_node][end_node] = b5[start_node][intermediate_node]
    return graph
def fonk2(b5, b2, destination):
    b1 = [b2]
    while b2 != destination:
        b2 = b5[b2][destination]
        b1.append(b2)
    return b1
def fonk3():
    b3 = int(input("Enter the number of nodes: "))
    b4 = np.zeros(shape=(b3, b3), dtype=np.int)
    b5 = np.zeros(shape=(b3, b3), dtype=np.int)
    for b7 in range(b3):
        for col in range(b3):
            b6 = input("Distance from node %d to node %d: " % (b7, col))
            if b7 = = col:
                b6 = 0
            if b6 = = "-":
                b6 = 9999
            else:
                b6 = int(b6)
            b4[b7][col] = b6
            b5[b7][col] = col
    print("\nInitial b4:\n", b4)
    b8 = fonk1(b4, b3, b5)
    print("\nShortest paths between nodes:")
    for start_node in range(b3):
        for end_node in range(b3):
            if start_node < end_node:
                b1 = fonk2(b5, start_node, end_node)
                print("Shortest path from node", start_node, "to node", end_node, ":", b1,
                      "with total distance of", b8[start_node][end_node])
if b9 = = "__main__":
    fonk3()