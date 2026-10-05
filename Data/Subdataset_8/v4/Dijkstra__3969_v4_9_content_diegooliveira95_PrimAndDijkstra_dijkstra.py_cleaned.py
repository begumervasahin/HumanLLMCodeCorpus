import heapq
from graph import Vertex, Graph
def shortest_path(v, path):
    if v.previous:
        path.append(v.previous.get_id())
        shortest_path(v.previous, path)
def dijkstra_shortest_paths(graph, start):
    start.set_distance(0)
    unvisited_queue = [(vertex.get_distance(), vertex) for vertex in graph]
    heapq.heapify(unvisited_queue)
    while unvisited_queue:
        current_distance, current_vertex = heapq.heappop(unvisited_queue)
        current_vertex.set_visited()
        for next_vertex in current_vertex.adjacent:
            if next_vertex.visited:
                continue
            new_distance = current_vertex.get_distance() + current_vertex.get_weight(next_vertex)
            if new_distance < next_vertex.get_distance():
                next_vertex.set_distance(new_distance)
                next_vertex.set_previous(current_vertex)
        while unvisited_queue:
            heapq.heappop(unvisited_queue)
        unvisited_queue = [(vertex.get_distance(), vertex) for vertex in graph if not vertex.visited]
        heapq.heapify(unvisited_queue)
if __name__ == "__main__":
    graph = Graph()
    graph.add_vertex('A')
    graph.add_vertex('B')
    graph.add_vertex('C')
    graph.add_vertex('D')
    graph.add_vertex('E')
    graph.add_edge('A', 'B', 1)
    graph.add_edge('A', 'C', 3)
    graph.add_edge('B', 'D', 2)
    graph.add_edge('C', 'D', 2)
    graph.add_edge('B', 'E', 4)
    graph.add_edge('D', 'E', 1)
    dijkstra_shortest_paths(graph, graph.get_vertex('A'))
    target_vertex = graph.get_vertex('E')
    shortest_path_list = [target_vertex.get_id()]
    shortest_path(target_vertex, shortest_path_list)
    print(shortest_path_list[::-1])
