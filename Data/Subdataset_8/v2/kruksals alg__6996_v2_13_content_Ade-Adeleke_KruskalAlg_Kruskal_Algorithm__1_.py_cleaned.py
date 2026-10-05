
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
        for edge in edges:
            parent[ancestor1] = ancestor2
def kruskal(graph):
    kmst = set()
    for vertice in graph['V']:
        make_set(vertice)
    edges = sorted(list(graph['E']))
    for edge in edges:
        weight, u, v = edge
        if find_set(u) != find_set(v):
            kmst.add(edge)
            union(u, v, edges)
    return kmst
graph = {
    'V': ['A', 'B', 'C', 'D', 'E'],
    'E': [(1, 'A', 'B'), (3, 'A', 'C'), (2, 'B', 'C'), (5, 'B', 'D'), (4, 'C', 'D'), (6, 'C', 'E'), (7, 'D', 'E')]
}
minimum_spanning_tree = kruskal(graph)
print("Minimum Spanning Tree:", minimum_spanning_tree)