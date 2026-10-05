import random
from itertools import chain
import time
import matplotlib
matplotlib.use('qt5agg')
import matplotlib.pyplot as plt
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
        original_start = start
        visited = {}
        parent_dict = {}
        for i in self.graph_dict:
            visited[i] = False
        queue = []
        queue.append(start)
        visited[start] = True
        while queue:
            start = queue.pop(0)
            for node in self.graph_dict[start]:
                if not visited[node]:
                    parent_dict[node] = start
                    if node == destination:
                        self.print_path(parent_dict, original_start, destination)
                        return
                    visited[node] = True
                    queue.append(node)
        print("NO FLIGHT PATH AVAILABLE")
    def print_path(self, parent_dict, start, destination):
        print("OPTIMAL ROUTE:", end=" ")
        current = parent_dict[destination]
        print(destination, end=" ")
        while start != current:
            print("-", current, end=" ")
            current = parent_dict[current]
        print('-', start)
    def generate_graph(self, max_cities, percentage_cities):
        for i in range(max_cities):
            random_range = chain(range(0, i), range(i + 1, max_cities))
            random_neighbour_array = random.sample(list(random_range), round(max_cities * percentage_cities))
            for neighbour in random_neighbour_array:
                self.add_edge(str(i + 1), str(neighbour + 1))
                self.add_edge(str(neighbour + 1), str(i + 1))
"""
Measuring the time taken for BFS Algorithm for:
1. Different number of cities in graphs (Vertices)
2. Different number of non-stop flights (Edges)
Plotting the shortest path for an airline to enable a passenger to fly from city A (Singapore) to city B (Florida).
1. Finding how the number of cities in the network affect the time taken for BFS Algorithm.