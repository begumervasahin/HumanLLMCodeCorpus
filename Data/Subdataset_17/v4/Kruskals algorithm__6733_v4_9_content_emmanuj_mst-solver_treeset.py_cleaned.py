from node import Node
class TreeSet:
    def __init__(self):
        self.data = {}
    def make_set(self, value):
        self.data[value] = Node(value)
    def find(self, value):
        node = self.data[value]
        while node.parent != node:
            node.parent = node.parent.parent
            node = node.parent
        return node.value
    def union(self, value_u, value_v):
        root_u = self.data[self.find(value_u)]
        root_v = self.data[self.find(value_v)]
        if root_u.rank > root_v.rank:
            root_v.parent = root_u
            return root_u
        elif root_u.rank < root_v.rank:
            root_u.parent = root_v
            return root_v
        else:
            root_v.parent = root_u
            root_u.rank += 1
            return root_u
    def print_data(self):
        for value, node in self.data.items():
            parent_value = node.parent.value if node.parent else None
            print(f"Node: {value}, Parent: {parent_value}, Rank: {node.rank}")
