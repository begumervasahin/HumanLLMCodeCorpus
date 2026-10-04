
parent = {}
def make_set(vertex):
    parent[vertex] = vertex
def find_set(vertex):
    if parent[vertex] != vertex:
        parent[vertex] = find_set(parent[vertex])
    return parent[vertex]
def union(u, v):
    root_u = find_set(u)
    root_v = find_set(v)
    if root_u != root_v:
        parent[root_u] = root_v
def kruskal(graph):
    mst = set()
    for vertex in graph['V']:
        make_set(vertex)
    sorted_edges = sorted(graph['E'])
    for edge in sorted_edges:
        weight, u, v = edge
        if find_set(u) != find_set(v):
            mst.add(edge)
            union(u, v)
    return mst
graph = {
    'V': ['A', 'B', 'C', 'D', 'E'],
    'E': [
        (1, 'A', 'B'),
        (2, 'B', 'C'),
        (3, 'C', 'D'),
        (4, 'D', 'E'),
        (5, 'A', 'E'),
        (6, 'B', 'D')
    ]
}
mst = kruskal(graph)
print("Minimum Spanning Tree:", mst)