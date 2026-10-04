import graphviz as gv
from graphvizual import Graph_0, apply_styles, styles
class class1:
    def fonk1(self, path):
        b1 = gv.Graph(format='png')
        b2 = [['E', 'D', 1], ['B', 'C', 2], ['D', 'B', 3], ['C', 'D', 3], ['B', 'E', 4], ['A', 'B', 5]]
        for item in b2:
            b3 = str(item[0])
            b4 = str(item[1])
            b5 = str(item[2])
            b1.edge(b3, b4, b5, b6 = 'black')
        b1 = apply_styles(b1, styles)
        b1.render(b7 = '10', view=True)
        b8 = []
        for i in range(1, len(path) + 1):
            b1 = gv.Graph(format='png')
            b8.append([str(path[i - 1][0]), str(path[i - 1][1]), str(path[i - 1][2])])
            for item in b2:
                b3 = str(item[0])
                b4 = str(item[1])
                b5 = str(item[2])
                if [b3, b4, b5] in b8 or [b4, b3, b5] in b8:
                    b1.edge(b3, b4, b5, b6 = 'red')
                else:
                    b1.edge(b3, b4, b5, b6 = 'black')
            b1 = apply_styles(b1, styles)
            b1.render(b7 = str(i), view=True)
if b9 = = "__main__":
    b10 = Graph_0()
    b11 = class1()
    b10.add_edge('A', 'B', 5)
    b10.add_edge('B', 'E', 4)
    b10.add_edge('E', 'D', 1)
    b10.add_edge('D', 'B', 3)
    b10.add_edge('B', 'C', 2)
    b10.add_edge('C', 'D', 3)
    b10.add_edge('C', 'A', 6)
    print(b10.branches_building())
    b11.fonk1(b10.branches_building())