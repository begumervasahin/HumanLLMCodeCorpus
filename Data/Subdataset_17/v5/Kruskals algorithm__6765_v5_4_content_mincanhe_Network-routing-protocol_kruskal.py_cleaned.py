
parent = {}
rank = {}
def make_set(vertex):
    parent[vertex] = vertex
    rank[vertex] = 0
def find(vertex):
    if parent[vertex] != vertex:
        parent[vertex] = find(parent[vertex])
    return parent[vertex]
def union(vertex1, vertex2):
    root1 = find(vertex1)
    root2 = find(vertex2)
    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
            if rank[root1] == rank[root2]:
                rank[root2] += 1
def kruskal(graph):
    for vertex in graph['vertices']:
        make_set(vertex)
    mst = set()
    edges = sorted(graph['edges'])
    for edge in edges:
        weight, vertex1, vertex2 = edge
        if find(vertex1) != find(vertex2):
            union(vertex1, vertex2)
            mst.add(edge)
    return mst
