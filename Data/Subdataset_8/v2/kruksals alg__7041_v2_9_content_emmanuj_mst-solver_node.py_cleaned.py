class Node:
    def __init__(self, value):
        self.value = value
        self.parent = self
        self.rank = 0
    def __repr__(self):
        return f"Node(value={self.value}, rank={self.rank}, parent={self.parent.value})"
node1 = Node('A')
node2 = Node('B')
node3 = Node('C')
print(node1)
print(node2)
print(node3)
