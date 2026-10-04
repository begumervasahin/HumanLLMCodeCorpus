def find_root(vertex):
    while root_ids[vertex] != vertex:
        root_ids[vertex] = root_ids[root_ids[vertex]]
        vertex = root_ids[vertex]
    return vertex
def union(u, v):
    root_u = find_root(u)
    root_v = find_root(v)
    if root_u != root_v:
        root_ids[root_v] = root_ids[root_u]
def kruskal(graph_edges):
    global root_ids
    total_weight = 0
    for edge in graph_edges:
        u, v, weight = edge
        if find_root(u) != find_root(v):
            total_weight += weight
            union(u, v)
    return total_weight
num_vertices, num_edges = map(int, input().split())
graph_edges = []
for _ in range(num_edges):
    u, v, weight = map(int, input().split())
    graph_edges.append([u, v, weight])
graph_edges = sorted(graph_edges, key=lambda x: x[2])
root_ids = list(range(num_vertices + 1))
print(kruskal(graph_edges))