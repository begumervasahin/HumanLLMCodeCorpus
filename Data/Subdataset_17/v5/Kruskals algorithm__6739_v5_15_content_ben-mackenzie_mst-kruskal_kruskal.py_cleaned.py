from DisJSets import DisJSet
from heapqriorityqueue import HeapPriorityQueue
def mst_kruskal(graph):
    mst = []
    priority_queue = HeapPriorityQueue()
    disjoint_set = DisJSet()
    vertex_to_group = {}
    for vertex in graph.vertices():
        vertex_to_group[vertex] = disjoint_set.make_group(vertex)
    for edge in graph.edges():
        priority_queue.insert(edge)
    num_vertices = graph.vertex_count()
    while len(mst) < num_vertices - 1 and not priority_queue.is_empty():
        edge = priority_queue.delete_min()
        u, v = edge.endpoints()
        group_u = disjoint_set.find(vertex_to_group[u])
        group_v = disjoint_set.find(vertex_to_group[v])
        if group_u != group_v:
            mst.append(edge)
            disjoint_set.union_sets(group_u, group_v)
    return mst