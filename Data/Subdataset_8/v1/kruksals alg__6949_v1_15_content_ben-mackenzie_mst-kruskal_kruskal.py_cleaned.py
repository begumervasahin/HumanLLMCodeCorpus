from DisJSets import DisJSet
from heapqriorityqueue import HeapPriorityQueue
def MST_Kruskal(g):
    '''Computes a minimum spanning tree of a graph using Kruskal's algorithm
    Returns a list of edges that comprise the MST
    MUST return a set of vertices with their associated edges
    PLUS the total weight of the MST
    The elements of the graph's edges are assumed to be weights
    '''
    tree = []
    pq = HeapPriorityQueue()
    forest = DisJSet()
    position = {}
    for v in g.vertices():
        position[v] = forest.make_group(v)
    for e in g.edges():
        pq.insert(e)
    size = g.vertex_count()
    while len(tree) != size - 1 and not pq.is_empty():
        edge = pq.deleteMin()
        u, v = edge.endpoints()
        a = forest.find(position[u])
        b = forest.find(position[v])
        if a != b:
            tree.append(edge)
            forest.unionSets(a, b)
    return tree
class Graph:
    def __init__(self):
        self.vertices = set()
        self.edges = []
    def add_vertex(self, vertex):
        self.vertices.add(vertex)
    def add_edge(self, edge):
        self.edges.append(edge)
    def vertex_count(self):
        return len(self.vertices)
    def vertices(self):
        return self.vertices
    def edges(self):
        return self.edges
    def endpoints(self):
        return (self.start, self.end)
g = Graph()
g.add_vertex('A')
g.add_vertex('B')
g.add_vertex('C')
g.add_edge(('A', 'B', 1))
g.add_edge(('B', 'C', 2))
g.add_edge(('A', 'C', 3))
minimum_spanning_tree = MST_Kruskal(g)
print("Minimum Spanning Tree:", minimum_spanning_tree)