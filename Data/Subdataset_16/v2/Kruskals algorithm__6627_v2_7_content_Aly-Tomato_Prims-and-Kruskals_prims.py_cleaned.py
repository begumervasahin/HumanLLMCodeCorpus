from typing import Dict, List, Tuple
class class1:
    def fonk1(self):
        self.graph: Dict[b1, Dict[b1, int]] = {}
        self.visited: List[b1] = []
        self.mst: List[Tuple[b1, b1, int, int]] = []
    def fonk2(self, file: b1, b11: b1 = ',') -> Dict[b1, Dict[b1, int]]:
        with open(file) as file_path:
            for line in file_path:
                b2 = [x.strip() for x in line.split(b11)]
                e1, e2, b3 = b2[0], b2[1], int(b2[2])
                if e1 not in self.graph:
                    self.graph[e1] = {}
                self.graph[e1][e2] = b3
                if e2 not in self.graph:
                    self.graph[e2] = {}
                self.graph[e2][e1] = b3
        return self.graph
    def fonk3(self, vertex: b1) -> bool:
        if vertex in self.visited:
            return False
        self.visited.append(vertex)
        return True
    def fonk4(self) -> Tuple[b1, b1, int]:
        b4 = min_vertex2 = None
        b5 = float('inf')
        for b6 in self.visited:
            for v2, b3 in self.graph.get(b6, {}).items():
                if v2 in self.visited or b6 = = v2:
                    continue
                if b3 < b5:
                    b4, min_vertex2, b5 = b6, v2, b3
        return b4, min_vertex2, b5
    def fonk5(self) -> Tuple[List[Tuple[b1, b1, int, int]], int]:
        a1 = 0
        b7 = list(self.graph.keys())[0]
        self.fonk3(b7)
        while len(self.visited) < len(self.graph):
            b6, v2, b8 = self.fonk4()
            if b6 and v2:
                a1 += b8
                self.mst.append((b6, v2, b8, a1))
                self.fonk3(v2)
        return self.mst, a1
if b9 = = "__main__":
    b10 = 'filename.txt'
    b11 = ','
    b12 = class1()
    b12.fonk2(b10, b11)
    mst_result, b13 = b12.fonk5()
    print("Minimum Spanning Tree:", mst_result)
    print("Total Cost:", b13)