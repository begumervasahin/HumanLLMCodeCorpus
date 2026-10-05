from queue import Queue
from copy import deepcopy
class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
    def visit(self):
        print(self.data, end='')
    def get_num_nodes(self):
        total = 1
        if self.left:
            total += self.left.get_num_nodes()
        if self.right:
            total += self.right.get_num_nodes()
        return total
    @classmethod
    def create_tree(cls, depth):
        root = Node('X')
        cls._create_tree_helper(root, depth, 1)
        return root
    @staticmethod
    def _create_tree_helper(node, depth, cur):
        if cur == depth:
            return
        node.left = Node('X')
        node.right = Node('XX')
        Node._create_tree_helper(node.left, depth, cur + 1)
        Node._create_tree_helper(node.right, depth, cur + 1)
    def get_height(self):
        return Node._get_height_helper(self)
    @staticmethod
    def _get_height_helper(node):
        if not node:
            return 0
        return max(Node._get_height_helper(node.left), Node._get_height_helper(node.right)) + 1
    def fill_tree(self, height):
        Node._fill_tree_helper(self, height)
    @staticmethod
    def _fill_tree_helper(node, height):
        if height <= 1:
            return
        if node:
            if not node.left:
                node.left = Node(' ')
            if not node.right:
                node.right = Node(' ')
            Node._fill_tree_helper(node.left, height - 1)
            Node._fill_tree_helper(node.right, height - 1)
    def pretty_print(self):
        total_layers = self.get_height()
        tree = deepcopy(self)
        tree.fill_tree(total_layers)
        queue = Queue()
        queue.put(tree)
        for gen in range(1, total_layers + 1):
            copy = Queue()
            while not queue.empty():
                copy.put(queue.get())
            first_item_in_layer = True
            edges_string = ""
            extra_spaces_next_node = False
            while not copy.empty():
                node = copy.get()
                spaces_front = 2**(total_layers - gen + 1) - 2
                spaces_mid = 2**(total_layers - gen + 2) - 2
                dash_count = 2**(total_layers - gen) - 2
                if dash_count < 0:
                    dash_count = 0
                spaces_mid -= dash_count * 2
                spaces_front -= dash_count
                spaces_front += 2
                if first_item_in_layer:
                    edges_string += " " * 2
                edge_sym_left = "/" if node.left and node.left.data != " " else " "
                if first_item_in_layer:
                    edges_string += " " * (2**(total_layers - gen) - 1) + edge_sym_left
                else:
                    edges_string += " " * (2**(total_layers - gen + 1) + 1) + edge_sym_left
                edge_sym_right = "\\" if node.right and node.right.data != " " else " "
                edges_string += " " * (2**(total_layers - gen + 1) - 3) + edge_sym_right
                dash_left = "_" if node.left and node.left.data != " " else " "
                dash_right = "_" if node.right and node.right.data != " " else " "
                extra_spaces = 1 if len(str(node.data)) % 2 == 0 and dash_count > 0 else 0
                data_length = len(str(node.data))
                if first_item_in_layer:
                    print(" " * spaces_front + dash_left * dash_count + node.data + dash_right * dash_count, end='')
                    first_item_in_layer = False
                else:
                    print(" " * (spaces_mid - extra_spaces) + dash_left * dash_count + node.data + dash_right * dash_count, end='')
                if node.left:
                    queue.put(node.left)
                if node.right:
                    queue.put(node.right)
            if not queue.empty():
                print("\n" + edges_string)
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