import graphviz as gv
from graphvizual import Graph_0, apply_styles, styles
class class1:
    def fonk1(self):
        self.b1 = [['E', 'D', 1], ['B', 'C', 2], ['D', 'B', 3], ['C', 'D', 3], ['B', 'E', 4], ['A', 'B', 5]]
    def fonk2(self):
        b2 = gv.Graph(format='png')
        for edge in self.b1:
            b3 = str(edge[0])
            b4 = str(edge[1])
            b5 = str(edge[2])
            b2.edge(b3, b4, b5, b6 = 'black')
        b2 = apply_styles(b2, styles)
        b2.render(b7 = '10', view=True)
    def fonk3(self, path):
        b8 = []
        for i in range(1, len(path) + 1):
            b2 = gv.Graph(format='png')
            b8.append([str(path[i - 1][0]), str(path[i - 1][1]), str(path[i - 1][2])])
            for edge in self.b1:
                b3 = str(edge[0])
                b4 = str(edge[1])
                b5 = str(edge[2])
                if [b3, b4, b5] in b8 or [b4, b3, b5] in b8:
                    b2.edge(b3, b4, b5, b6 = 'red')
                else:
                    b2.edge(b3, b4, b5, b6 = 'black')
            b2 = apply_styles(b2, styles)
            b2.render(b7 = str(i), view=True)
    def fonk4(self, path):
        self.fonk2()
        self.fonk3(path)
if b9 = = "__main__":
    b10 = Graph_0()
    b2 = class1()
    b10.add_edge('A', 'B', 5)
    b10.add_edge('B', 'E', 4)
    b10.add_edge('E', 'D', 1)
    b10.add_edge('D', 'B', 3)
    b10.add_edge('B', 'C', 2)
    b10.add_edge('C', 'D', 3)
    b10.add_edge('C', 'A', 6)
    b11 = b10.branches_building()
    print(b11)
    b2.fonk4(b11)