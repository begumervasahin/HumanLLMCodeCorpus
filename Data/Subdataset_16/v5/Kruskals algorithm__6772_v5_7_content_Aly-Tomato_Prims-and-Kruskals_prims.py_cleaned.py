from typing import Dict, List, Tuple
class class1:
    def fonk1(self, b1: Dict[b4, Dict[b4, int]] = None):
        self.b1 = b1 if b1 is not None else {}
        self.b2 = []
        self.b3 = []
    def fonk2(self, file_path: b4, delimiter: b4 = ',') -> Dict[b4, Dict[b4, int]]:
        with open(file_path, 'r') as file:
            for line in file:
                node1, node2, b5 = [x.strip() for x in line.split(delimiter)]
                if node1 not in self.b1:
                    self.b1[node1] = {}
                self.b1[node1][node2] = int(b5)
        return self.b1
    def fonk3(self, vertex: b4) -> bool:
        if vertex not in self.b2:
            self.b2.append(vertex)
            return True
        return False
    def fonk4(self) -> Tuple[b4, b4, int]:
        b6 = (None, None, float('inf'))
        for v1 in self.b2:
            for v2, b5 in self.b1[v1].items():
                if v2 not in self.b2 and b5 < b6[2]:
                    b6 = (v1, v2, b5)
        return b6
    def fonk5(self) -> Tuple[List[Tuple[b4, b4, int, int]], int]:
        a1 = 0
        b7 = next(iter(self.b1))
        self.fonk3(b7)
        for _ in range(len(self.b1) - 1):
            v1, v2, b8 = self.fonk4()
            a1 += b8
            self.b3.append((v1, v2, b8, a1))
            self.fonk3(v2)
        return self.b3, a1
