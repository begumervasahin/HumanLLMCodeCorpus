def find_root(vertex):
    if rootIds[vertex] == vertex:
        return vertex
    else:
        while rootIds[vertex] != vertex:
            rootIds[vertex] = rootIds[rootIds[vertex]]
            vertex = rootIds[vertex]
        return vertex
def union(u, v):
    u_root = find_root(u)
    v_root = find_root(v)
    rootIds[v_root] = rootIds[u_root]
def kruskal(GE):
    global rootIds
    min_weight = 0
    for edge in GE:
        u, v, weight = edge
        if find_root(u) != find_root(v):
            min_weight += weight
            union(u, v)
    return min_weight
V, E = map(int, input().split())
GE = []
for i in range(E):
    GE.append(list(map(int, input().split())))
GE = sorted(GE, key=lambda x: x[2])
rootIds = list(range(V + 1))
print(kruskal(GE)))