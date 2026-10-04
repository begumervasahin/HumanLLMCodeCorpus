import random
def construct_random_graph(n):
    adjacency_list = [[] for _ in range(n)]
    for i in range(2, n):
        x = random.randint(1, i-1)
        for _ in range(x):
            node_connect = random.randint(0, n-1)
            weight = random.randint(10, 100)
            adjacency_list[i].append((node_connect, weight))
            adjacency_list[node_connect].append((i, weight))
    adjacency_matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for node_connect, weight in adjacency_list[i]:
            adjacency_matrix[i][node_connect] = weight
            adjacency_matrix[node_connect][i] = weight
    return adjacency_matrix
def bfs(graph):
    start_vertex = random.randint(0, len(graph)-1)
    total_weight = 0
    queue = [start_vertex]
    visited = [False] * len(graph)
    visited[start_vertex] = True
    while queue:
        current = queue.pop(0)
        for neighbor in range(len(graph)):
            if graph[current][neighbor] > 0 and not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
                total_weight += graph[current][neighbor]
    return total_weight
def prim(graph):
    total_weight = 0
    n = len(graph)
    start_vertex = random.randint(0, n-1)
    visited = [False] * n
    min_edge = [(float('inf'), -1)] * n
    min_edge[start_vertex] = (0, -1)
    for _ in range(n):
        current = min((w, v) for v, (w, _) in enumerate(min_edge) if not visited[v])[1]
        visited[current] = True
        total_weight += min_edge[current][0]
        for neighbor, weight in enumerate(graph[current]):
            if weight > 0 and not visited[neighbor] and weight < min_edge[neighbor][0]:
                min_edge[neighbor] = (weight, current)
    return total_weight
def experiment():
    node_counts = [20, 30, 40, 50, 60]
    repetitions = 1000
    for num_nodes in node_counts:
        total_diff = 0
        for _ in range(repetitions):
            graph = construct_random_graph(num_nodes)
            bfs_weight = bfs(graph)
            prim_weight = prim(graph)
            diff = ((bfs_weight / prim_weight) - 1) * 100
            total_diff += diff
        avg_diff = total_diff / repetitions
        print(f"Average difference for n = {num_nodes}: {avg_diff:.2f}%")
if __name__ == "__main__":
    experiment()