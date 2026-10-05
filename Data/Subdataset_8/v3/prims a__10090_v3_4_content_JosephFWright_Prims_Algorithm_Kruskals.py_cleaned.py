class Weighted_Graph:
    def __init__(self, edge_file_name):
        pass
def kruskals(edge_file_name, start_vertex=0):
    def find(parent, i):
        if parent[i] == i:
            return i
        return find(parent, parent[i])
    def union(parent, rank, x, y):
        x_root = find(parent, x)
        y_root = find(parent, y)
        if rank[x_root] < rank[y_root]:
            parent[x_root] = y_root
        elif rank[x_root] > rank[y_root]:
            parent[y_root] = x_root
        else:
            parent[y_root] = x_root
            rank[x_root] += 1
    graph = Weighted_Graph(edge_file_name)
    sorted_edges = sorted(graph.edges(), key=lambda x: x[2])
    num_vertices = len(graph.vertex_set())
    parent = [i for i in range(num_vertices)]
    rank = [0] * num_vertices
    minimum_spanning_tree = []
    for edge in sorted_edges:
        u, v, weight = edge
        x = find(parent, u)
        y = find(parent, v)
        if x != y:
            minimum_spanning_tree.append(edge)
            union(parent, rank, x, y)
    return minimum_spanning_tree
