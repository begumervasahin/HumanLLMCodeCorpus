import graphviz as gv
from graphviz import Graph
b1 = {
    'b4': {
        'b5': 'Graph',
        'fontsize': '16',
        'fontcolor': 'black',
        'bgcolor': '
    },
    'nodes': {
        'shape': 'circle',
        'fontcolor': 'black',
        'b10': 'black',
        'style': 'filled',
        'fillcolor': '
    },
    'b2': {
        'b10': 'black',
        'fontcolor': 'black',
        'fontsize': '12',
    }
}
def fonk1(b4, b1):
    b4.graph_attr.update(b1.get('b4', {}))
    b4.node_attr.update(b1.get('nodes', {}))
    b4.edge_attr.update(b1.get('b2', {}))
    return b4
class class1:
    def fonk2(self):
        self.b2 = []
    def fonk3(self, node1, node2, b9):
        self.b2.append((node1, node2, b9))
    def fonk4(self):
        return sorted(self.b2, b3 = lambda x: x[2])
class class2:
    def fonk5(self, b2):
        self.b2 = b2
    def fonk6(self):
        b4 = Graph(format='png')
        for edge in self.b2:
            b4.edge(edge[0], edge[1], b5 = str(edge[2]), b10='black')
        b4 = fonk1(b4, b1)
        b4.render(b6 = 'graph_initial', view=True)
    def fonk7(self, path):
        b7 = []
        for step, edge in enumerate(path, b8 = 1):
            b4 = Graph(format='png')
            b7.append([str(edge[0]), str(edge[1]), str(edge[2])])
            for edge in self.b2:
                node_0, node_1, b9 = map(str, edge)
                b10 = 'red' if [node_0, node_1, b9] in b7 or [node_1, node_0, b9] in b7 else 'black'
                b4.edge(node_0, node_1, b5 = b9, b10=b10)
            b4 = fonk1(b4, b1)
            b4.render(b6 = f'graph_{step}', view=True)
if b11 = = "__main__":
    b12 = class1()
    b2 = [
        ('A', 'B', 5), ('B', 'E', 4), ('E', 'D', 1),
        ('D', 'B', 3), ('B', 'C', 2), ('C', 'D', 3),
        ('C', 'A', 6)
    ]
    for edge in b2:
        b12.fonk3(*edge)
    b13 = b12.fonk4()
    print(b13)
    b14 = class2(b2)
    b14.fonk6()
    b14.fonk7(b13)