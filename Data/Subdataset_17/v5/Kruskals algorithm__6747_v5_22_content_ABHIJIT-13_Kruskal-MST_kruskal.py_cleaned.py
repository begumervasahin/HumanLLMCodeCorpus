def find_root(vertex, root_ids):
    while root_ids[vertex] != vertex:
        root_ids[vertex] = root_ids[root_ids[vertex]]
        vertex = root_ids[vertex]
    return vertex
def union(u, v, root_ids):
    root_u = find_root(u, root_ids)
    root_v = find_root(v, root_ids)
    if root_u != root_v:
        root_ids[root_v] = root_u
def kruskal(graph_edges, num_vertices):
    root_ids = list(range(num_vertices + 1))
    total_weight = 0
    for u, v, weight in graph_edges:
        if find_root(u, root_ids) != find_root(v, root_ids):
            total_weight += weight
            union(u, v, root_ids)
    return total_weight
def main():
    num_vertices, num_edges = map(int, input("Enter the number of vertices and edges: ").split())
    graph_edges = []
    for _ in range(num_edges):
        u, v, weight = map(int, input("Enter the vertices and weight of the edge: ").split())
        graph_edges.append([u, v, weight])
    graph_edges.sort(key=lambda x: x[2])
    mst_weight = kruskal(graph_edges, num_vertices)
    print(f"The total weight of the Minimum Spanning Tree is: {mst_weight}")
if __name__ == "__main__":
    main()