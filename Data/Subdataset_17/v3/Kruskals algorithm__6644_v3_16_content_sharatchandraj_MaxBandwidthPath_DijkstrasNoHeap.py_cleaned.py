from collections import namedtuple
Edge = namedtuple('Edge', ['vertex', 'weight'])
class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.edges = {i: [] for i in range(num_vertices)}
    def add_edge(self, u, v, weight):
        self.edges[u].append(Edge(v, weight))
        self.edges[v].append(Edge(u, weight))
    def get_vertices(self):
        return list(self.edges.keys())
    def get_edges(self, vertex):
        return self.edges[vertex]
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
        for vertex in range(self.num_vertices):
            if self.status[vertex] == 'fringe' and self.wt[vertex] > best_weight:
                best_weight = self.wt[vertex]
                best_vertex = vertex
        return best_vertex
    def find_max_bandwidth_path(self, source, destination):
        self.status[source] = 'intree'
        for edge in self.graph.get_edges(source):
            self.status[edge.vertex] = 'fringe'
            self.wt[edge.vertex] = edge.weight
            self.dad[edge.vertex] = source
        while 'fringe' in self.status:
            best_vertex = self.pick_best_vertex()
            if best_vertex is None:
                break
            self.status[best_vertex] = 'intree'
            for edge in self.graph.get_edges(best_vertex):
                if self.status[edge.vertex] == 'unseen':
                    self.status[edge.vertex] = 'fringe'
                    self.dad[edge.vertex] = best_vertex
                    self.wt[edge.vertex] = min(self.wt[best_vertex], edge.weight)
                elif self.status[edge.vertex] == 'fringe' and self.wt[edge.vertex] < min(self.wt[best_vertex], edge.weight):
                    self.dad[edge.vertex] = best_vertex
                    self.wt[edge.vertex] = min(self.wt[best_vertex], edge.weight)
        max_bandwidth_path = []
        current_vertex = destination
        while current_vertex is not None:
            max_bandwidth_path.append(current_vertex)
            current_vertex = self.dad[current_vertex]
        max_bandwidth_path.reverse()
        return max_bandwidth_path, self.wt[destination]
if __name__ == "__main__":
    num_vertices = 5000
    graph = Graph(num_vertices)
    source = 0
    destination = num_vertices - 1
    dijkstra = DijkstraNoHeap(graph)
    path, max_bandwidth = dijkstra.find_max_bandwidth_path(source, destination)
    print(f"Maximum Bandwidth Path: {path}")
    print(f"Maximum Bandwidth: {max_bandwidth}")