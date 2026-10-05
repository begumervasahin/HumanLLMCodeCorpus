class Node:
    def __init__(self, x_coordinate, y_coordinate, key_value, adjacency_list):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.key_value = key_value
        self.adjacency_list = adjacency_list
    def __eq__(self, other):
        return (self.x_coordinate, self.y_coordinate, self.key_value) == \
               (other.x_coordinate, other.y_coordinate, other.key_value)
node1 = Node(1, 2, 3, [4, 5, 6])
node2 = Node(1, 2, 3, [4, 5, 6])
node3 = Node(4, 5, 6, [7, 8, 9])
print("Are node1 and node2 equal?", node1 == node2)
print("Are node1 and node3 equal?", node1 == node3)
