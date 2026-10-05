from DisJSets import DisJSet
from heapqriorityqueue import HeapPriorityQueue
def compute_minimum_spanning_tree(graph):
    '''
    Computes a minimum spanning tree of a graph using Kruskal's algorithm.
    Returns a list of edges that comprise the MST, a set of vertices with their associated edges,
    and the total weight of the MST.
    '''
    mst_edges = []
    priority_queue = HeapPriorityQueue()
    disjoint_sets = DisJSet()
    position = {}
    for vertex in graph.vertices():
        position[vertex] = disjoint_sets.make_group(vertex)
    for edge in graph.edges():
        priority_queue.insert(edge)
    while len(mst_edges) != graph.vertex_count() - 1 and not priority_queue.is_empty():
        edge = priority_queue.deleteMin()
        u, v = edge.endpoints()
        set_a = disjoint_sets.find(position[u])
        set_b = disjoint_sets.find(position[v])
        if set_a != set_b:
            mst_edges.append(edge)
            disjoint_sets.union_sets(set_a, set_b)
    return mst_edges, disjoint_sets, sum(edge[2] for edge in mst_edges) if mst_edges else 0
class Graph:
    def __init__(self):
        self.vertices_set = set()
        self.edges_list = []
    def add_vertex(self, vertex):
        self.vertices_set.add(vertex)
    def add_edge(self, edge):
        self.edges_list.append(edge)
    def vertex_count(self):
        return len(self.vertices_set)
    def vertices(self):
        return self.vertices_set
    def edges(self):
        return self.edges_list
    def endpoints(self):
        return (self.start, self.end)
g = Graph()
g.add_vertex('A')
g.add_vertex('B')
g.add_vertex('C')
g.add_edge(('A', 'B', 1))
g.add_edge(('B', 'C', 2))
g.add_edge(('A', 'C', 3))
minimum_spanning_tree, vertex_sets, total_weight = compute_minimum_spanning_tree(g)
print("Minimum Spanning Tree:", minimum_spanning_tree)
print("Vertex Sets with Associated Edges:", vertex_sets)
print("Total Weight of MST:", total_weight)