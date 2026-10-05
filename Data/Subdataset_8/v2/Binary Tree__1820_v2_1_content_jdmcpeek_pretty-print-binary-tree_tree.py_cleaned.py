from queue import Queue
from copy import deepcopy as deepcopy
import sys
class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
    def visit(self):
        sys.stdout.write(self.data)
    def get_num_nodes(self):
        total = 0
        if self.left:
            total += self.left.get_num_nodes()
        if self.right:
            total += self.right.get_num_nodes()
        return total + 1
    @classmethod
    def create_tree(cls, depth):
        tree = Node('X')
        cls.create_tree_helper(tree, depth, 1)
        return tree
    @classmethod
    def create_tree_helper(cls, node, depth, cur):
        if cur == depth:
            return
        node.left = Node('X')
        node.right = Node('XX')
        cls.create_tree_helper(node.left, depth, cur + 1)
        cls.create_tree_helper(node.right, depth, cur + 1)
    def get_height(self):
        return Node.get_height_helper(self)
    @staticmethod
    def get_height_helper(node):
        if not node:
            return 0
        else:
            return max(Node.get_height_helper(node.left), Node.get_height_helper(node.right)) + 1
    def fill_tree(self, height):
        Node.fill_tree_helper(self, height)
    def fill_tree_helper(node, height):
        if height <= 1:
            return
        if node:
            if not node.left:
                node.left = Node(' ')
            if not node.right:
                node.right = Node(' ')
            Node.fill_tree_helper(node.left, height - 1)
            Node.fill_tree_helper(node.right, height - 1)
    def pretty_print(self):
        total_layers = self.get_height()
        tree = deepcopy(self)
        tree.fill_tree(total_layers)
        queue = Queue()
        queue.put(tree)
        gen = 1
        while not queue.empty():
            copy = Queue()
            while not queue.empty():
                copy.put(queue.get())
            first_item_in_layer = True
            edges_string = ""
            extra_spaces_next_node = False
            while not copy.empty():
                node = copy.get()
                spaces_front = pow(2, total_layers - gen + 1) - 2
                spaces_mid = pow(2, total_layers - gen + 2) - 2
                dash_count = pow(2, total_layers - gen) - 2
                if dash_count < 0:
                    dash_count = 0
                spaces_mid = spaces_mid - (dash_count * 2)
                spaces_front = spaces_front - dash_count
                init_padding = 2
                spaces_front += init_padding
                if first_item_in_layer:
                    edges_string += " " * init_padding
                edge_sym = "/" if node.left and node.left.data is not " " else " "
                if first_item_in_layer:
                    edges_string += " " * (pow(2, total_layers - gen) - 1) + edge_sym
                else:
                    edges_string += " " * (pow(2, total_layers - gen + 1) + 1) + edge_sym
                edge_sym = "\\" if node.right and node.right.data is not " " else " "
                edges_string += " " * (pow(2, total_layers - gen + 1) - 3) + edge_sym
                if node.left and node.left.data == " ":
                    dash_left = " "
                else:
                    dash_left = "_"
                if node.right and node.right.data == " ":
                    dash_right = " "
                else:
                    dash_right = "_"
                if extra_spaces_next_node:
                    extra_spaces = 1
                    extra_spaces_next_node = False
                else:
                    extra_spaces = 0
                data_length = len(str(node.data))
                if data_length > 1:
                    if data_length % 2 == 1:
                        if dash_count > 0:
                            dash_count -= ((data_length - 1) / 2)
                        else:
                            spaces_mid -= (data_length - 1) / 2
                            spaces_front -= (data_length - 1) / 2
                            if data_length is not 1:
                                extra_spaces_next_node = True
                    else:
                        if dash_count > 0:
                            dash_count -= ((data_length) / 2) - 1
                            extra_spaces_next_node = True
                        else:
                            spaces_mid -= (data_length - 1)
                            spaces_front -= (data_length - 1)
                if first_item_in_layer:
                    print(" " * spaces_front) + (dash_left * dash_count) + (node.data) + (dash_right * dash_count),
                    first_item_in_layer = False
                else:
                    print(" " * (spaces_mid - extra_spaces)) + (dash_left * dash_count) + (node.data) + (
                                dash_right * dash_count),
                if node.left:
                    queue.put(node.left)
                if node.right:
                    queue.put(node.right)
            if not queue.empty():
                print("\n" + edges_string)
            gen += 1
if __name__ == '__main__':
    root = Node('A')
    root.left = Node('B')
    root.right = Node('C')
    root.left.left = Node('D')
    root.left.right = Node('E')
    root.left.right.right = Node.create_tree(2)
    root.right.left = Node('F')
    root.right.right = Node('G')
    root.left.left.left = Node('H')
    root.left.left.right = Node('I')
    root.left.right.left = Node('J')
    root.right.right.left = Node('N')
    root.right.right.right = Node('O')
    root.pretty_print()