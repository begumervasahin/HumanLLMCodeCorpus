import time
from collections import defaultdict
import sys
class WeightedDirectedGraph:
    def __init__(self, nr_vs: int):
        self.nr_vs = nr_vs
        self.es = defaultdict(set)
        self.ws = dict()
    def show_nr_vs(self) -> int:
        return self.nr_vs
    def add_edge(self, t: int, h: int, w: int):
        self.es[t].add(h)
        self.ws[(t, h)] = w
    def get_edges(self, t: int) -> set:
        return self.es[t]
    def get_weight(self, t: int, h: int) -> int:
        return self.ws[(t, h)]
    def remove_edge(self, t: int, h: int):
        self.es[t].remove(h)
        del self.ws[(t, h)]
    def display(self):
        nr_es_present = 0
        for t in self.es:
            for h in self.es[t]:
                print(f"Edge from {t} to {h} with weight {self.ws[(t, h)]}")
                nr_es_present += 1
        print(f"There are {nr_es_present} edges in total.")
    def run_floyd_warshall(self) -> list:
        self.A = [[0 if t == h else sys.maxsize for h in range(self.nr_vs)] for t in range(self.nr_vs)]
        for t in range(self.nr_vs):
            for h in self.es[t]:
                self.A[t][h] = self.ws[(t, h)]
        for k in range(self.nr_vs):
            self.B = [row[:] for row in self.A]
            for t in range(self.nr_vs):
                for h in range(self.nr_vs):
                    self.A[t][h] = min(self.B[t][h], self.B[t][k] + self.B[k][h])
        for t in range(self.nr_vs):
            if self.A[t][t] < 0:
                print("There is a negative cycle!")
                sys.exit()
        return self.A
if __name__ == "__main__":
    file_name = 'APSPtest3.txt'
    start_time = time.time()
    with open(file_name, 'r') as file:
        nr_vs, _ = map(int, file.readline().strip().split())
        graph = WeightedDirectedGraph(nr_vs)
        for line in file:
            t, h, w = map(int, line.strip().split())
            graph.add_edge(t - 1, h - 1, w)
    shortest_paths = graph.run_floyd_warshall()
    for t in range(nr_vs):
        for h in range(nr_vs):
            print(f"From {t} to {h} the shortest path is {shortest_paths[t][h]}")
    min_distance = min(min(row) for row in shortest_paths)
    print(f"Minimum distance is {min_distance}")
    end_time = time.time()
    print(f"Time taken: {end_time - start_time:.4f} seconds")