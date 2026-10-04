import heapq
from collections import namedtuple, defaultdict
Edge = namedtuple('Edge', ['vertex', 'weight'])
class DijkstraWithMaxHeap:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.status = ['unseen'] * num_vertices
        self.max_bandwidth = [float('-inf')] * num_vertices
        self.parents = [None] * num_vertices
        self.graph = defaultdict(list)
    def add_edge(self, u, v, weight):
        self.graph[u].append(Edge(vertex=v, weight=weight))
        self.graph[v].append(Edge(vertex=u, weight=weight))
    def _insert_into_max_heap(self, heap, vertex, weight):
        heapq.heappush(heap, (-weight, vertex))
    def _pop_from_max_heap(self, heap):
        weight, vertex = heapq.heappop(heap)
        return -weight, vertex
    def run_dijkstra(self, source, destination):
        heap = []
        self.status[source] = 'intree'
        for edge in self.graph[source]:
            self.status[edge.vertex] = 'fringe'
            self.max_bandwidth[edge.vertex] = edge.weight
            self._insert_into_max_heap(heap, edge.vertex, edge.weight)
            self.parents[edge.vertex] = source
        while heap:
            current_bandwidth, current_vertex = self._pop_from_max_heap(heap)
            if current_vertex == destination:
                break
            self.status[current_vertex] = 'intree'
            for edge in self.graph[current_vertex]:
                new_bandwidth = min(current_bandwidth, edge.weight)
                if self.status[edge.vertex] == 'unseen':
                    self.status[edge.vertex] = 'fringe'
                    self.max_bandwidth[edge.vertex] = new_bandwidth
                    self.parents[edge.vertex] = current_vertex
                    self._insert_into_max_heap(heap, edge.vertex, new_bandwidth)
                elif self.status[edge.vertex] == 'fringe' and self.max_bandwidth[edge.vertex] < new_bandwidth:
                    self.max_bandwidth[edge.vertex] = new_bandwidth
                    self.parents[edge.vertex] = current_vertex
                    self._insert_into_max_heap(heap, edge.vertex, new_bandwidth)
        return self._build_path(destination), self.max_bandwidth[destination]
    def _build_path(self, destination):
        path = []
        while destination is not None:
            path.append(destination)
            destination = self.parents[destination]
        return path[::-1]
if __name__ == "__main__":
    num_vertices = 5000
    dijkstra = DijkstraWithMaxHeap(num_vertices)
    source = 0
    destination = 4999
    max_bw_path, max_bandwidth = dijkstra.run_dijkstra(source, destination)
    print(f"Maximum bandwidth path: {max_bw_path}")
    print(f"Maximum bandwidth: {max_bandwidth}")