from temporal_graph import TemporalGraph
from math import inf
from TreeNode import TreeNode
from draw_tree import draw_tree
def find_edge_with_min_time(E):
    edge_min = E[0]
    for i in range(1, len(E)):
        if E[i].time < edge_min.time:
            edge_min = E[i]
    return edge_min
def dfs_v1(current_node):
    global current_tree_node
    for v in graph.get_neighbors(current_node):
        if v is predecessor[current_tree_node.name]:
            continue
        filter_function = lambda edge: not edge.is_traversed and sigma[current_node] <= edge.time
        E = list(filter(filter_function, graph.get_edge_neighbor(current_node, v)))
        if len(E) != 0:
            edge_min = find_edge_with_min_time(E)
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
edges = [["a", "b", 1],
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
for e in edges:
    graph.add_edge(e[0], e[1], e[2])
starting_time = 2
V = graph.get_nodes()
sigma = {key: inf for key in V}
source = V[0]
sigma[source] = starting_time
tree_node_root = TreeNode(source, starting_time)
predecessor = {node: None for node in V}
current_tree_node = tree_node_root
dfs_v1(source)
draw_tree(tree_node_root, 'DFS_v1')