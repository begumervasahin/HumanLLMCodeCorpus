from typing import Dict, List, Tuple
class PrimAlgorithm:
    def __init__(self):
        self.graph: Dict[str, Dict[str, int]] = {}
        self.visited: List[str] = []
        self.mst: List[Tuple[str, str, int, int]] = []
    def read_graph(self, file_path: str, delimiter: str = ',') -> None:
        with open(file_path) as file:
            for line in file:
                node1, node2, weight = [x.strip() for x in line.split(delimiter)]
                weight = int(weight)
                if node1 not in self.graph:
                    self.graph[node1] = {}
                if node2 not in self.graph:
                    self.graph[node2] = {}
                self.graph[node1][node2] = weight
                self.graph[node2][node1] = weight
    def add_visited(self, vertex: str) -> bool:
        if vertex not in self.visited:
            self.visited.append(vertex)
            return True
        return False
    def get_min_edge(self) -> Tuple[str, str, int]:
        min_edge = (None, None, float('inf'))
        for visited_vertex in self.visited:
            for adjacent_vertex, weight in self.graph.get(visited_vertex, {}).items():
                if adjacent_vertex not in self.visited and weight < min_edge[2]:
                    min_edge = (visited_vertex, adjacent_vertex, weight)
        return min_edge
    def execute(self) -> Tuple[List[Tuple[str, str, int, int]], int]:
        if not self.graph:
            return [], 0
        total_cost = 0
        start_vertex = next(iter(self.graph))
        self.add_visited(start_vertex)
        while len(self.visited) < len(self.graph):
            vertex1, vertex2, edge_weight = self.get_min_edge()
            if vertex1 and vertex2:
                total_cost += edge_weight
                self.mst.append((vertex1, vertex2, edge_weight, total_cost))
                self.add_visited(vertex2)
        return self.mst, total_cost
if __name__ == "__main__":
    graph_file = 'filename.txt'
    delimiter = ','
    prim = PrimAlgorithm()
    prim.read_graph(graph_file, delimiter)
    mst_result, total_cost = prim.execute()
    print("Minimum Spanning Tree:", mst_result)
    print("Total Cost:", total_cost)