from typing import List, Optional
class Node:
    def __init__(self, name: str, x: float = 0, y: float = 0, dest_nodes: Optional[List['Node']] = None):
        self.name = name
        self.x = x
        self.y = y
        self.dest_nodes = dest_nodes if dest_nodes else []
    def __eq__(self, other: 'Node') -> bool:
        return isinstance(other, Node) and self.name == other.name
    def dest_nodes_to_string(self) -> str:
        if not self.dest_nodes:
            return '[]'
        node_names = ', '.join(node.name for node in self.dest_nodes)
        return f'[{node_names}]'
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