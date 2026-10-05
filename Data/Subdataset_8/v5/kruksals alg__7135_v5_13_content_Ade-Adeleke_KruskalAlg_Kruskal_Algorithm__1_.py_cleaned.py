def make_set(vertice):
    parent[vertice] = vertice
def find_set(vertice):
    if parent[vertice] != vertice:
        parent[vertice] = find_set(parent[vertice])
    return parent[vertice]
def union(u, v):
    ancestor1 = find_set(u)
    ancestor2 = find_set(v)
    if ancestor1 != ancestor2:
        parent[ancestor1] = ancestor2
def kruskal(graph):
    kmst = set()
    vertices = graph['V']
    edges = sorted(list(graph['E']))
    for vertice in vertices:
        make_set(vertice)
    for weight, u, v in edges:
        if find_set(u) != find_set(v):
            kmst.add((weight, u, v))
            union(u, v)
    return kmst