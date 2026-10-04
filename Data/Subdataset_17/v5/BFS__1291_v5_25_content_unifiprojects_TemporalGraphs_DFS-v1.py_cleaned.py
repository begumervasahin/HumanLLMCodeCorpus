import sys
from math import inf
from temporal_graph import TemporalGraph
from TreeNode import TreeNode
from draw_tree import draw_tree
sys.setrecursionlimit(10**6)
def find_edge_with_min_time(edges):
    return min(edges, key=lambda edge: edge.time)
def dfs_v1(current_node):
    global current_tree_node
    for neighbor in graph.get_neighbors(current_node):
        if neighbor == predecessor[current_tree_node.name]:
            continue
        edges = [edge for edge in graph.get_edge_neighbor(current_node, neighbor)
                 if not edge.is_traversed and sigma[current_node] <= edge.time]
        if edges:
            edge_min = find_edge_with_min_time(edges)
            edge_min.is_traversed = True
            if sigma[edge_min.destination] > edge_min.time:
                next_tree_node = TreeNode(edge_min.destination, edge_min.time)
                predecessor[next_tree_node.name] = current_tree_node
                current_tree_node.add_node(next_tree_node)
                current_tree_node = next_tree_node
                sigma[edge_min.destination] = edge_min.time
                dfs_v1(edge_min.destination)
    current_tree_node = predecessor[current_tree_node.name]
graph = TemporalGraph()
edges = [
    ["a", "b", 1], ["a", "b", 6], ["b", "a", 8], ["b", "c", 4],
    ["b", "c", 7], ["c", "b", 6], ["a", "f", 3], ["a", "f", 7],
    ["f", "c", 5], ["f", "h", 2], ["f", "g", 8], ["g", "a", 9]
]
for edge in edges:
    graph.add_edge(edge[0], edge[1], edge[2])
starting_time = 2
V = graph.get_nodes()
sigma = {node: inf for node in V}
source = V[0]
sigma[source] = starting_time
tree_node_root = TreeNode(source, starting_time)
predecessor = {node: None for node in V}
current_tree_node = tree_node_root
dfs_v1(source)
draw_tree(tree_node_root, 'DFS_v1')