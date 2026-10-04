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
    def __init__(self, edges):
        self.edges = edges
    def draw_initial_graph(self):
        graph = Graph(format='png')
        for edge in self.edges:
            graph.edge(edge[0], edge[1], label=str(edge[2]), color='black')
        graph = apply_styles(graph, styles)
        graph.render(filename='graph_initial', view=True)
    def draw_highlighted_paths(self, path):
        path_edges = []
        for step, edge in enumerate(path, start=1):
            graph = Graph(format='png')
            path_edges.append([str(edge[0]), str(edge[1]), str(edge[2])])
            for edge in self.edges:
                node_0, node_1, weight = map(str, edge)
                color = 'red' if [node_0, node_1, weight] in path_edges or [node_1, node_0, weight] in path_edges else 'black'
                graph.edge(node_0, node_1, label=weight, color=color)
            graph = apply_styles(graph, styles)
            graph.render(filename=f'graph_{step}', view=True)
if __name__ == "__main__":
    g = Graph_0()
    edges = [
        ('A', 'B', 5), ('B', 'E', 4), ('E', 'D', 1),
        ('D', 'B', 3), ('B', 'C', 2), ('C', 'D', 3),
        ('C', 'A', 6)
    ]
    for edge in edges:
        g.add_edge(*edge)
    mst = g.branches_building()
    print(mst)
    d = Drawing(edges)
    d.draw_initial_graph()
    d.draw_highlighted_paths(mst)