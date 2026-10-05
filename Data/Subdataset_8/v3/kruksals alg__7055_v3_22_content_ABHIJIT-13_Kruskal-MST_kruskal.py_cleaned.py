def find_root(vertex, root_ids):
    if root_ids[vertex] == vertex:
        return vertex
    else:
        while root_ids[vertex] != vertex:
            root_ids[vertex] = root_ids[root_ids[vertex]]
            vertex = root_ids[vertex]
        return vertex
def union(u, v, root_ids):
    u_root = find_root(u, root_ids)
    v_root = find_root(v, root_ids)
    root_ids[v_root] = root_ids[u_root]
def kruskal(V, E, graph_edges):
    min_weight = 0
    graph_edges = sorted(graph_edges, key=lambda x: x[2])
    root_ids = list(range(V + 1))
    for u, v, weight in graph_edges:
        if find_root(u, root_ids) != find_root(v, root_ids):
            min_weight += weight
            union(u, v, root_ids)
    return min_weight
if __name__ == "__main__":
    V, E = map(int, input().split())
    graph_edges = [list(map(int, input().split())) for _ in range(E)]
    print(kruskal(V, E, graph_edges)))