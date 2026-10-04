import graphviz as gv
from graphviz import Graph
styles = {
    'graph': {
        'label': 'Graph',
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
    'edges': {
        'color': 'black',
        'fontcolor': 'black',
        'fontsize': '12',
    }
}
def apply_styles(graph, styles):
    graph.graph_attr.update(styles.get('graph', {}))
    graph.node_attr.update(styles.get('nodes', {}))
    graph.edge_attr.update(styles.get('edges', {}))
    return graph
class Graph_0:
    def __init__(self):
        self.edges = []
    def add_edge(self, node1, node2, weight):
        self.edges.append((node1, node2, weight))
    def branches_building(self):
        return sorted(self.edges, key=lambda x: x[2])
class Drawing:
    def drawing(self, path):
        list_e = [['E', 'D', 1], ['B', 'C', 2], ['D', 'B', 3], ['C', 'D', 3], ['B', 'E', 4], ['A', 'B', 5]]
        initial_drawing = Graph(format='png')
        for item in list_e:
            initial_drawing.edge(str(item[0]), str(item[1]), label=str(item[2]), color='black')
        initial_drawing = apply_styles(initial_drawing, styles)
        initial_drawing.render(filename='graph_initial', view=True)
        path_edges = []
        for i in range(1, len(path) + 1):
            step_drawing = Graph(format='png')
            path_edges.append([str(path[i - 1][0]), str(path[i - 1][1]), str(path[i - 1][2])])
            for item in list_e:
                node_00, node_11, wei = str(item[0]), str(item[1]), str(item[2])
                if [node_00, node_11, wei] in path_edges or [node_11, node_00, wei] in path_edges:
                    step_drawing.edge(node_00, node_11, label=wei, color='red')
                else:
                    step_drawing.edge(node_00, node_11, label=wei, color='black')
            step_drawing = apply_styles(step_drawing, styles)
            step_drawing.render(filename=f'graph_{i}', view=True)
if __name__ == "__main__":
    g = Graph_0()
    g.add_edge('A', 'B', 5)
    g.add_edge('B', 'E', 4)
    g.add_edge('E', 'D', 1)
    g.add_edge('D', 'B', 3)
    g.add_edge('B', 'C', 2)
    g.add_edge('C', 'D', 3)
    g.add_edge('C', 'A', 6)
    mst = g.branches_building()
    print(mst)
    d = Drawing()
    d.drawing(mst)