import math
from DataGenerator import Adjacency_List, Edge, DataGenerator
class class1:
    def fonk1(self, num_vertices):
        self.b1 = [class2(b10) for b10 in range(num_vertices)]
    def fonk2(self, b10):
        b2 = []
        b3 = self.b1[b10].fonk5(b2)
        for node in b2:
            node.b4 = b3
        return b3
    def fonk3(self, root_x, root_y, edge, b12):
        b12.add_edge(edge)
        if root_x.b6 <= root_y.b6:
            root_y.fonk6(root_x)
            root_y.b6 += 1
        else:
            root_x.fonk6(root_y)
            root_x.b6 += 1
class class2:
    def fonk4(self, b5, b4 = None):
        self.b5 = b5
        self.b4 = b4
        self.b6 = 1 if b4 is None else b4.b6 + 1
    def fonk5(self, b2):
        if self.b4 is None:
            return self
        b2.append(self)
        return self.b4.fonk5(b2)
    def fonk6(self, b4):
        self.b4 = b4
def fonk7(b14, low, high):
    if low < high:
        b7 = (low + high)
        fonk7(b14, low, b7)
        fonk7(b14, b7 + 1, high)
        fonk8(b14, low, b7, high)
def fonk8(b14, low, b7, high):
    b8 = b14[low:b7 + 1]
    b9 = b14[b7 + 1:high + 1]
    b10 = j = 0
    b11 = low
    while b10 < len(b8) and j < len(b9):
        if b8[b10].weight <= b9[j].weight:
            b14[b11] = b8[b10]
            b10 += 1
        else:
            b14[b11] = b9[j]
            j += 1
        b11 += 1
    while b10 < len(b8):
        b14[b11] = b8[b10]
        b10 += 1
        b11 += 1
    while j < len(b9):
        b14[b11] = b9[j]
        j += 1
        b11 += 1
def fonk9(adj):
    b12 = Adjacency_List(adj.get_vertices(), [])
    b13 = class1(adj.get_number_of_vertices())
    b14 = adj.get_edges()
    fonk7(b14, 0, len(b14) - 1)
    for edge in b14:
        b15 = b13.fonk2(edge.u)
        b16 = b13.fonk2(edge.v)
        if b15.b5 != b16.b5:
            b13.fonk3(b15, b16, edge, b12)
    return b12
if b17 = = '__main__':
    print("Original Adjacency List")
    b18 = DataGenerator(100, 0.1, method=2)
    b19 = b18.generate_data()
    b19.print_me()
    b12 = fonk9(b19)
    print("MST: Kruskal Algorithm")
    b12.print_me()