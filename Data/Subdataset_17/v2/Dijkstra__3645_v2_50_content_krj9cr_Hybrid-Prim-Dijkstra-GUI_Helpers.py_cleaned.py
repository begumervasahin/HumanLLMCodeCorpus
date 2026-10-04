import math
import matplotlib.pyplot as plt
from sympy import cos, sin, pi
class Node:
    def __init__(self, x, y, idx):
        self.x = x
        self.y = y
        self.idx = idx
def generate_points_on_circle(radius, num_points=100):
    return [(cos(2 * pi / num_points * i) * radius,
             sin(2 * pi / num_points * i) * radius)
            for i in range(num_points)]
def calculate_distance(node1, node2):
    return math.sqrt((node1.x - node2.x) ** 2 + (node1.y - node2.y) ** 2)
def create_graph(radius=1.0, num_points=8):
    points = generate_points_on_circle(radius, num_points)
    nodes = [Node(x, y, i) for i, (x, y) in enumerate(points)]
    distances = [[0 if i == j else calculate_distance(nodes[i], nodes[j])
                  for j in range(num_points)] for i in range(num_points)]
    return points, nodes, distances
def plot_graph(points, edges, radius=1.0):
    x_coords, y_coords = zip(*points)
    plt.plot(x_coords, y_coords, 'ro')
    for edge in edges:
        plt.plot([edge[0].x, edge[1].x], [edge[0].y, edge[1].y], 'b-', lw=1)
    plt.axis([-radius*2, radius*2, -radius*2, radius*2])
    plt.grid(True)
    plt.gca().set_aspect('equal', 'datalim')
    plt.show()
if __name__ == "__main__":
    points, nodes, _ = create_graph(radius=1.0, num_points=8)
    edge_list = [(nodes[i], nodes[j]) for i in range(len(nodes)) for j in range(i + 1, len(nodes))]
    plot_graph(points, edge_list, radius=1.0)