import math
import matplotlib.pyplot as plt
from sympy import cos, sin, pi
class Node:
    def __init__(self, x, y, idx):
        self.x = x
        self.y = y
        self.idx = idx
def points_in_circumference(radius, num_points=100):
    return [(0, 0)] + [(cos(2 * pi / num_points * x) * radius,
                        sin(2 * pi / num_points * x) * radius)
                       for x in range(num_points + 1)]
def distance(node1, node2):
    return math.sqrt((node1.x - node2.x) ** 2 + (node1.y - node2.y) ** 2)
def generate_graph(radius=1.0, num_points=8):
    points = points_in_circumference(radius, num_points)
    nodes = [Node(x, y, i) for i, (x, y) in enumerate(points)]
    edges = []
    for i in range(len(nodes)):
        row = []
        for j in range(len(nodes)):
            if i == j:
                row.append(0)
            else:
                row.append(distance(nodes[i], nodes[j]))
        edges.append(row)
    return points, nodes, edges
def plot_graph(points, edges, radius=1.0):
    x = [p[0] for p in points]
    y = [p[1] for p in points]
    plt.plot(x, y, 'ro')
    for edge in edges:
        plt.plot([edge[0].x, edge[1].x], [edge[0].y, edge[1].y], 'b-', lw=1)
    size = radius * 2
    plt.axis([-size, size, -size, size])
    plt.grid(True)
    plt.gca().set_aspect('equal', 'datalim')
    plt.show()
if __name__ == "__main__":
    points, nodes, edges = generate_graph(radius=1.0, num_points=8)
    edge_list = [(nodes[i], nodes[j]) for i in range(len(nodes)) for j in range(len(nodes)) if i != j]
    plot_graph(points, edge_list, radius=1.0)