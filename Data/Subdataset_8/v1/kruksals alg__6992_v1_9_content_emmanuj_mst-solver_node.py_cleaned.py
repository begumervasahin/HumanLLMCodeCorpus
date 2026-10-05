class Node:
    def __init__(self, val):
        self.value = val
        self.parent = self
        self.rank = 0
    def __repr__(self):
        return "n " + str(self.value) + " r " + str(self.rank) + " p " + str(self.parent.value)
node1 = Node('A')
node2 = Node('B')
node3 = Node('C')
print(node1)
print(node2)
print(node3)
