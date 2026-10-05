import heapq
from graph import Vertex, Graph
def shortest_path_to_vertex(vertex, path):
    if vertex.previous:
        path.append(vertex.previous.get_id())
        shortest_path_to_vertex(vertex.previous, path)
def dijkstra_shortest_paths(graph, start_vertex):
    start_vertex.set_distance(0)
    unvisited_vertices = [(v.get_distance(), v) for v in graph]
    heapq.heapify(unvisited_vertices)
    while unvisited_vertices:
        current_distance, current_vertex = heapq.heappop(unvisited_vertices)
        current_vertex.set_visited()
        for neighbor_vertex in current_vertex.adjacent:
            if neighbor_vertex.visited:
                continue
            new_distance = current_vertex.get_distance() + current_vertex.get_weight(neighbor_vertex)
            if new_distance < neighbor_vertex.get_distance():
                neighbor_vertex.set_distance(new_distance)
                neighbor_vertex.set_previous(current_vertex)
        while unvisited_vertices:
            heapq.heappop(unvisited_vertices)
        unvisited_vertices = [(v.get_distance(), v) for v in graph if not v.visited]
        heapq.heapify(unvisited_vertices)
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
    shortest_path_to_vertex(target_vertex, shortest_path_list)
    print(shortest_path_list[::-1])
