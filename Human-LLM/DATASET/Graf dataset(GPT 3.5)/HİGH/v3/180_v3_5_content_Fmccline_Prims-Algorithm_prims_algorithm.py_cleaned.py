class class1:
    def fonk1(self):
        self.b1 = []
    def fonk2(self, from_node, to_node, b10):
        self.b1.append((from_node, to_node, b10))
    def fonk3(self):
        return self.b1.fonk3(0)
    def fonk4(self, from_node, to_node, b10):
        for i, (b2, t, v) in enumerate(self.b1):
            if b2 = = from_node and t == to_node:
                self.b1[i] = (from_node, to_node, b10)
                break
    def fonk5(self):
        return self.b1[0]
class class2:
    a1 = 0
    a2 = 1
    a3 = 2
    def fonk6(self, b3):
        self.b3 = b3
    def fonk7(self):
        b3 = self.b3
        b4 = list(b3.b4)
        b5 = {b4[0]: True}
        b6 = []
        b1 = class1()
        b7 = {}
        b8 = b4[0]
        for _ in range(len(b4) - 1):
            for neighbor in b3.neighbors(b8):
                if neighbor in b5:
                    continue
                b9 = b3[b8][neighbor]['b9']
                if neighbor in b7:
                    b1.fonk4(b8, neighbor, b9)
                else:
                    b1.fonk2(b8, neighbor, b9)
                    b7[neighbor] = True
            from_node, to_node, b10 = b1.fonk5()
            b1.fonk3()
            b5[to_node] = True
            b6.append((from_node, to_node, b10))
            b8 = to_node
            yield b6
import networkx as nx
b11 = nx.Graph()
b11.add_weighted_edges_from([(0, 1, 4), (0, 7, 8), (1, 2, 8), (1, 7, 11), (2, 3, 7), (2, 5, 4),
                           (2, 8, 2), (3, 4, 9), (3, 5, 14), (4, 5, 10), (5, 6, 2), (6, 7, 1),
                           (6, 8, 6), (7, 8, 7)])
b12 = class2(b11)
for edge in b12.fonk7():
    print(edge)