import math
import matplotlib.pyplot as plt
from sympy import *
from Node import Node
def pointsInCircum(r, n=100):
    return [(0, 0)] + [(cos(2 * pi / n * x) * r, sin(2 * pi / n * x) * r) for x in range(0, n + 1)]
def distance(node1, node2):
    return math.sqrt((node1.x - node2.x) ** 2 + (node1.y - node2.y) ** 2)
def generateGraph(radius=1.0, n=8):
    points = pointsInCircum(radius, n)
    nodes = [Node(points[i][0], points[i][1], i) for i in range(len(points))]
    edges = [[distance(nodes[i], nodes[j]) if i != j else 0 for j in range(len(nodes))] for i in range(len(nodes))]
    return points, nodes, edges
def plotGraph(points, lines, radius=1.0):
    x = [p[0] for p in points]
    y = [p[1] for p in points]
    plt.plot(x, y, 'ro')
    for line in lines:
        print(line[0].idx, line[1].idx)
        plt.plot([line[0].x, line[1].x], [line[0].y, line[1].y], 'b-', lw=1)
    size = radius * 2
    plt.axis([-size, size, -size, size])
    plt.grid(True)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()
def main():
    radius = 1.0
    n = 8
    points, nodes, edges = generateGraph(radius, n)
    plotGraph(points, edges, radius)
if __name__ == "__main__":
    main()