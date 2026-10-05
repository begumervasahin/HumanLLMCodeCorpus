class Node:
    def __init__(self, value):
        self.value = value
        self.parent = self
        self.rank = 0
    def __repr__(self):
        return f"Node(value={self.value}, rank={self.rank}, parent={self.parent.value})"
class TreeSet:
    def __init__(self):
        self.nodes = {}
    def make_set(self, value):
        self.nodes[value] = Node(value)
    def find(self, value):
        grandparent = self.nodes[value].parent.parent
        while grandparent != self.nodes[value].parent:
            self.nodes[value].parent = grandparent
            value = grandparent.value
            grandparent = self.nodes[value].parent.parent
        return grandparent.value
    def union(self, u, v):
        pointer = None
        node_u = self.nodes[u]
        node_v = self.nodes[v]
        if node_u.rank > node_v.rank:
            node_v.parent = node_u
            pointer = node_u
        elif node_u.rank < node_v.rank:
            node_u.parent = node_v
            pointer = node_v
        else:
            node_u.parent = node_v
            node_v.rank += 1
            pointer = node_v
        return pointer
    def print_data(self):
        print(self.nodes)
tree_set = TreeSet()
tree_set.make_set(1)
tree_set.make_set(2)
tree_set.make_set(3)
print("Initial TreeSet:")
tree_set.print_data()
print("\nFinding representative of 2:", tree_set.find(2))
print("Finding representative of 3:", tree_set.find(3))
print("\nUnion of 2 and 3:")
ptr = tree_set.union(2, 3)
tree_set.print_data()
print("Parent of representative of 2 after union:", ptr)