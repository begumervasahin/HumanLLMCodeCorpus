import graphviz as gv
from graphviz import Graph
b1 = {
    'graph': {
        'b6': 'Graph',
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
    graph.graph_attr.update(b1.get('graph', {}))
    graph.node_attr.update(b1.get('nodes', {}))
    graph.edge_attr.update(b1.get('b2', {}))
    return graph
class class1:
    def fonk2(self):
        self.b2 = []
    def fonk3(self, node1, node2, weight):
        self.b2.append((node1, node2, weight))
    def fonk4(self):
        return sorted(self.b2, b3 = lambda x: x[2])
class class2:
    def fonk5(self, path):
        b4 = [['E', 'D', 1], ['B', 'C', 2], ['D', 'B', 3], ['C', 'D', 3], ['B', 'E', 4], ['A', 'B', 5]]
        b5 = Graph(format='png')
        for item in b4:
            b5.edge(str(item[0]), str(item[1]), b6 = str(item[2]), color='black')
        b5 = fonk1(b5, b1)
        b5.render(b7 = 'graph_initial', view=True)
        b8 = []
        for i in range(1, len(path) + 1):
            b9 = Graph(format='png')
            b8.append([str(path[i - 1][0]), str(path[i - 1][1]), str(path[i - 1][2])])
            for item in b4:
                node_00, node_11, b10 = str(item[0]), str(item[1]), str(item[2])
                if [node_00, node_11, b10] in b8 or [node_11, node_00, b10] in b8:
                    b9.edge(node_00, node_11, b6 = b10, color='red')
                else:
                    b9.edge(node_00, node_11, b6 = b10, color='black')
            b9 = fonk1(b9, b1)
            b9.render(b7 = f'graph_{i}', view=True)
if b11 = = "__main__":
    b12 = class1()
    b12.fonk3('A', 'B', 5)
    b12.fonk3('B', 'E', 4)
    b12.fonk3('E', 'D', 1)
    b12.fonk3('D', 'B', 3)
    b12.fonk3('B', 'C', 2)
    b12.fonk3('C', 'D', 3)
    b12.fonk3('C', 'A', 6)
    b13 = b12.fonk4()
    print(b13)
    b14 = class2()
    b14.fonk5(b13)