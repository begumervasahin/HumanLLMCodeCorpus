def make_set(vertice):
    parent[vertice] = vertice
def find_set(vertice):
    if parent[vertice] != vertice:
        parent[vertice] = find_set(parent[vertice])
    return parent[vertice]
def union(u, v, edges):
    root_u = find_set(u)
    root_v = find_set(v)
    if root_u != root_v:
        parent[root_u] = root_v
def kruskal(graph):
    mst = set()
    for vertex in graph['V']:
        make_set(vertex)
    edges = sorted(graph['E'])
    for edge in edges:
        weight, u, v = edge
        if find_set(u) != find_set(v):
            mst.add(edge)
            union(u, v, edges)
    return mst