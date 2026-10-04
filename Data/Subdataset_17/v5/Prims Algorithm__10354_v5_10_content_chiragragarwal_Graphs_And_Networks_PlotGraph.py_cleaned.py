import math
import string
import numpy as np
from matplotlib import pyplot as plt
class PlotGraph:
    '''
    Plot a graph using the graphMat matrix provided.
    graphMat: matrix of type numpy.matrix
    '''
    def __init__(self, graphMat):
        self.graphMat = graphMat
        if self.graphMat.shape[0] != self.graphMat.shape[1]:
            raise ValueError("Please enter a valid adjacency matrix!")
        self.numVertices = self.graphMat.shape[0]
        self.r = 1
    def get_vertex_coordinates(self):
        '''
        Return the Cartesian coordinates of the graph based on the number of vertices
        and radius of the circle containing the points
        '''
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
        '''
        Return a list of edges denoted by vertex numbers and not actual position.
        Ex: (0, 1) means Vertex 0 and Vertex 1
        '''
        edge_list = []
        for i in range(self.numVertices):
            for j in range(self.numVertices):
                if self.graphMat[i, j]:
                    edge_list.append((i, j))
        return edge_list
    def get_offsetted_values(self, x_pos, y_pos, offset):
        '''
        Return modified x_pos and y_pos values with the offset depending on the quadrant
        '''
        if y_pos > 0:
            y_pos += offset
            x_pos += offset if x_pos > 0 else -offset
        elif y_pos < 0:
            y_pos -= offset
            x_pos += offset if x_pos > 0 else -offset
        elif y_pos == 0:
            x_pos += offset if x_pos > 0 else -offset
        elif x_pos == 0:
            y_pos += offset if y_pos > 0 else -offset
        return x_pos, y_pos
    def plot(self):
        '''
        Plot the graph/network
        '''
        vertex_coords = self.get_vertex_coordinates()
        print(vertex_coords)
        edge_list = self.get_edges()
        print(f"Found {len(edge_list)} edges in the graph")
        for edge in edge_list:
            print(edge)
            x_start, y_start = vertex_coords[edge[0]]
            x_end, y_end = vertex_coords[edge[1]]
            plt.arrow(x_start, y_start,
                      x_end - x_start, y_end - y_start,
                      head_length=0.2, head_width=0.1, fc='k', ec='k',
                      length_includes_head=True, overhang=0.2)
        alphabet = string.ascii_uppercase
        for v in range(self.numVertices):
            x_pos, y_pos = vertex_coords[v]
            x_pos_label, y_pos_label = self.get_offsetted_values(x_pos, y_pos, 0.3)
            plt.text(x_pos_label, y_pos_label, alphabet[v], fontsize=20)
            x_pos_vertex, y_pos_vertex = self.get_offsetted_values(x_pos, y_pos, 0.07)
            plt.plot(x_pos_vertex, y_pos_vertex, 'wo', mew=2, ms=20)
        plt.axis([-2 * self.r, 2 * self.r, -2 * self.r, 2 * self.r])
        plt.title(f"Graph of {self.numVertices} vertices, {len(edge_list)} edges", loc='center')
        plt.show()
if __name__ == "__main__":
    graph_mat = np.matrix([
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1],
        [1, 0, 0, 0]
    ])
    plot_graph = PlotGraph(graph_mat)
    plot_graph.plot()