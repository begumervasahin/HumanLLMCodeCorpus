import time
from collections import defaultdict
import sys
class WeightedDirectedGraph:
    def __init__(self, num_vertices: int):
        self.num_vertices = num_vertices
        self.edges = defaultdict(set)
        self.weights = {}
    def add_edge(self, tail: int, head: int, weight: int):
        self.edges[tail].add(head)
        self.weights[(tail, head)] = weight
    def get_edges(self, tail: int) -> set:
        return self.edges[tail]
    def get_weight(self, tail: int, head: int) -> int:
        return self.weights.get((tail, head), sys.maxsize)
    def remove_edge(self, tail: int, head: int):
        if head in self.edges[tail]:
            self.edges[tail].remove(head)
            del self.weights[(tail, head)]
    def display_edges(self):
        edge_count = 0
        for tail in self.edges:
            for head in self.edges[tail]:
                print(f"Edge from {tail} to {head} with weight {self.weights[(tail, head)]}")
                edge_count += 1
        print(f"There are {edge_count} edges in total.")
    def run_floyd_warshall(self) -> list:
        self.distance_matrix = [
            [0 if i == j else sys.maxsize for j in range(self.num_vertices)]
            for i in range(self.num_vertices)
        ]
        for tail in self.edges:
            for head in self.edges[tail]:
                self.distance_matrix[tail][head] = self.weights[(tail, head)]
        for k in range(self.num_vertices):
            self.temp_matrix = [row[:] for row in self.distance_matrix]
            for i in range(self.num_vertices):
                for j in range(self.num_vertices):
                    self.distance_matrix[i][j] = min(
                        self.temp_matrix[i][j],
                        self.temp_matrix[i][k] + self.temp_matrix[k][j]
                    )
        for i in range(self.num_vertices):
            if self.distance_matrix[i][i] < 0:
                print("Negative cycle detected!")
                sys.exit()
        return self.distance_matrix
if __name__ == "__main__":
    file_name = 'APSPtest3.txt'
    start_time = time.time()
    with open(file_name, 'r') as file:
        num_vertices, _ = map(int, file.readline().strip().split())
        graph = WeightedDirectedGraph(num_vertices)
        for line in file:
            tail, head, weight = map(int, line.strip().split())
            graph.add_edge(tail - 1, head - 1, weight)
    shortest_paths = graph.run_floyd_warshall()
    for i in range(num_vertices):
        for j in range(num_vertices):
            print(f"From {i} to {j} the shortest path is {shortest_paths[i][j]}")
    min_distance = min(min(row) for row in shortest_paths)
    print(f"Minimum distance is {min_distance}")
    end_time = time.time()
    print(f"Time taken: {end_time - start_time:.4f} seconds")