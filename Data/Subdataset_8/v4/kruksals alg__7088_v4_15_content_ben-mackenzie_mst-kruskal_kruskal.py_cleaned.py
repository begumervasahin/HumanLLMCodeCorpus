from DisJSets import DisJSet
from heapqriorityqueue import HeapPriorityQueue
def MST_Kruskal(graph):
    tree = []
    priority_queue = HeapPriorityQueue()
    forest = DisJSet()
    position = {}
    for vertex in graph.vertices():
        position[vertex] = forest.make_group(vertex)
    for edge in graph.edges():
        priority_queue.insert(edge)
    size = graph.vertex_count()
    while len(tree) != size - 1 and not priority_queue.is_empty():
        edge = priority_queue.deleteMin()
        u, v = edge.endpoints()
        a = forest.find(position[u])
        b = forest.find(position[v])
        if a != b:
            tree.append(edge)
            forest.unionSets(a, b)
    return tree