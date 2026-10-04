import math
import string
import numpy as np
from matplotlib import pyplot as plt
class PlotGraph:
    def __init__(self, graphMat):
        self.graphMat = graphMat
        if self.graphMat.shape[0] != self.graphMat.shape[1]:
            raise ValueError("Please enter a valid square adjacency matrix!")
        self.numVertices = self.graphMat.shape[0]
        self.r = 1
    def get_vertex_coordinates(self):
        pi = math.pi
        theta = pi
        interval = 2 * pi / self.numVertices
        vertex_coords = []
        for _ in range(self.numVertices):
            x = round(self.r * math.cos(theta), 2)
            y = round(self.r * math.sin(theta), 2)
            vertex_coords.append((x, y))
            theta += interval
        return vertex_coords
    def get_edges(self):
        edge_list = []
        for i in range(self.numVertices):
            for j in range(self.numVertices):
                if self.graphMat[i, j]:
                    edge_list.append((i, j))
        return edge_list
    def get_offsetted_values(self, x, y, offset):
        if y > 0:
            y += offset
            x += offset if x > 0 else -offset
        elif y < 0:
            y -= offset
            x += offset if x > 0 else -offset
        elif y == 0:
            x += offset if x > 0 else -offset
        elif x == 0:
            y += offset if y > 0 else -offset
        return x, y
    def plot(self):
        vertex_coords = self.get_vertex_coordinates()
        edge_list = self.get_edges()
        print(vertex_coords)
        print(f"Found {len(edge_list)} edges in the graph")
        for edge in edge_list:
            print(edge)
            start = vertex_coords[edge[0]]
            end = vertex_coords[edge[1]]
            plt.arrow(start[0], start[1], end[0] - start[0], end[1] - start[1],
                      head_length=0.2, head_width=0.1, fc='k', ec='k',
                      length_includes_head=True, overhang=0.2)
        for i in range(self.numVertices):
            x, y = vertex_coords[i]
            label_x, label_y = self.get_offsetted_values(x, y, 0.3)
            plt.text(label_x, label_y, string.ascii_uppercase[i], fontsize=20)
            vertex_x, vertex_y = self.get_offsetted_values(x, y, 0.07)
            plt.plot(vertex_x, vertex_y, 'wo', mew=2, ms=20)
        plt.axis([-2 * self.r, 2 * self.r, -2 * self.r, 2 * self.r])
        plt.title(f"Graph of {self.numVertices} vertices, {len(edge_list)} edges", loc='center')
        plt.show()
if __name__ == "__main__":
    graphMat = np.matrix([[0, 1, 0, 1],
                          [1, 0, 1, 0],
                          [0, 1, 0, 1],
                          [1, 0, 1, 0]])
    plotGraph = PlotGraph(graphMat)
    plotGraph.plot()