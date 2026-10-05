class Node:
    def __init__(self, x, y, k, adjacency_list):
        self.x = x
        self.y = y
        self.k = k
        self.adjacency_list = adjacency_list
    def __eq__(self, other):
        return (self.x == other.x and
                self.y == other.y and
                self.k == other.k)
node1 = Node(1, 2, 3, [4, 5, 6])
node2 = Node(1, 2, 3, [4, 5, 6])
node3 = Node(4, 5, 6, [7, 8, 9])
print("Is node1 equal to node2?", node1 == node2)
print("Is node1 equal to node3?", node1 == node3)
