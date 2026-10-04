from typing import Dict, List, Tuple
class PrimAlgorithm:
    def __init__(self, graph: Dict[str, Dict[str, int]] = None):
        self.graph = graph if graph is not None else {}
        self.visited = []
        self.mst = []
    def read_graph(self, file_path: str, delimiter: str = ',') -> Dict[str, Dict[str, int]]:
        with open(file_path, 'r') as file:
            for line in file:
                node1, node2, weight = [x.strip() for x in line.split(delimiter)]
                if node1 not in self.graph:
                    self.graph[node1] = {}
                self.graph[node1][node2] = int(weight)
        return self.graph
    def add_visited(self, vertex: str) -> bool:
        if vertex not in self.visited:
            self.visited.append(vertex)
            return True
        return False
    def get_min_edge(self) -> Tuple[str, str, int]:
        min_edge = (None, None, float('inf'))
        for v1 in self.visited:
            for v2, weight in self.graph[v1].items():
                if v2 not in self.visited and weight < min_edge[2]:
                    min_edge = (v1, v2, weight)
        return min_edge
    def execute(self) -> Tuple[List[Tuple[str, str, int, int]], int]:
        total_distance = 0
        start_vertex = next(iter(self.graph))
        self.add_visited(start_vertex)
        for _ in range(len(self.graph) - 1):
            v1, v2, edge_distance = self.get_min_edge()
            total_distance += edge_distance
            self.mst.append((v1, v2, edge_distance, total_distance))
            self.add_visited(v2)
        return self.mst, total_distance
