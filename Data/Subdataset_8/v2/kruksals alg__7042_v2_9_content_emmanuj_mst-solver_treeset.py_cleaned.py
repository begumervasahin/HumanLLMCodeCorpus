class Node:
    def __init__(self, value):
        self.value = value
        self.parent = self
        self.rank = 0
    def __repr__(self):
        return f"Node(value={self.value}, rank={self.rank}, parent={self.parent.value})"
class TreeSet:
    def __init__(self):
        self.data = {}
    def make_set(self, value):
        self.data[value] = Node(value)
    def find(self, value):
        grandparent = self.data[value].parent.parent
        while grandparent != self.data[value].parent:
            self.data[value].parent = grandparent
            value = grandparent.value
            grandparent = self.data[value].parent.parent
        return grandparent.value
    def union(self, u, v):
        pointer = None
        if self.data[u].rank > self.data[v].rank:
            self.data[v].parent = self.data[u]
            pointer = self.data[u]
        elif self.data[u].rank < self.data[v].rank:
            self.data[u].parent = self.data[v]
            pointer = self.data[v]
        else:
            self.data[u].parent = self.data[v]
            self.data[v].rank = self.data[v].rank + 1
            pointer = self.data[v]
        return pointer
    def print_data(self):
        print(self.data)
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