def find_root(vertex):
    if root_ids[vertex] == vertex:
        return vertex
    else:
        while root_ids[vertex] != vertex:
            root_ids[vertex] = root_ids[root_ids[vertex]]
            vertex = root_ids[vertex]
        return vertex
def union(u, v):
    u_root = find_root(u)
    v_root = find_root(v)
    root_ids[v_root] = root_ids[u_root]
def kruskal(graph_edges):
    global root_ids
    min_weight = 0
    graph_edges = sorted(graph_edges, key=lambda x: x[2])
    for edge in graph_edges:
        u, v, weight = edge
        if find_root(u) != find_root(v):
            min_weight += weight
            union(u, v)
    return min_weight
V, E = map(int, input().split())
graph_edges = []
for i in range(E):
    graph_edges.append(list(map(int, input().split())))
root_ids = list(range(V + 1))
print(kruskal(graph_edges)))