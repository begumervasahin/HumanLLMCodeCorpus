import random
def constructRandomGraph(n):
    vSet = [[] for _ in range(n)]
    for i in range(2, n):
        x = random.randint(1, i-1)
        for _ in range(x):
            nodeConnect = random.randint(0, n-1)
            weight = random.randint(10, 100)
            vSet[i].append((nodeConnect, weight))
            vSet[nodeConnect].append((i, weight))
    matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for nodeConnect, matrixWeight in vSet[i]:
            matrix[i][nodeConnect] = matrixWeight
            matrix[nodeConnect][i] = matrixWeight
    return matrix
def BFS(G):
    v = random.randint(0, len(G)-1)
    total = 0
    Q = [v]
    visited = [0] * len(G)
    visited[v] = 1
    while Q:
        x = Q.pop(0)
        for y in range(len(G)):
            if G[x][y] > 0 and not visited[y]:
                visited[y] = 1
                Q.append(y)
                total += G[x][y]
    return total
def Prim(G):
    total = 0
    startVertex = random.randint(0, len(G)-1)
    n = len(G)
    A = [["empty"] * n for _ in range(3)]
    A[0][startVertex] = "N"
    for i in range(n):
        if i != startVertex:
            A[0][i] = "Y"
            A[2][i] = 1000
    for i in range(n):
        if G[startVertex][i] > 0:
            A[1][i] = startVertex
            A[2][i] = G[startVertex][i]
    T = [startVertex]
    chosen_edges = []
    while len(T) < n:
        min_val = 1000
        for i in range(n):
            if A[0][i] == "Y" and A[2][i] < min_val:
                min_val = A[2][i]
                x = i
        T.append(x)
        chosen_edges.append((x, A[1][x]))
        total += A[2][x]
        A[0][x] = "N"
        for y in range(n):
            if G[x][y] > 0 and A[0][y] == "Y" and G[x][y] < A[2][y]:
                A[1][y] = x
                A[2][y] = G[x][y]
    return total
def experiment():
    n = [20, 30, 40, 50, 60]
    k = 1000
    for num_nodes in n:
        total_diff = 0
        for _ in range(k):
            graph = constructRandomGraph(num_nodes)
            B = BFS(graph)
            P = Prim(graph)
            Diff = ((B / P) - 1) * 100
            total_diff += Diff
        avg_diff = total_diff / k
        print(f"Average of Diff for n = {num_nodes}: {avg_diff:.2f}")
if __name__ == "__main__":
    experiment()