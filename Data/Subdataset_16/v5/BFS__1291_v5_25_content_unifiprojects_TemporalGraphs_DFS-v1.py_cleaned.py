import sys
from math import inf
from temporal_graph import TemporalGraph
from TreeNode import TreeNode
from draw_tree import draw_tree
sys.setrecursionlimit(10**6)
def fonk1(b3):
    return min(b3, b1 = lambda edge: edge.time)
def fonk2(current_node):
    global b7
    for b2 in b8.get_neighbors(current_node):
        if b2 = = b13[b7.name]:
            continue
        b3 = [edge for edge in b8.get_edge_neighbor(current_node, b2)
                 if not edge.b5 and b10[current_node] <= edge.time]
        if b3:
            b4 = fonk1(b3)
            b4.b5 = True
            if b10[b4.destination] > b4.time:
                b6 = TreeNode(b4.destination, b4.time)
                b13[b6.name] = b7
                b7.add_node(b6)
                b7 = b6
                b10[b4.destination] = b4.time
                fonk2(b4.destination)
    b7 = b13[b7.name]
b8 = TemporalGraph()
b3 = [
    ["a", "b", 1], ["a", "b", 6], ["b", "a", 8], ["b", "c", 4],
    ["b", "c", 7], ["c", "b", 6], ["a", "f", 3], ["a", "f", 7],
    ["f", "c", 5], ["f", "h", 2], ["f", "g", 8], ["g", "a", 9]
]
for edge in b3:
    b8.add_edge(edge[0], edge[1], edge[2])
a1 = 2
b9 = b8.get_nodes()
b10 = {node: inf for node in b9}
b11 = b9[0]
b10[b11] = a1
b12 = TreeNode(b11, a1)
b13 = {node: None for node in b9}
b7 = b12
fonk2(b11)
draw_tree(b12, 'DFS_v1')