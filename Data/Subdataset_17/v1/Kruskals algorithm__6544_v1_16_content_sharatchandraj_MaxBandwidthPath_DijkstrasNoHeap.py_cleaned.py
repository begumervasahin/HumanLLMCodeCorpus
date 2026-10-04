from collections import namedtuple
Edge = namedtuple('Edge', ['vertex', 'weight'])
class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.edges = {i: [] for i in range(num_vertices)}
    def add_edge(self, u, v, weight):
        self.edges[u].append(Edge(v, weight))
        self.edges[v].append(Edge(u, weight))
    def get_vertex(self):
        return list(self.edges.keys())
    def get_edge(self, u):
        return self.edges[u]
class DijkstraNoHeap:
    def __init__(self, graph):
        self.graph = graph
        self.num_vertices = graph.num_vertices
        self.status = ['unseen'] * self.num_vertices
        self.dad = [None] * self.num_vertices
        self.wt = [0] * self.num_vertices
    def pick_best_vertex(self):
        best_weight = 0
        best_vertex = None
        for i in range(self.num_vertices):
            if self.status[i] == 'fringe' and self.wt[i] > best_weight:
                best_weight = self.wt[i]
                best_vertex = i
        return best_vertex
    def find_max_bandwidth_path(self, source, destination):
        self.status[source] = 'intree'
        for edge in self.graph.get_edge(source):
            self.status[edge.vertex] = 'fringe'
            self.wt[edge.vertex] = edge.weight
            self.dad[edge.vertex] = source
        while 'fringe' in self.status:
            v = self.pick_best_vertex()
            if v is None:
                break
            self.status[v] = 'intree'
            for edge in self.graph.get_edge(v):
                if self.status[edge.vertex] == 'unseen':
                    self.status[edge.vertex] = 'fringe'
                    self.dad[edge.vertex] = v
                    self.wt[edge.vertex] = min(self.wt[v], edge.weight)
                elif self.status[edge.vertex] == 'fringe' and self.wt[edge.vertex] < min(self.wt[v], edge.weight):
                    self.dad[edge.vertex] = v
                    self.wt[edge.vertex] = min(self.wt[v], edge.weight)
        max_bw_path = []
        end = destination
        while end is not None:
            max_bw_path.append(end)
            end = self.dad[end]
        max_bw_path.reverse()
        return max_bw_path, self.wt[destination]
if __name__ == "__main__":
    NumberOfVertices = 5000
    graph = Graph(NumberOfVertices)
    source = 0
    destination = 4999
    dijkstra = DijkstraNoHeap(graph)
    path, max_bandwidth = dijkstra.find_max_bandwidth_path(source, destination)
    print(f"Maximum Bandwidth Path: {path}")
    print(f"Maximum Bandwidth: {max_bandwidth}")