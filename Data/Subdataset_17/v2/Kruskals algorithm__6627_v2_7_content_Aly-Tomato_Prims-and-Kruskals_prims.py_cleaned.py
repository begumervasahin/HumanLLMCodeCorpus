from typing import Dict, List, Tuple
class PrimAlgorithm:
    def __init__(self):
        self.graph: Dict[str, Dict[str, int]] = {}
        self.visited: List[str] = []
        self.mst: List[Tuple[str, str, int, int]] = []
    def read_graph(self, file: str, delimiter: str = ',') -> Dict[str, Dict[str, int]]:
        with open(file) as file_path:
            for line in file_path:
                nodes = [x.strip() for x in line.split(delimiter)]
                e1, e2, weight = nodes[0], nodes[1], int(nodes[2])
                if e1 not in self.graph:
                    self.graph[e1] = {}
                self.graph[e1][e2] = weight
                if e2 not in self.graph:
                    self.graph[e2] = {}
                self.graph[e2][e1] = weight
        return self.graph
    def add_visited(self, vertex: str) -> bool:
        if vertex in self.visited:
            return False
        self.visited.append(vertex)
        return True
    def get_min_edge(self) -> Tuple[str, str, int]:
        min_vertex1 = min_vertex2 = None
        min_distance = float('inf')
        for v1 in self.visited:
            for v2, weight in self.graph.get(v1, {}).items():
                if v2 in self.visited or v1 == v2:
                    continue
                if weight < min_distance:
                    min_vertex1, min_vertex2, min_distance = v1, v2, weight
        return min_vertex1, min_vertex2, min_distance
    def prims(self) -> Tuple[List[Tuple[str, str, int, int]], int]:
        total_distance = 0
        start_vertex = list(self.graph.keys())[0]
        self.add_visited(start_vertex)
        while len(self.visited) < len(self.graph):
            v1, v2, edge_distance = self.get_min_edge()
            if v1 and v2:
                total_distance += edge_distance
                self.mst.append((v1, v2, edge_distance, total_distance))
                self.add_visited(v2)
        return self.mst, total_distance
if __name__ == "__main__":
    graph_file = 'filename.txt'
    delimiter = ','
    prim = PrimAlgorithm()
    prim.read_graph(graph_file, delimiter)
    mst_result, total_cost = prim.prims()
    print("Minimum Spanning Tree:", mst_result)
    print("Total Cost:", total_cost)