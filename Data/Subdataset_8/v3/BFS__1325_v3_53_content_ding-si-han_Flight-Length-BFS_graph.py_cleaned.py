import random
from collections import deque
class Graph:
    def __init__(self):
        self.graph_dict = {}
    def add_edge(self, node, neighbour):
        if node not in self.graph_dict:
            self.graph_dict[node] = [neighbour]
        else:
            if neighbour not in self.graph_dict[node] and neighbour != node:
                self.graph_dict[node].append(neighbour)
    def show_edges(self):
        for node in self.graph_dict:
            for neighbour in self.graph_dict[node]:
                print("(", node, ", ", neighbour, ")")
    def bfs(self, start, destination):
        visited = set()
        parent_dict = {}
        queue = deque([start])
        visited.add(start)
        while queue:
            current_node = queue.popleft()
            for neighbour in self.graph_dict.get(current_node, []):
                if neighbour not in visited:
                    parent_dict[neighbour] = current_node
                    if neighbour == destination:
                        self.print_route(parent_dict, start, destination)
                        return
                    visited.add(neighbour)
                    queue.append(neighbour)
        print("NO FLIGHT PATH AVAILABLE")
    def print_route(self, parent_dict, start, destination):
        print("OPTIMAL ROUTE:", end=" ")
        current = parent_dict[destination]
        print(destination, end=" ")
        while start != current:
            print("-", current, end=" ")
            current = parent_dict[current]
        print('-', start)
    def generate_graph(self, max_cities, connectivity_percentage):
        for i in range(max_cities):
            random_range = range(0, i) + range(i + 1, max_cities)
            random_neighbours = random.sample(random_range, round(max_cities * connectivity_percentage))
            for neighbour in random_neighbours:
                self.add_edge(str(i + 1), str(neighbour + 1))
                self.add_edge(str(neighbour + 1), str(i + 1))
if __name__ == "__main__":
    graph = Graph()
    graph.generate_graph(10, 0.3)
    start_city = '1'
    destination_city = '10'
    print("Finding optimal route from", start_city, "to", destination_city)
    graph.bfs(start_city, destination_city)