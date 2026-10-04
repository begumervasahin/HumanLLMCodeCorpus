import math
import matplotlib.pyplot as plt
from sympy import cos, sin, pi
from Node import Node
def generate_points_on_circle(radius, num_points=100):
    angle_step = 2 * pi / num_points
    return [
        (cos(angle_step * x) * radius, sin(angle_step * x) * radius)
        for x in range(num_points)
    ]
def calculate_distance(node1, node2):
    dx = node1.x - node2.x
    dy = node1.y - node2.y
    return math.sqrt(dx ** 2 + dy ** 2)
def generate_graph(radius=1.0, num_points=8):
    points = generate_points_on_circle(radius, num_points)
    nodes = [Node(x, y, i) for i, (x, y) in enumerate(points)]
    distances = [
        [calculate_distance(nodes[i], nodes[j]) if i != j else 0
         for j in range(num_points)]
        for i in range(num_points)
    ]
    return points, nodes, distances
def plot_graph(points, edges, radius=1.0):
    x_coords, y_coords = zip(*points)
    plt.figure(figsize=(8, 8))
    plt.plot(x_coords, y_coords, 'ro', label='Nodes')
    for node1, node2 in edges:
        plt.plot(
            [node1.x, node2.x],
            [node1.y, node2.y],
            'b-',
            lw=1
        )
    plt.axis([-radius * 1.5, radius * 1.5, -radius * 1.5, radius * 1.5])
    plt.grid(True)
    plt.gca().set_aspect('equal', 'datalim')
    plt.legend()
    plt.show()
if __name__ == "__main__":
    points, nodes, _ = generate_graph(radius=1.0, num_points=8)
    edge_list = [
        (nodes[i], nodes[j])
        for i in range(len(nodes))
        for j in range(i + 1, len(nodes))
    ]
    plot_graph(points, edge_list, radius=1.0)