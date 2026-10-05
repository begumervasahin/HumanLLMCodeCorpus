parent = {}
rank = {}
def make_set(vertice):
    parent[vertice] = vertice
    rank[vertice] = 0
def find(vertice):
    if parent[vertice] != vertice:
        parent[vertice] = find(parent[vertice])
    return parent[vertice]
def union(vertice1, vertice2):
    root1 = find(vertice1)
    root2 = find(vertice2)
    if root1 != root2:
        if rank[root1] < rank[root2]:
            parent[root1] = root2
        else:
            parent[root2] = root1
            if rank[root1] == rank[root2]:
                rank[root2] += 1
def kruskal(graph):
    for vertice in graph['vertices']:
        make_set(vertice)
    max_bandwidth_path = set()
    edges = sorted(graph['edges'])
    for weight, vertice1, vertice2 in edges:
        if find(vertice1) != find(vertice2):
            union(vertice1, vertice2)
            max_bandwidth_path.add((weight, vertice1, vertice2))
    return max_bandwidth_path