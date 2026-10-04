import graphviz as gv
from graphvizual import Graph_0, apply_styles, styles
class Drawing:
    def drawing(self, path):
        drawing = gv.Graph(format='png')
        list_e = [['E', 'D', 1], ['B', 'C', 2], ['D', 'B', 3], ['C', 'D', 3], ['B', 'E', 4], ['A', 'B', 5]]
        for item in list_e:
            node_00 = str(item[0])
            node_11 = str(item[1])
            wei = str(item[2])
            drawing.edge(node_00, node_11, wei, color='black')
        drawing = apply_styles(drawing, styles)
        drawing.render(filename='10', view=True)
        path_list = []
        for i in range(1, len(path) + 1):
            drawing = gv.Graph(format='png')
            path_list.append([str(path[i - 1][0]), str(path[i - 1][1]), str(path[i - 1][2])])
            for item in list_e:
                node_00 = str(item[0])
                node_11 = str(item[1])
                wei = str(item[2])
                if [node_00, node_11, wei] in path_list or [node_11, node_00, wei] in path_list:
                    drawing.edge(node_00, node_11, wei, color='red')
                else:
                    drawing.edge(node_00, node_11, wei, color='black')
            drawing = apply_styles(drawing, styles)
            drawing.render(filename=str(i), view=True)
if __name__ == "__main__":
    g = Graph_0()
    d = Drawing()
    g.add_edge('A', 'B', 5)
    g.add_edge('B', 'E', 4)
    g.add_edge('E', 'D', 1)
    g.add_edge('D', 'B', 3)
    g.add_edge('B', 'C', 2)
    g.add_edge('C', 'D', 3)
    g.add_edge('C', 'A', 6)
    print(g.branches_building())
    d.drawing(g.branches_building())