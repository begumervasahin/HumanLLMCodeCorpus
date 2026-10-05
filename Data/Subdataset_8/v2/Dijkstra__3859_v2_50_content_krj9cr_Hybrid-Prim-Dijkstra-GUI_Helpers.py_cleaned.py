import math
import matplotlib.pyplot as plt
from sympy import *
from Node import Node
def generate_points_on_circle(radius, num_points=100):
    return [(0, 0)] + [(cos(2 * pi / num_points * x) * radius, sin(2 * pi / num_points * x) * radius) for x in range(num_points + 1)]
def calculate_distance(node1, node2):
    return math.sqrt((node1.x - node2.x) ** 2 + (node1.y - node2.y) ** 2)
def generate_graph(radius=1.0, num_nodes=8):
    points = generate_points_on_circle(radius, num_nodes)
    nodes = [Node(points[i][0], points[i][1], i) for i in range(len(points))]
    edges = [[calculate_distance(nodes[i], nodes[j]) if i != j else 0 for j in range(len(nodes))] for i in range(len(nodes))]
    return points, nodes, edges
def plot_graph(points, edges, radius=1.0):
    x = [p[0] for p in points]
    y = [p[1] for p in points]
    plt.plot(x, y, 'ro')
    for edge in edges:
        print(edge[0].idx, edge[1].idx)
        plt.plot([edge[0].x, edge[1].x], [edge[0].y, edge[1].y], 'b-', lw=1)
    size = radius * 2
    plt.axis([-size, size, -size, size])
    plt.grid(True)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()
def main():
    circle_radius = 1.0
    num_nodes = 8
    points, nodes, edges = generate_graph(circle_radius, num_nodes)
    plot_graph(points, edges, circle_radius)
if __name__ == "__main__":
    main()