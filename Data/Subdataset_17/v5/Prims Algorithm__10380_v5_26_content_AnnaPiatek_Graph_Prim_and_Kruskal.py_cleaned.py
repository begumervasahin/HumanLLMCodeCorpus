import graphviz as gv
from graphvizual import Graph_0, apply_styles, styles
class Drawing:
    def __init__(self):
        self.edge_list = [['E', 'D', 1], ['B', 'C', 2], ['D', 'B', 3], ['C', 'D', 3], ['B', 'E', 4], ['A', 'B', 5]]
    def draw_initial_graph(self):
        drawing = gv.Graph(format='png')
        for edge in self.edge_list:
            node_start = str(edge[0])
            node_end = str(edge[1])
            weight = str(edge[2])
            drawing.edge(node_start, node_end, weight, color='black')
        drawing = apply_styles(drawing, styles)
        drawing.render(filename='10', view=True)
    def draw_path_graphs(self, path):
        path_edges = []
        for i in range(1, len(path) + 1):
            drawing = gv.Graph(format='png')
            path_edges.append([str(path[i - 1][0]), str(path[i - 1][1]), str(path[i - 1][2])])
            for edge in self.edge_list:
                node_start = str(edge[0])
                node_end = str(edge[1])
                weight = str(edge[2])
                if [node_start, node_end, weight] in path_edges or [node_end, node_start, weight] in path_edges:
                    drawing.edge(node_start, node_end, weight, color='red')
                else:
                    drawing.edge(node_start, node_end, weight, color='black')
            drawing = apply_styles(drawing, styles)
            drawing.render(filename=str(i), view=True)
    def draw(self, path):
        self.draw_initial_graph()
        self.draw_path_graphs(path)
if __name__ == "__main__":
    graph = Graph_0()
    drawing = Drawing()
    graph.add_edge('A', 'B', 5)
    graph.add_edge('B', 'E', 4)
    graph.add_edge('E', 'D', 1)
    graph.add_edge('D', 'B', 3)
    graph.add_edge('B', 'C', 2)
    graph.add_edge('C', 'D', 3)
    graph.add_edge('C', 'A', 6)
    branch_paths = graph.branches_building()
    print(branch_paths)
    drawing.draw(branch_paths)