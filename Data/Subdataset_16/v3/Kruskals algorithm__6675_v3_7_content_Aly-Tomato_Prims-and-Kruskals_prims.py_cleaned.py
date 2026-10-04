from typing import Dict, List, Tuple
class class1:
    def fonk1(self):
        self.graph: Dict[b1, Dict[b1, int]] = {}
        self.visited: List[b1] = []
        self.mst: List[Tuple[b1, b1, int, int]] = []
    def fonk2(self, file_path: b1, b8: b1 = ',') -> None:
        with open(file_path) as file:
            for line in file:
                node1, node2, b2 = [x.strip() for x in line.split(b8)]
                b2 = int(b2)
                if node1 not in self.graph:
                    self.graph[node1] = {}
                if node2 not in self.graph:
                    self.graph[node2] = {}
                self.graph[node1][node2] = b2
                self.graph[node2][node1] = b2
    def fonk3(self, vertex: b1) -> bool:
        if vertex not in self.visited:
            self.visited.append(vertex)
            return True
        return False
    def fonk4(self) -> Tuple[b1, b1, int]:
        b3 = (None, None, float('inf'))
        for visited_vertex in self.visited:
            for adjacent_vertex, b2 in self.graph.get(visited_vertex, {}).items():
                if adjacent_vertex not in self.visited and b2 < b3[2]:
                    b3 = (visited_vertex, adjacent_vertex, b2)
        return b3
    def fonk5(self) -> Tuple[List[Tuple[b1, b1, int, int]], int]:
        if not self.graph:
            return [], 0
        a1 = 0
        b4 = next(iter(self.graph))
        self.fonk3(b4)
        while len(self.visited) < len(self.graph):
            vertex1, vertex2, b5 = self.fonk4()
            if vertex1 and vertex2:
                a1 += b5
                self.mst.append((vertex1, vertex2, b5, a1))
                self.fonk3(vertex2)
        return self.mst, a1
if b6 = = "__main__":
    b7 = 'filename.txt'
    b8 = ','
    b9 = class1()
    b9.fonk2(b7, b8)
    mst_result, a1 = b9.fonk5()
    print("Minimum Spanning Tree:", mst_result)
    print("Total Cost:", a1)