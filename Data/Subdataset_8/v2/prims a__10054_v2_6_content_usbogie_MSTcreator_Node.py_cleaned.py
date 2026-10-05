
class Node:
    def __init__(self, x_location, y_location, k_value, adjacency_list):
        self.x_location = x_location
        self.y_location = y_location
        self.k_value = k_value
        self.adjacency_list = adjacency_list
    def __eq__(self, other_node):
        return (self.x_location == other_node.x_location and
                self.y_location == other_node.y_location and
                self.k_value == other_node.k_value)
node1 = Node(1, 2, 3, [4, 5, 6])
node2 = Node(1, 2, 3, [4, 5, 6])
node3 = Node(4, 5, 6, [7, 8, 9])
print("Is node1 equal to node2?", node1 == node2)
print("Is node1 equal to node3?", node1 == node3)
