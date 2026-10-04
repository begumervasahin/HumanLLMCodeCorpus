import heapq
class Graph:
    def __init__(self):
        self.edges = {}
        self.weights = {}
    def add_directed_edge(self, from_node, to_node, weight):
        self.edges.setdefault(from_node, []).append(to_node)
        self.weights[(from_node, to_node)] = weight
    def add_undirected_edge(self, node1, node2, weight):
        self.add_directed_edge(node1, node2, weight)
        self.add_directed_edge(node2, node1, weight)
def dijkstra(graph, start):
    shortest_paths = {start: (None, 0)}
    priority_queue = [(0, start)]
    while priority_queue:
        current_weight, current_node = heapq.heappop(priority_queue)
        for neighbor in graph.edges.get(current_node, []):
            weight = current_weight + graph.weights[(current_node, neighbor)]
            if neighbor not in shortest_paths or weight < shortest_paths[neighbor][1]:
                shortest_paths[neighbor] = (current_node, weight)
                heapq.heappush(priority_queue, (weight, neighbor))
    return shortest_paths
def get_dijkstra_path(graph, start, end):
    shortest_paths = dijkstra(graph, start)
    path = []
    while end:
        path.append(end)
        end = shortest_paths[end][0]
    path.reverse()
    return path
def main():
    directed_graph = Graph()
    directed_graph.add_directed_edge('a', 'b', 4)
    directed_graph.add_directed_edge('a', 'h', 8)
    directed_graph.add_directed_edge('b', 'c', 8)
    directed_graph.add_directed_edge('c', 'd', 7)
    directed_graph.add_directed_edge('b', 'h', 11)
    directed_graph.add_directed_edge('h', 'i', 7)
    directed_graph.add_directed_edge('i', 'c', 2)
    directed_graph.add_directed_edge('i', 'g', 6)
    directed_graph.add_directed_edge('h', 'g', 1)
    directed_graph.add_directed_edge('g', 'f', 2)
    directed_graph.add_directed_edge('c', 'f', 4)
    directed_graph.add_directed_edge('d', 'f', 14)
    directed_graph.add_directed_edge('d', 'e', 9)
    directed_graph.add_directed_edge('f', 'e', 10)
    undirected_graph = Graph()
    undirected_graph.add_undirected_edge('s', 't', 10)
    undirected_graph.add_undirected_edge('s', 'y', 5)
    undirected_graph.add_undirected_edge('t', 'x', 1)
    undirected_graph.add_undirected_edge('y', 'z', 2)
    undirected_graph.add_undirected_edge('t', 'y', 2)
    undirected_graph.add_undirected_edge('y', 't', 3)
    undirected_graph.add_undirected_edge('x', 'z', 4)
    undirected_graph.add_undirected_edge('z', 'x', 6)
    undirected_graph.add_undirected_edge('y', 'x', 9)
    undirected_graph.add_undirected_edge('z', 's', 7)
    path = get_dijkstra_path(undirected_graph, 't', 's')
    print(f"The shortest path from 't' to 's' is: {path}")
if __name__ == "__main__":
    main()