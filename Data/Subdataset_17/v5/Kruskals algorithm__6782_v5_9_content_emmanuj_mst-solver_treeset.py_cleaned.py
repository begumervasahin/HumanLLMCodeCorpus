from node import Node
class TreeSet:
    def __init__(self):
        self.nodes = {}
    def make_set(self, value):
        if value not in self.nodes:
            self.nodes[value] = Node(value)
    def find(self, value):
        node = self.nodes[value]
        if node.parent != node:
            node.parent = self.nodes[self.find(node.parent.value)]
        return node.parent.value
    def union(self, value_u, value_v):
        root_u = self.nodes[self.find(value_u)]
        root_v = self.nodes[self.find(value_v)]
        if root_u != root_v:
            if root_u.rank > root_v.rank:
                root_v.parent = root_u
            elif root_u.rank < root_v.rank:
                root_u.parent = root_v
            else:
                root_v.parent = root_u
                root_u.rank += 1
    def print_data(self):
        for value, node in self.nodes.items():
            parent_value = node.parent.value if node.parent else None
            print(f"Node: {value}, Parent: {parent_value}, Rank: {node.rank}")
