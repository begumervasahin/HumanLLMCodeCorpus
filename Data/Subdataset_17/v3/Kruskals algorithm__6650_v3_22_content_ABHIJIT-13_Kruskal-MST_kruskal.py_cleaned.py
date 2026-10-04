def find_root(vertex):
    while root_ids[vertex] != vertex:
        root_ids[vertex] = root_ids[root_ids[vertex]]
        vertex = root_ids[vertex]
    return vertex
def union_sets(u, v):
    root_u = find_root(u)
    root_v = find_root(v)
    root_ids[root_v] = root_u
def kruskal(graph_edges):
    global root_ids
    total_weight = 0
    for u, v, weight in graph_edges:
        if find_root(u) != find_root(v):
            total_weight += weight
            union_sets(u, v)
    return total_weight
if __name__ == "__main__":
    V, E = map(int, input("Enter number of vertices and edges: ").split())
    graph_edges = []
    for _ in range(E):
        u, v, weight = map(int, input("Enter edge (u v weight): ").split())
        graph_edges.append((u, v, weight))
    graph_edges.sort(key=lambda edge: edge[2])
    root_ids = list(range(V + 1))
    mst_weight = kruskal(graph_edges)
    print("Total weight of Minimum Spanning Tree:", mst_weight)