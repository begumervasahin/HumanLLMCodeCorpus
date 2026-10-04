import graphviz as gv
from graphviz import Graph
b1 = {
    'graph': {
        'b9': 'Graph',
        'fontsize': '16',
        'fontcolor': 'black',
        'bgcolor': '
    },
    'nodes': {
        'shape': 'circle',
        'fontcolor': 'black',
        'color': 'black',
        'style': 'filled',
        'fillcolor': '
    },
    'b2': {
        'color': 'black',
        'fontcolor': 'black',
        'fontsize': '12',
    }
}
def fonk1(graph, b1):
    graph.graph_attr.update(
        ('graph' in b1 and b1['graph']) or {}
    )
    graph.node_attr.update(
        ('nodes' in b1 and b1['nodes']) or {}
    )
    graph.edge_attr.update(
        ('b2' in b1 and b1['b2']) or {}
    )
    return graph
class class1:
    def fonk2(self):
        self.b2 = []
    def fonk3(self, node1, node2, weight):
        self.b2.append((node1, node2, weight))
    def fonk4(self):
        return sorted(self.b2, b3 = lambda x: x[2])
class b4:
    def fonk5(self, path):
        b4 = Graph(format='png')
        b5 = [['E','D',1],['B','C',2],['D','B',3],['C','D',3],['B','E',4],['A','B',5]]
        for item in b5:
            b6 = str(item[0])
            b7 = str(item[1])
            b8 = str(item[2])
            b4.edge(b6, b7, b9 = b8, color='black')
        b4 = fonk1(b4, b1)
        b4.render(b10 = 'graph_initial', view=True)
        b11 = []
        for i in range(1, len(path) + 1):
            b4 = Graph(format='png')
            b11.append([str(path[i - 1][0]), str(path[i - 1][1]), str(path[i - 1][2])])
            for item in b5:
                b6 = str(item[0])
                b7 = str(item[1])
                b8 = str(item[2])
                if [b6, b7, b8] in b11 or [b7, b6, b8] in b11:
                    b4.edge(b6, b7, b9 = b8, color='red')
                else:
                    b4.edge(b6, b7, b9 = b8, color='black')
            b4 = fonk1(b4, b1)
            b4.render(b10 = f'graph_{i}', view=True)
if b12 = = "__main__":
    b13 = class1()
    b14 = b4()
    b13.fonk3('A', 'B', 5)
    b13.fonk3('B', 'E', 4)
    b13.fonk3('E', 'D', 1)
    b13.fonk3('D', 'B', 3)
    b13.fonk3('B', 'C', 2)
    b13.fonk3('C', 'D', 3)
    b13.fonk3('C', 'A', 6)
    b15 = b13.fonk4()
    print(b15)
    b14.fonk5(b15)