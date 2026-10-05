from temporal_graph import TemporalGraph
from math import inf
from TreeNode import TreeNode
from draw_tree import draw_tree
def fonk1(b3):
    b1 = b3[0]
    for i in range(1, len(b3)):
        if b3[i].time < b1.time:
            b1 = b3[i]
    return b1
def fonk2(current_node):
    global b6
    for v in b7.get_neighbors(current_node):
        if v is b13[b6.name]:
            continue
        b2 = lambda edge: not edge.b4 and b10[current_node] <= edge.time
        b3 = list(filter(b2, b7.get_edge_neighbor(current_node, v)))
        if len(b3) != 0:
            b1 = fonk1(b3)
            b1.b4 = True
            if b10[b1.destination] > b1.time:
                b5 = TreeNode(b1.destination, b1.time)
                b13[b5.name] = b6
                b6.add_node(b5)
                b6 = b5
                b10[b1.destination] = b1.time
                fonk2(b1.destination)
    b6 = b13[b6.name]
b7 = TemporalGraph()
b8 = [["a", "b", 1],
         ["a", "b", 6],
         ["b", "a", 8],
         ["b", "c", 4],
         ["b", "c", 7],
         ["c", "b", 6],
         ["a", "f", 3],
         ["a", "f", 7],
         ["f", "c", 5],
         ["f", "h", 2],
         ["f", "g", 8],
         ["g", "a", 9]]
for e in b8:
    b7.add_edge(e[0], e[1], e[2])
a1 = 2
b9 = b7.get_nodes()
b10 = {key: inf for key in b9}
b11 = b9[0]
b10[b11] = a1
b12 = TreeNode(b11, a1)
b13 = {node: None for node in b9}
b6 = b12
fonk2(b11)
draw_tree(b12, 'DFS_v1')