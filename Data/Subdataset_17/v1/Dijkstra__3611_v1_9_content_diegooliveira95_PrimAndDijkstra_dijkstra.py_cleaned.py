import heapq
class Vertex:
    def __init__(self, vertex_id):
        self.vertex_id = vertex_id
        self.distance = float('inf')
        self.previous = None
        self.adjacent = []
        self.visited = False
    def getId(self):
        return self.vertex_id
    def getDistance(self):
        return self.distance
    def setDistance(self, distance):
        self.distance = distance
    def getPrevious(self):
        return self.previous
    def setPrevious(self, previous):
        self.previous = previous
    def addNeighbor(self, neighbor, weight):
        self.adjacent.append((neighbor, weight))
    def getWeight(self, neighbor):
        for n, weight in self.adjacent:
            if n == neighbor:
                return weight
        return float('inf')
    def setVisited(self):
        self.visited = True
class Graph:
    def __init__(self):
        self.vertices = {}
    def addVertex(self, vertex):
        self.vertices[vertex.getId()] = vertex
    def getVertex(self, vertex_id):
        return self.vertices.get(vertex_id)
    def addEdge(self, from_id, to_id, weight):
        from_vertex = self.getVertex(from_id)
        to_vertex = self.getVertex(to_id)
        if from_vertex and to_vertex:
            from_vertex.addNeighbor(to_vertex, weight)
            to_vertex.addNeighbor(from_vertex, weight)
def dijkstra(graph, start_id):
    start = graph.getVertex(start_id)
    start.setDistance(0)
    unvisited_queue = [(vertex.getDistance(), vertex) for vertex in graph.vertices.values()]
    heapq.heapify(unvisited_queue)
    while unvisited_queue:
        current_distance, current_vertex = heapq.heappop(unvisited_queue)
        if current_vertex.visited:
            continue
        current_vertex.setVisited()
        for neighbor, weight in current_vertex.adjacent:
            if neighbor.visited:
                continue
            new_distance = current_vertex.getDistance() + weight
            if new_distance < neighbor.getDistance():
                neighbor.setDistance(new_distance)
                neighbor.setPrevious(current_vertex)
        unvisited_queue = [(vertex.getDistance(), vertex) for vertex in graph.vertices.values() if not vertex.visited]
        heapq.heapify(unvisited_queue)
    distances = {vertex.getId(): vertex.getDistance() for vertex in graph.vertices.values()}
    predecessors = {vertex.getId(): vertex.getPrevious().getId() if vertex.getPrevious() else None for vertex in graph.vertices.values()}
    return distances, predecessors
def print_path(vertex, predecessors):
    path = []
    while vertex:
        path.append(vertex.getId())
        vertex = graph.getVertex(predecessors.get(vertex.getId()))
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
        graph.addVertex(Vertex(node_id))
    for from_id, to_id, weight in edges:
        graph.addEdge(from_id, to_id, weight)
    distances, predecessors = dijkstra(graph, 0)
    print("Shortest distances from start node 0 to all other nodes:")
    for node_id, distance in distances.items():
        print(f"Node {node_id}: Distance = {distance}")
    print("\nShortest paths from start node 0:")
    for node_id in nodes:
        print(f"Path to node {node_id}:")
        print_path(graph.getVertex(node_id), predecessors)