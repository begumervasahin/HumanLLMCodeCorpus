class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node
        self.previous_node = None
        self.image = None
    def set_next_node(self, next_node):
        self.next_node = next_node
    def get_next_node(self):
        return self.next_node
    def set_previous_node(self, previous_node):
        self.previous_node = previous_node
    def get_previous_node(self):
        return self.previous_node
    def get_value(self):
        return self.value
    def assign_image(self, image):
        self.image = image
    def get_image(self):
        return self.image
if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node1.set_next_node(node2)
    node2.set_previous_node(node1)
    node2.set_next_node(node3)
    node3.set_previous_node(node2)
    node1.assign_image('image1.png')
    node2.assign_image('image2.png')
    node3.assign_image('image3.png')
    current_node = node1
    while current_node is not None:
        print(f'Node Value: {current_node.get_value()}')
        print(f'Node Image: {current_node.get_image()}')
        current_node = current_node.get_next_node()