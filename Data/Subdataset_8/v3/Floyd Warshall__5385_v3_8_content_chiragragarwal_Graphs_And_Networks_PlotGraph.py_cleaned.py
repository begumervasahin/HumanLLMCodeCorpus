import math
import string
import numpy as np
import matplotlib.pyplot as plt
class PlotGraph:
    '''
    Plot a graph using the adjacency matrix provided.
    Attributes:
        graph_mat (numpy.ndarray): The adjacency matrix representing the graph.
        num_vertices (int): The number of vertices in the graph.
        radius (int): The radius of the circle containing the vertices.
    '''
    def __init__(self, graph_mat):
        if graph_mat.shape[0] != graph_mat.shape[1]:
            raise ValueError("Please provide a valid adjacency matrix (square matrix).")
        self.graph_mat = graph_mat
        self.num_vertices = graph_mat.shape[0]
        self.radius = 1
    def get_vertex_coordinates(self):
        '''
        Calculate the Cartesian coordinates of the vertices based on the number of vertices
        and radius of the circle containing the points.
        Returns:
            list: A list of tuples containing (x, y) coordinates for each vertex.
        '''
        pi = math.pi
        vertex_coords = []
        theta = pi
        interval = 2 * pi / self.num_vertices
        for _ in range(self.num_vertices):
            x_coord = round(self.radius * math.cos(theta), 2)
            y_coord = round(self.radius * math.sin(theta), 2)
            vertex_coords.append((x_coord, y_coord))
            theta += interval
        return vertex_coords
    def get_edges(self):
        '''
        Retrieve the edges present in the graph.
        Returns:
            list: A list of tuples representing the edges in the graph.
        '''
        edge_list = []
        for i in range(self.num_vertices):
            for j in range(self.num_vertices):
                if self.graph_mat[i, j]:
                    edge_list.append((i, j))
        return edge_list
    def get_offsetted_values(self, x_pos, y_pos, offset):
        '''
        Calculate modified x_pos and y_pos values with the offset depending on the quadrant.
        Args:
            x_pos (float): The x-coordinate.
            y_pos (float): The y-coordinate.
            offset (float): The offset value.
        Returns:
            tuple: The modified (x_pos, y_pos) coordinates.
        '''
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
        '''
        Plot the graph.
        '''
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
        for v in range(self.num_vertices):
            x_pos, y_pos = vertex_coords[v][0], vertex_coords[v][1]
            x_pos_label, y_pos_label = self.get_offsetted_values(x_pos, y_pos, 0.3)
            plt.text(x_pos_label, y_pos_label, alphabet[v], fontsize=20)
            x_pos_vertex, y_pos_vertex = self.get_offsetted_values(x_pos, y_pos, 0.07)
            plt.plot(x_pos_vertex, y_pos_vertex, 'wo', mew=2, ms=20)
        plt.axis([-2 * self.radius, 2 * self.radius, -2 * self.radius, 2 * self.radius])
        plt.title("Graph of %d vertices, %d edges" % (self.num_vertices, len(edge_list)), loc='center')
        plt.show()
if __name__ == "__main__":
    graph_matrix = np.array([[0, 1, 1, 0],
                             [1, 0, 1, 1],
                             [1, 1, 0, 1],
                             [0, 1, 1, 0]])
    plotter = PlotGraph(graph_matrix)
    plotter.plot()