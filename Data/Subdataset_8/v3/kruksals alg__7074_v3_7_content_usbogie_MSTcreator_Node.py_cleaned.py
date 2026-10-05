class Node:
    def __init__(self, x, y, key, adjacency_list):
        self.x = x
        self.y = y
        self.key = key
        self.adjacency_list = adjacency_list
    def __eq__(self, other):
        return (self.x, self.y, self.key) == (other.x, other.y, other.key)
node1 = Node(1, 2, 3, [4, 5, 6])
node2 = Node(1, 2, 3, [4, 5, 6])
node3 = Node(4, 5, 6, [7, 8, 9])
print("Are node1 and node2 equal?", node1 == node2)
print("Are node1 and node3 equal?", node1 == node3)
