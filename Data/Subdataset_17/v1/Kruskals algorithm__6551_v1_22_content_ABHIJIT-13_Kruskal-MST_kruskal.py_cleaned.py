def root(vertex):
    while root_ids[vertex] != vertex:
        root_ids[vertex] = root_ids[root_ids[vertex]]
        vertex = root_ids[vertex]
    return vertex
def union(u, v):
    u_root = root(u)
    v_root = root(v)
    root_ids[v_root] = u_root
def kruskal(graph_edges):
    global root_ids
    min_weight = 0
    for edge in graph_edges:
        u, v, weight = edge
        if root(u) != root(v):
            min_weight += weight
            union(u, v)
    return min_weight
V, E = map(int, input("Enter number of vertices and edges: ").split())
graph_edges = []
for i in range(E):
    u, v, weight = map(int, input("Enter edge (u v weight): ").split())
    graph_edges.append([u, v, weight])
graph_edges = sorted(graph_edges, key=lambda x: x[2])
root_ids = list(range(V + 1))
print("Total weight of Minimum Spanning Tree:", kruskal(graph_edges))
Enter number of vertices and edges: 5 7
Enter edge (u v weight): 1 2 2
Enter edge (u v weight): 1 3 3
Enter edge (u v weight): 2 3 1
Enter edge (u v weight): 2 4 4
Enter edge (u v weight): 3 4 5
Enter edge (u v weight): 4 5 6
Enter edge (u v weight): 3 5 7
Total weight of Minimum Spanning Tree: 16