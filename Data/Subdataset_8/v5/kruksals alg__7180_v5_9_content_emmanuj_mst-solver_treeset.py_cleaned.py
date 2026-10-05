from node import Node
class TreeSet:
    def __init__(self):
        self.elements = {}
    def make_set(self, value):
        self.elements[value] = Node(value)
    def find(self, value):
        node = self.elements[value]
        while node.parent != node.parent.parent:
            node.parent = node.parent.parent
            node = node.parent
        return node.parent.value
    def union(self, u, v):
        node_u = self.elements[u]
        node_v = self.elements[v]
        if node_u.rank > node_v.rank:
            node_v.parent = node_u
            return node_u
        elif node_u.rank < node_v.rank:
            node_u.parent = node_v
            return node_v
        else:
            node_u.parent = node_v
            node_v.rank += 1
            return node_v
    def print_data(self):
        print(self.elements)