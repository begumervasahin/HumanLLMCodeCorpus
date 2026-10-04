import numpy as np
import math
np.set_printoptions(precision=2, suppress=True)
infinity = math.inf
def get_graph():
    V = int(input("Enter number of vertices: "))
    print("Enter the values of adjacency matrix row-wise:")
    graph = np.zeros((V, V))
    for i in range(V):
        for j in range(V):
            graph[i][j] = int(input())
    return V, graph
def floyd_warshall(graph, n):
    print("\n\n")
    print("D[0] :\n", graph)
    print("\n")
    for k in range(n):
        for i in range(n):
            for j in range(n):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
        print(f"D[{k+1}] :\n", graph)
        print("\n")
def main():
    V, graph = get_graph()
    floyd_warshall(graph, V)
if __name__ == '__main__':
    main()