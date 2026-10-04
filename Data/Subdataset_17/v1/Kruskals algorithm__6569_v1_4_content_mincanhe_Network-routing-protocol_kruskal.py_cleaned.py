parent = dict()
rank = dict()
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
                rank[root1] += 1
def kruskal(graph):
    for vertice in graph['vertices']:
        make_set(vertice)
    max_bandwidth_path = set()
    edges = list(graph['edges'])
    edges.sort(reverse=True)
    for edge in edges:
        weight, vertice1, vertice2 = edge
        if find(vertice1) != find(vertice2):
            union(vertice1, vertice2)
            max_bandwidth_path.add(edge)
    return max_bandwidth_path
if __name__ == "__main__":
    graph = {
        'vertices': ['A', 'B', 'C', 'D', 'E'],
        'edges': [
            (5, 'A', 'B'),
            (10, 'A', 'C'),
            (7, 'B', 'D'),
            (8, 'C', 'D'),
            (6, 'C', 'E'),
            (4, 'D', 'E')
        ]
    }
    max_bandwidth_path = kruskal(graph)
    print("Edges in the Maximum Bandwidth Path (or Minimum Spanning Tree):")
    for edge in max_bandwidth_path:
        print(edge)