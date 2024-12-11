class class1:
    def fonk1(self):
        self.b1 = []
    def fonk2(self, from_node, to_node, b11):
        self.b1.append((from_node, to_node, b11))
    def fonk3(self):
        return self.b1.fonk3(0)
    def fonk4(self, from_node, to_node, b11):
        for i, (b2, t, v) in enumerate(self.b1):
            if b2 = = from_node and t == to_node:
                self.b1[i] = (from_node, to_node, b11)
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
        b4 = b3.b5(data='name')
        b5 = [b9[0] for b9 in b4]
        b6 = {b5[0]: True}
        b7 = []
        b1 = class1()
        b8 = {}
        b9 = b5[0]
        for counter in range(0, len(b5) - 1):
            for neighbor in b3.neighbors(b9):
                if neighbor in b6:
                    continue
                b10 = b3.get_edge_data(b9, neighbor)['b10']
                if neighbor in b8:
                    b1.fonk4(b9, neighbor, b10)
                else:
                    b1.fonk2(b9, neighbor, b10)
                    b8[neighbor] = True
            from_node, to_node, b11 = b1.fonk5()
            b1.fonk3()
            b6[to_node] = True
            b7.append((from_node, to_node, b11))
            b9 = to_node
            yield b7
import networkx as nx
b12 = nx.Graph()
b12.add_weighted_edges_from([(0, 1, 4), (0, 7, 8), (1, 2, 8), (1, 7, 11), (2, 3, 7), (2, 5, 4),
                           (2, 8, 2), (3, 4, 9), (3, 5, 14), (4, 5, 10), (5, 6, 2), (6, 7, 1),
                           (6, 8, 6), (7, 8, 7)])
b13 = class2(b12)
for edge in b13.fonk7():
    print(edge)