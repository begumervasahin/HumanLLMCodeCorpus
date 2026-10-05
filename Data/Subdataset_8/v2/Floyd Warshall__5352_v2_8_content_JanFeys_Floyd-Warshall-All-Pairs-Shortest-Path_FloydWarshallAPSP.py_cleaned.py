import time
import sys
from collections import defaultdict
class WeightedDirectedGraph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.edges = defaultdict(set)
        self.weights = dict()
    def add_edge(self, source, destination, weight):
        self.edges[source].add(destination)
        self.weights[(source, destination)] = weight
    def remove_edge(self, source, destination):
        self.edges[source].remove(destination)
        del self.weights[(source, destination)]
    def run_floyd_warshall(self):
        distance_matrix = [[0 if i == j else sys.maxsize for j in range(self.num_vertices)] for i in range(self.num_vertices)]
        for source in self.edges:
            for destination in self.edges[source]:
                distance_matrix[source][destination] = self.weights[(source, destination)]
        for k in range(self.num_vertices):
            for i in range(self.num_vertices):
                for j in range(self.num_vertices):
                    distance_matrix[i][j] = min(distance_matrix[i][j], distance_matrix[i][k] + distance_matrix[k][j])
        for i in range(self.num_vertices):
            if distance_matrix[i][i] < 0:
                print("Negative cycle detected!")
                return None
        return distance_matrix
    def display(self):
        num_edges_present = 0
        for source in self.edges:
            for destination in self.edges[source]:
                print(f"Edge from {source} to {destination} with weight {self.weights[(source, destination)]}")
                num_edges_present += 1
        print(f"There are {num_edges_present} edges in total.")
if __name__ == "__main__":
    file_name = 'APSPtest3.txt'
    start_time = time.time()
    with open(file_name, 'r') as file:
        num_vertices, _ = map(int, file.readline().strip().split())
        graph = WeightedDirectedGraph(num_vertices)
        for line in file:
            source, destination, weight = map(int, line.strip().split())
            graph.add_edge(source - 1, destination - 1, weight)
    shortest_paths = graph.run_floyd_warshall()
    if shortest_paths:
        for source in range(num_vertices):
            for destination in range(num_vertices):
                print(f"From {source} to {destination}, shortest path is {shortest_paths[source][destination]}")
        print("Minimum shortest path:", min(min(shortest_paths)))
    end_time = time.time()
    print("Execution time:", end_time - start_time)