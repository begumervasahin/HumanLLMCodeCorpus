from collections import namedtuple, deque
from pprint import pprint as pp
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'
inf = float('inf')
Edge = namedtuple('Edge', 'start, end, cost')
class Graph():
    def __init__(self, edges):
        self.edges = edges2 = [Edge(*edge) for edge in edges]
        self.vertices = set(sum(([e.start, e.end] for e in edges2), []))
    def dijkstra(self, source, dest):
        assert source in self.vertices
        dist = {vertex: inf for vertex in self.vertices}
        previous = {vertex: None for vertex in self.vertices}
        dist[source] = 0
        q = self.vertices.copy()
        neighbours = {vertex: set() for vertex in self.vertices}
        for start, end, cost in self.edges:
            neighbours[start].add((end, cost))
        while q:
            u = min(q, key=lambda vertex: dist[vertex])
            q.remove(u)
            if dist[u] == inf or u == dest:
                break
            for v, cost in neighbours[u]:
                alt = dist[u] + cost
                if alt < dist[v]:
                    dist[v] = alt
                    previous[v] = u
        s, u = deque(), dest
        while previous[u]:
            s.appendleft(u)
            u = previous[u]
        s.appendleft(u)
        return s
def drawGraph(graphItem, totalNodes, path, startNode, endNode, weight):
    G = nx.DiGraph()
    pStartNode = []
    pEndNode = []
    pWeights = []
    for idx, val in enumerate(path):
        pEndNode.append(val)
        pStartNode.append(val)
        if idx == 0:
            pEndNode.pop()
    pStartNode.pop()
    pathEdges = list(zip(pStartNode, pEndNode))
    for item in graphItem:
        for pathEdge in pathEdges:
            if pathEdge[0] == item[0] and pathEdge[1] == item[1]:
                pWeights.append(item[2])
    totalWeight = sum(pWeights)
    print('Total weight:', totalWeight)
    blackEdges = [edge for edge in G.edges() if edge not in pathEdges]
    for i in range(totalNodes):
        G.add_edge(startNode[i], endNode[i], weight=weight[i])
    edge_labels = dict([((u, v,), d['weight']) for u, v, d in G.edges(data=True)])
    pos = nx.nx_pydot.graphviz_layout(G, prog='neato')
    nx.draw(G, pos, edge_color='black', width=1, linewidths=1, node_size=500,
            node_color='pink', labels={node: node for node in G.nodes()}, arrows=False)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='black')
    nx.draw_networkx_edges(G, pos, edgelist=pathEdges, edge_color='red', arrows=True, arrowsize=24)
    nx.draw_networkx_edges(G, pos, edgelist=blackEdges, arrows=False)
    showGraph()
def swapNodes(sStartNode, sEndNode, weight):
    startNodes = []
    endNodes = []
    startNodes.extend(sStartNode)
    endNodes.extend(sEndNode)
    startNodes.extend(sEndNode)
    endNodes.extend(sStartNode)
    weight += weight
    return startNodes, endNodes, weight
def showGraph():
    plt.axis('off')
    plt.show()
edges = [(1, 2, 5), (2, 3, 7), (1, 3, 10), (2, 4, 3), (3, 4, 1)]
graph = Graph(edges)
startNode = [1, 2, 1, 2, 3]
endNode = [2, 3, 3, 4, 4]
weight = [5, 7, 10, 3, 1]
totalNodes = len(startNode)
source = 1
dest = 4
path = graph.dijkstra(source, dest)
drawGraph(edges, totalNodes, path, startNode, endNode, weight)