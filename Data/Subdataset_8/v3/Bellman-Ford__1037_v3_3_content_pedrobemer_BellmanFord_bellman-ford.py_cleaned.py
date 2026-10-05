import argparse
class BellmanFord:
    def __init__(self, start_node, graph):
        self.graph = graph
        self.distances = {node: float('inf') for node in graph}
        self.distances[start_node] = 0
        self.start_node = start_node
        self.relax()
        self.detect_negative_cycle()
    def relax(self):
        num_vertices = len(self.graph)
        for _ in range(num_vertices - 1):
            for node in self.graph:
                for neighbor, weight in self.graph[node].items():
                    if self.distances[node] == float('inf'):
                        continue
                    new_distance = self.distances[node] + weight
                    if new_distance < self.distances[neighbor]:
                        self.distances[neighbor] = new_distance
        print("Shortest distances from", self.start_node + ":", self.distances)
    def detect_negative_cycle(self):
        for node in self.graph:
            for neighbor, weight in self.graph[node].items():
                if self.distances[node] + weight < self.distances[neighbor]:
                    print('The graph has a negative-weight cycle.')
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--node', type=str, required=True, help='Starting node')
    args = parser.parse_args()
    graph = {
        'A': {'B': 6, 'C': 7},
        'B': {'C': 8, 'D': 5, 'E': -4},
        'C': {'D': -3, 'E': 9},
        'D': {'B': -2},
        'E': {'A': 2}
    }
    bellman_ford = BellmanFord(args.node, graph)