import heapq
class Vertex:
    def __init__(self, vertex_id):
        self.vertex_id = vertex_id
        self.distance = float('inf')
        self.previous = None
        self.adjacent = []
        self.visited = False
    def get_id(self):
        return self.vertex_id
    def get_distance(self):
        return self.distance
    def set_distance(self, distance):
        self.distance = distance
    def get_previous(self):
        return self.previous
    def set_previous(self, previous):
        self.previous = previous
    def add_neighbor(self, neighbor, weight):
        self.adjacent.append((neighbor, weight))
    def get_weight(self, neighbor):
        for n, weight in self.adjacent:
            if n == neighbor:
                return weight
        return float('inf')
    def set_visited(self):
        self.visited = True
class Graph:
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex):
        self.vertices[vertex.get_id()] = vertex
    def get_vertex(self, vertex_id):
        return self.vertices.get(vertex_id)
    def add_edge(self, from_id, to_id, weight):
        from_vertex = self.get_vertex(from_id)
        to_vertex = self.get_vertex(to_id)
        if from_vertex and to_vertex:
            from_vertex.add_neighbor(to_vertex, weight)
            to_vertex.add_neighbor(from_vertex, weight)
def dijkstra(graph, start_id):
    start = graph.get_vertex(start_id)
    start.set_distance(0)
    unvisited_queue = [(vertex.get_distance(), vertex) for vertex in graph.vertices.values()]
    heapq.heapify(unvisited_queue)
    while unvisited_queue:
        current_distance, current_vertex = heapq.heappop(unvisited_queue)
        if current_vertex.visited:
            continue
        current_vertex.set_visited()
        for neighbor, weight in current_vertex.adjacent:
            if neighbor.visited:
                continue
            new_distance = current_vertex.get_distance() + weight
            if new_distance < neighbor.get_distance():
                neighbor.set_distance(new_distance)
                neighbor.set_previous(current_vertex)
        unvisited_queue = [(vertex.get_distance(), vertex) for vertex in graph.vertices.values() if not vertex.visited]
        heapq.heapify(unvisited_queue)
    distances = {vertex.get_id(): vertex.get_distance() for vertex in graph.vertices.values()}
    predecessors = {vertex.get_id(): vertex.get_previous().get_id() if vertex.get_previous() else None for vertex in graph.vertices.values()}
    return distances, predecessors
def print_path(vertex, predecessors, graph):
    path = []
    while vertex:
        path.append(vertex.get_id())
        vertex = graph.get_vertex(predecessors.get(vertex.get_id()))
    path.reverse()
    print(" -> ".join(map(str, path)))
if __name__ == '__main__':
    graph = Graph()
    nodes = [0, 1, 2, 3, 4]
    edges = [
        (0, 1, 6),
        (0, 2, 1),
        (0, 3, 4),
        (1, 4, 3),
        (2, 1, -3),
        (2, 3, 2),
        (3, 4, -1),
        (4, 2, 5)
    ]
    for node_id in nodes:
        graph.add_vertex(Vertex(node_id))
    for from_id, to_id, weight in edges:
        graph.add_edge(from_id, to_id, weight)
    distances, predecessors = dijkstra(graph, 0)
    print("Shortest distances from start node 0 to all other nodes:")
    for node_id, distance in distances.items():
        print(f"Node {node_id}: Distance = {distance}")
    print("\nShortest paths from start node 0:")
    for node_id in nodes:
        print(f"Path to node {node_id}:")
        print_path(graph.get_vertex(node_id), predecessors, graph)