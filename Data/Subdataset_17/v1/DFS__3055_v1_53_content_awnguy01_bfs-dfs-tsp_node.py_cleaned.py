from typing import List
class Node:
    def __init__(self, name: str, x: float = 0, y: float = 0, dest_nodes: List['Node'] = None):
        if dest_nodes is None:
            dest_nodes = []
        self.name = name
        self.x = x
        self.y = y
        self.dest_nodes = dest_nodes
    def __eq__(self, other):
        return isinstance(other, Node) and self.name == other.name
    def dest_nodes_to_string(self):
        next_nodes_str = '['
        if self.dest_nodes:
            next_nodes_str += ','.join(node.name for node in self.dest_nodes)
        next_nodes_str += ']'
        return next_nodes_str
if __name__ == "__main__":
    node_a = Node('A')
    node_b = Node('B')
    node_c = Node('C')
    node_d = Node('D', dest_nodes=[node_a, node_b])
    node_e = Node('E', dest_nodes=[node_b, node_c])
    print(f"Node D destination nodes: {node_d.dest_nodes_to_string()}")
    print(f"Node E destination nodes: {node_e.dest_nodes_to_string()}")
    print(f"Node A equals Node B: {node_a == node_b}")
    print(f"Node A equals Node A: {node_a == node_a}")