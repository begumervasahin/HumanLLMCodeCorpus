import random
def construct_random_graph(n):
    adjacency_list = [[] for _ in range(n)]
    for i in range(2, n):
        connections = random.randint(1, i - 1)
        for _ in range(connections):
            node_connect = random.randint(0, n - 1)
            weight = random.randint(10, 100)
            adjacency_list[i].append((node_connect, weight))
            adjacency_list[node_connect].append((i, weight))
    adjacency_matrix = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for node_connect, weight in adjacency_list[i]:
            adjacency_matrix[i][node_connect] = weight
    return adjacency_matrix
def bfs(graph):
    start_vertex = random.randint(0, len(graph) - 1)
    total_weight = 0
    queue = []
    visited = [False] * len(graph)
    visited[start_vertex] = True
    queue.append(start_vertex)
    while queue:
        current_vertex = queue.pop(0)
        for neighbor in range(len(graph)):
            if graph[current_vertex][neighbor] > 0 and not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
                total_weight += graph[current_vertex][neighbor]
    return total_weight
def prim(graph):
    total_weight = 0
    start_vertex = random.randint(0, len(graph) - 1)
    num_vertices = len(graph)
    in_mst = ["N"] + ["Y"] * (num_vertices - 1)
    parent = ["empty"] * num_vertices
    key = [1000] * num_vertices
    in_mst[start_vertex] = "N"
    key[start_vertex] = 0
    for i in range(num_vertices):
        if graph[start_vertex][i] > 0:
            parent[i] = start_vertex
            key[i] = graph[start_vertex][i]
    mst_set = [start_vertex]
    while len(mst_set) < num_vertices:
        min_weight = 1000
        for i in range(num_vertices):
            if in_mst[i] == "Y" and key[i] < min_weight:
                min_weight = key[i]
                u = i
        mst_set.append(u)
        total_weight += key[u]
        in_mst[u] = "N"
        for v in range(num_vertices):
            if graph[u][v] > 0 and in_mst[v] == "Y" and graph[u][v] < key[v]:
                parent[v] = u
                key[v] = graph[u][v]
    return total_weight
def experiment():
    n_values = [20, 30, 40, 50, 60]
    num_trials = 1000
    for n in n_values:
        total_diff = 0
        for _ in range(num_trials):
            graph = construct_random_graph(n)
            bfs_total = bfs(graph)
            prim_total = prim(graph)
            diff = ((bfs_total / prim_total) - 1) * 100
            total_diff += diff
        avg_diff = total_diff / num_trials
        print(f"Average of Diff for n = {n}: {avg_diff}")
experiment()