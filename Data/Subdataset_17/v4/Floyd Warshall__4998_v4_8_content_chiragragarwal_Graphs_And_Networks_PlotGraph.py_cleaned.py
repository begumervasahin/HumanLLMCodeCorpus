import math
import string
import numpy as np
import matplotlib.pyplot as plt
class PlotGraph:
    def __init__(self, graphMat):
        self.graphMat = graphMat
        if self.graphMat.shape[0] != self.graphMat.shape[1]:
            raise ValueError("The adjacency matrix must be square.")
        self.num_vertices = self.graphMat.shape[0]
        self.radius = 1
    def get_vertex_coordinates(self):
        vertex_coords = []
        angle_step = 2 * math.pi / self.num_vertices
        angle = math.pi
        for _ in range(self.num_vertices):
            x = round(self.radius * math.cos(angle), 2)
            y = round(self.radius * math.sin(angle), 2)
            vertex_coords.append((x, y))
            angle += angle_step
        return vertex_coords
    def get_edges(self):
        edges = []
        for i in range(self.num_vertices):
            for j in range(self.num_vertices):
                if self.graphMat[i, j]:
                    edges.append((i, j))
        return edges
    def adjust_coordinates(self, x, y, offset):
        if y > 0:
            y += offset
            x += offset if x > 0 else x - offset
        elif y < 0:
            y -= offset
            x += offset if x > 0 else x - offset
        else:
            x += offset if x > 0 else x - offset
        if x == 0:
            y += offset if y > 0 else y - offset
        return x, y
    def plot(self):
        vertex_coords = self.get_vertex_coordinates()
        edges = self.get_edges()
        print("Vertex coordinates:", vertex_coords)
        print(f"Found {len(edges)} edges in the graph.")
        for edge in edges:
            x_start, y_start = vertex_coords[edge[0]]
            x_end, y_end = vertex_coords[edge[1]]
            plt.arrow(
                x_start, y_start,
                x_end - x_start, y_end - y_start,
                head_length=0.2, head_width=0.1, fc='k', ec='k',
                length_includes_head=True, overhang=0.2
            )
        alphabet = string.ascii_uppercase
        for v in range(self.num_vertices):
            x, y = vertex_coords[v]
            x_label, y_label = self.adjust_coordinates(x, y, 0.3)
            plt.text(x_label, y_label, alphabet[v], fontsize=20)
            x_vertex, y_vertex = self.adjust_coordinates(x, y, 0.07)
            plt.plot(x_vertex, y_vertex, 'wo', mew=2, ms=20)
        plt.axis([-2 * self.radius, 2 * self.radius, -2 * self.radius, 2 * self.radius])
        plt.title(f"Graph with {self.num_vertices} vertices and {len(edges)} edges", loc='center')
        plt.show()
if __name__ == '__main__':
    example_matrix = np.matrix([
        [0, 1, 0],
        [1, 0, 1],
        [0, 1, 0]
    ])
    graph_plotter = PlotGraph(example_matrix)
    graph_plotter.plot()