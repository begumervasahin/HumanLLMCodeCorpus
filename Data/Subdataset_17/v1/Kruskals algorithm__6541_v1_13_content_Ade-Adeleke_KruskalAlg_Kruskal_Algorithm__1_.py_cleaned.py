
parent = {}
def make_set(vertice):
    parent[vertice] = vertice
def find_set(vertice):
    if parent[vertice] != vertice:
        parent[vertice] = find_set(parent[vertice])
    return parent[vertice]
def union(u, v, edges):
    ancestor1 = find_set(u)
    ancestor2 = find_set(v)
    if ancestor1 != ancestor2:
        parent[ancestor1] = ancestor2
def kruskal(graph):
    kmst = set()
    for vertice in graph['V']:
        make_set(vertice)
    edges = list(graph['E'])
    edges.sort()
    for edge in edges:
        weight, u, v = edge
        if find_set(u) != find_set(v):
            kmst.add(edge)
            union(u, v, edges)
    return kmst
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