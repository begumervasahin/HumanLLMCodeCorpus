import random
from itertools import chain
import matplotlib.pyplot as plt
class Graph:
    def __init__(self):
        self.graph_dict = {}
    def add_edge(self, node, neighbour):
        if node not in self.graph_dict:
            self.graph_dict[node] = []
        if neighbour not in self.graph_dict[node] and neighbour != node:
            self.graph_dict[node].append(neighbour)
    def show_edges(self):
        for node in self.graph_dict:
            for neighbour in self.graph_dict[node]:
                print(f"({node}, {neighbour})")
    def bfs(self, start, destination):
        original_start = start
        visited = {node: False for node in self.graph_dict}
        parent_dict = {}
        queue = [start]
        visited[start] = True
        while queue:
            current_node = queue.pop(0)
            for neighbour in self.graph_dict[current_node]:
                if not visited[neighbour]:
                    parent_dict[neighbour] = current_node
                    if neighbour == destination:
                        self.print_path(parent_dict, original_start, destination)
                        return
                    visited[neighbour] = True
                    queue.append(neighbour)
        print("NO FLIGHT PATH AVAILABLE")
    def print_path(self, parent_dict, start, destination):
        print("OPTIMAL ROUTE:", end=" ")
        current = destination
        path = []
        while current != start:
            path.append(current)
            current = parent_dict.get(current, start)
        path.append(start)
        print(" - ".join(reversed(path)))
    def generate_graph(self, max_nodes, percentage_cities):
        for i in range(max_nodes):
            random_range = chain(range(0, i), range(i + 1, max_nodes))
            random_neighbours = random.sample(list(random_range), round(max_nodes * percentage_cities))
            for neighbour in random_neighbours:
                self.add_edge(str(i + 1), str(neighbour + 1))
                self.add_edge(str(neighbour + 1), str(i + 1))
if __name__ == "__main__":
    g = Graph()
    g.generate_graph(10, 0.3)
    g.show_edges()
    g.bfs('1', '7')
This project measures the time taken for the BFS algorithm for:
1. Different numbers of cities in graphs (vertices).
2. Different numbers of non-stop flights (edges).
To plot the shortest path for an airline, enabling a passenger to fly from city A (Singapore) to city B (Florida).
1. To find how the number of cities in the network affects the time taken for the BFS algorithm:
   ```sh
   $ python numCities.py