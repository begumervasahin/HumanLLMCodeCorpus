import math
import string
import matplotlib.pyplot as plt
import numpy as np
class PlotGraph:
    def __init__(self, graphMat):
        if graphMat.shape[0] != graphMat.shape[1]:
            raise ValueError("Please provide a valid adjacency matrix (square matrix).")
        self.graphMat = graphMat
        self.numVertices = graphMat.shape[0]
        self.r = 1
    def get_vertex_coordinates(self):
        pi = math.pi
        vertex_coords = []
        theta = pi
        interval = 2 * pi / self.numVertices
        for _ in range(self.numVertices):
            x_coord = round(self.r * math.cos(theta), 2)
            y_coord = round(self.r * math.sin(theta), 2)
            vertex_coords.append((x_coord, y_coord))
            theta += interval
        return vertex_coords
    def get_edges(self):
        edge_list = []
        for i in range(self.numVertices):
            for j in range(self.numVertices):
                if self.graphMat[i, j]:
                    edge_list.append((i, j))
        return edge_list
    def get_offsetted_values(self, x_pos, y_pos, offset):
        if y_pos > 0:
            y_pos += offset
            if x_pos != 0:
                x_pos += offset if x_pos > 0 else -offset
        elif y_pos < 0:
            y_pos -= offset
            if x_pos != 0:
                x_pos += offset if x_pos > 0 else -offset
        elif y_pos == 0:
            x_pos += offset if x_pos != 0 else 0
        elif x_pos == 0:
            y_pos += offset if y_pos != 0 else 0
        return x_pos, y_pos
    def plot(self):
        vertex_coords = self.get_vertex_coordinates()
        print(vertex_coords)
        edge_list = self.get_edges()
        print("Found %d edges in the graph" % len(edge_list))
        for edge in edge_list:
            print(edge)
            x_pos = vertex_coords[edge[0]]
            y_pos = vertex_coords[edge[1]]
            plt.arrow(x_pos[0], x_pos[1], y_pos[0] - x_pos[0], y_pos[1] - x_pos[1],
                      head_length=0.2, head_width=0.1, fc='k', ec='k',
                      length_includes_head=True, overhang=0.2)
        alphabet = string.ascii_uppercase
        for v in range(self.numVertices):
            x_pos, y_pos = vertex_coords[v][0], vertex_coords[v][1]
            x_pos_label, y_pos_label = self.get_offsetted_values(x_pos, y_pos, 0.3)
            plt.text(x_pos_label, y_pos_label, alphabet[v], fontsize=20)
            x_pos_vertex, y_pos_vertex = self.get_offsetted_values(x_pos, y_pos, 0.07)
            plt.plot(x_pos_vertex, y_pos_vertex, 'wo', mew=2, ms=20)
        plt.axis([-2 * self.r, 2 * self.r, -2 * self.r, 2 * self.r])
        plt.title("Graph of %d vertices, %d edges" % (self.numVertices, len(edge_list)), loc='center')
        plt.show()
if __name__ == "__main__":
    graph_matrix = np.array([[0, 1, 1, 0],
                             [1, 0, 1, 1],
                             [1, 1, 0, 1],
                             [0, 1, 1, 0]])
    plotter = PlotGraph(graph_matrix)
    plotter.plot()