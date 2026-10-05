from collections import namedtuple
from MaxHeap import MaxHeap
NUMBER_OF_VERTICES = 5000
Edge = namedtuple('Edge', ['vertex', 'weight'])
status = [None] * NUMBER_OF_VERTICES
wt = [None] * NUMBER_OF_VERTICES
def dijkstras_with_heap(graph, source, destination):
    max_heap = MaxHeap()
    dad = [None] * NUMBER_OF_VERTICES
    for vertex in graph.get_vertex():
        status[vertex] = 'unseen'
    status[source] = 'intree'
    for edge in graph.get_edge(source):
        status[edge.vertex] = 'fringe'
        wt[edge.vertex] = edge.weight
        max_heap.insert(edge.vertex, edge.weight)
        dad[edge.vertex] = source
    while 'fringe' in status:
        destination_found = False
        v = max_heap.maximum()
        if v == destination:
            break
        status[v] = 'intree'
        max_heap.delete(v)
        for e in graph.get_edge(v):
            if status[e.vertex] == 'unseen':
                status[e.vertex] = 'fringe'
                dad[e.vertex] = v
                wt[e.vertex] = min(wt[v], e.weight)
                max_heap.insert(e.vertex, wt[e.vertex])
            elif status[e.vertex] == 'fringe' and wt[e.vertex] < min(wt[v], e.weight):
                dad[e.vertex] = v
                max_heap.delete(e.vertex)
                wt[e.vertex] = min(wt[v], e.weight)
                max_heap.insert(e.vertex, wt[e.vertex])
    max_bw_path = []
    end = destination
    while end is not None:
        max_bw_path.append(end)
        end = dad[end]
    max_bw_path.reverse()
    return max_bw_path, wt[destination]
class Graph:
    def __init__(self):
        self.vertices = set()
        self.edges = {}
    def add_vertex(self, vertex):
        self.vertices.add(vertex)
    def add_edge(self, start, end, weight):
        if start not in self.edges:
            self.edges[start] = []
        self.edges[start].append(Edge(end, weight))
    def get_vertex(self):
        return self.vertices
    def get_edge(self, vertex):
        return self.edges.get(vertex, [])
g = Graph()
g.add_vertex(1)
g.add_vertex(2)
g.add_vertex(3)
g.add_edge(1, 2, 5)
g.add_edge(1, 3, 9)
g.add_edge(2, 3, 2)
source_vertex = 1
destination_vertex = 3
shortest_path, weight = dijkstras_with_heap(g, source_vertex, destination_vertex)
print("Shortest Path:", shortest_path)
print("Weight of Shortest Path:", weight)