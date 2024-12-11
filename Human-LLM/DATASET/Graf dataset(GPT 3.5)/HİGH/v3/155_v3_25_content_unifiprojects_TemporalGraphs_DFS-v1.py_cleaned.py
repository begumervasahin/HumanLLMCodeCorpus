
from temporal_graph import TemporalGraph
from TreeNode import TreeNode
from draw_tree import draw_tree
from math import inf
def fonk1(b7):
    b1 = min(b7, key=lambda x: x.time)
    return b1
def fonk2(current_node):
    global b5
    for neighbor in b6.get_neighbors(current_node):
        if neighbor is b12[b5.name]:
            continue
        b2 = [edge for edge in b6.get_edge_neighbor(current_node, neighbor) if not edge.b3 and b9[current_node] <= edge.time]
        if b2:
            b1 = fonk1(b2)
            b1.b3 = True
            if b9[b1.destination] > b1.time:
                b4 = TreeNode(b1.destination, b1.time)
                b12[b4.name] = b5
                b5.add_node(b4)
                b5 = b4
                b9[b1.destination] = b1.time
                fonk2(b1.destination)
    b5 = b12[b5.name]
b6 = TemporalGraph()
b7 = [
    ["a", "b", 1], ["a", "b", 6], ["b", "a", 8], ["b", "c", 4],
    ["b", "c", 7], ["c", "b", 6], ["a", "f", 3], ["a", "f", 7],
    ["f", "c", 5], ["f", "h", 2], ["f", "g", 8], ["g", "a", 9]
]
for b10, destination, time in b7:
    b6.add_edge(b10, destination, time)
a1 = 2
b8 = b6.get_nodes()
b9 = {node: inf for node in b8}
b10 = b8[0]
b9[b10] = a1
b11 = TreeNode(b10, a1)
b12 = {node: None for node in b8}
b5 = b11
fonk2(b10)
draw_tree(b11, 'DFS_v1')