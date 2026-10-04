import random
from itertools import chain
import time
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
                print(f"({node}, {neighbour})")
    def bfs(self, start, destination):
        original_start = start
        visited = {i: False for i in self.graph_dict}
        parent_dict = {}
        queue = [start]
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
        current = destination
        path = []
        while current != start:
            path.append(current)
            current = parent_dict[current]
        path.append(start)
        path.reverse()
        print(" - ".join(path))
    def generate_graph(self, max_nodes, percentage_cities):
        for i in range(max_nodes):
            random_range = chain(range(0, i), range(i + 1, max_nodes))
            random_neighbour_array = random.sample(list(random_range), round(max_nodes * percentage_cities))
            for neighbour in random_neighbour_array:
                self.add_edge(str(i + 1), str(neighbour + 1))
                self.add_edge(str(neighbour + 1), str(i + 1))
def measure_bfs_time(num_cities, percentage_cities, start_city, end_city):
    graph = Graph()
    graph.generate_graph(num_cities, percentage_cities)
    start_time = time.time()
    graph.bfs(start_city, end_city)
    end_time = time.time()
    return end_time - start_time
def plot_bfs_time_vs_cities():
    num_cities_list = [10, 20, 50, 100, 200, 500, 1000]
    percentage_cities = 0.1
    times = []
    for num_cities in num_cities_list:
        time_taken = measure_bfs_time(num_cities, percentage_cities, '1', str(num_cities))
        times.append(time_taken)
        print(f"Number of cities: {num_cities}, Time taken: {time_taken:.5f} seconds")
    plt.plot(num_cities_list, times, marker='o')
    plt.xlabel('Number of Cities')
    plt.ylabel('Time taken for BFS (seconds)')
    plt.title('BFS Time vs Number of Cities')
    plt.grid(True)
    plt.show()
def plot_bfs_time_vs_edges():
    num_cities = 100
    percentage_edges_list = [0.05, 0.1, 0.2, 0.3, 0.4, 0.5]
    times = []
    for percentage_edges in percentage_edges_list:
        time_taken = measure_bfs_time(num_cities, percentage_edges, '1', '100')
        times.append(time_taken)
        print(f"Percentage of edges: {percentage_edges}, Time taken: {time_taken:.5f} seconds")
    plt.plot(percentage_edges_list, times, marker='o')
    plt.xlabel('Percentage of Edges')
    plt.ylabel('Time taken for BFS (seconds)')
    plt.title('BFS Time vs Percentage of Edges')
    plt.grid(True)
    plt.show()
if __name__ == '__main__':
    choice = input("Enter '1' to plot BFS time vs number of cities or '2' to plot BFS time vs percentage of edges: ")
    if choice == '1':
        plot_bfs_time_vs_cities()
    elif choice == '2':
        plot_bfs_time_vs_edges()
    else:
        print("Invalid choice. Exiting.")