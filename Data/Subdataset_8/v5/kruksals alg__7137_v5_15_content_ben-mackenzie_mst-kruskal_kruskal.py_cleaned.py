from disjoint_sets import DisjointSets
from heap_priority_queue import HeapPriorityQueue
def compute_mst_kruskal(graph):
    mst_edges = []
    priority_queue = HeapPriorityQueue()
    disjoint_sets = DisjointSets()
    vertex_positions = {}
    for vertex in graph.vertices():
        vertex_positions[vertex] = disjoint_sets.make_group(vertex)
    for edge in graph.edges():
        priority_queue.insert(edge)
    num_vertices = graph.vertex_count()
    while len(mst_edges) != num_vertices - 1 and not priority_queue.is_empty():
        edge = priority_queue.delete_min()
        u, v = edge.endpoints()
        a = disjoint_sets.find(vertex_positions[u])
        b = disjoint_sets.find(vertex_positions[v])
        if a != b:
            mst_edges.append(edge)
            disjoint_sets.union_sets(a, b)
    return mst_edges