import graphviz
from math import inf
class TemporalEdge:
    def __init__(self, source, destination, time):
        self.source = source
        self.destination = destination
        self.time = time
        self.is_traversed = False
class TemporalGraph:
    def __init__(self):
        self.edges = []
        self.nodes = set()
    def add_edge(self, source, destination, time):
        self.edges.append(TemporalEdge(source, destination, time))
        self.nodes.add(source)
        self.nodes.add(destination)
    def get_nodes(self):
        return list(self.nodes)
    def get_neighbors(self, node):
        neighbors = set()
        for edge in self.edges:
            if edge.source == node:
                neighbors.add(edge.destination)
        return list(neighbors)
    def get_edge_neighbor(self, node, neighbor):
        return [edge for edge in self.edges if edge.source == node and edge.destination == neighbor]
class TreeNode:
    def __init__(self, name, time):
        self.name = name
        self.time = time
        self.children = []
    def add_node(self, node):
        self.children.append(node)
def draw_tree(root, filename):
    dot = graphviz.Digraph(comment='DFS_v1 Tree')
    def add_edges(node):
        for child in node.children:
            dot.edge(f"{node.name} ({node.time})", f"{child.name} ({child.time})")
            add_edges(child)
    add_edges(root)
    dot.render(filename, view=True)
def find_edge_with_min_time(edges):
    return min(edges, key=lambda edge: edge.time)
def dfs_v1(current_node):
    global current_tree_node
    for v in graph.get_neighbors(current_node):
        if v == predecessor[current_tree_node.name]:
            continue
        edges = [edge for edge in graph.get_edge_neighbor(current_node, v) if not edge.is_traversed and sigma[current_node] <= edge.time]
        if edges:
            edge_min = find_edge_with_min_time(edges)
            edge_min.is_traversed = True
            if sigma[edge_min.destination] > edge_min.time:
                next_tree_node = TreeNode(edge_min.destination, edge_min.time)
                predecessor[next_tree_node.name] = current_tree_node.name
                current_tree_node.add_node(next_tree_node)
                current_tree_node = next_tree_node
                sigma[edge_min.destination] = edge_min.time
                dfs_v1(edge_min.destination)
    current_tree_node = tree_node_map[predecessor[current_tree_node.name]]
if __name__ == "__main__":
    graph = TemporalGraph()
    edges = [["a", "b", 1], ["a", "b", 6], ["b", "a", 8], ["b", "c", 4], ["b", "c", 7],
             ["c", "b", 6], ["a", "f", 3], ["a", "f", 7], ["f", "c", 5], ["f", "h", 2],
             ["f", "g", 8], ["g", "a", 9]]
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
    tree_node_map = {source: tree_node_root}
    dfs_v1(source)
    draw_tree(tree_node_root, 'DFS_v1')