class Node:
    def __init__(self, x_location, y_location, k_value, adjacent_nodes):
        self.x_location = x_location
        self.y_location = y_location
        self.k_value = k_value
        self.adjacent_nodes = adjacent_nodes
    def __eq__(self, other_node):
        return (
            self.x_location == other_node.x_location
            and self.y_location == other_node.y_location
            and self.k_value == other_node.k_value
        )