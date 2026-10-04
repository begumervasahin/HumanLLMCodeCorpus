import sys
from copy import deepcopy
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
        tree = cls('X')
        cls._create_tree_helper(tree, depth, 1)
        return tree
    @classmethod
    def _create_tree_helper(cls, node, depth, current_depth):
        if current_depth == depth:
            return
        node.left = Node('X')
        node.right = Node('XX')
        cls._create_tree_helper(node.left, depth, current_depth + 1)
        cls._create_tree_helper(node.right, depth, current_depth + 1)
    def get_height(self):
        return self._get_height_helper(self)
    @staticmethod
    def _get_height_helper(node):
        if not node:
            return 0
        return max(Node._get_height_helper(node.left), Node._get_height_helper(node.right)) + 1
    def fill_tree(self, height):
        self._fill_tree_helper(self, height)
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
        queue.enqueue(tree)
        current_level = 1
        while not queue.is_empty():
            level_queue = Queue()
            while not queue.is_empty():
                level_queue.enqueue(queue.dequeue())
            first_in_layer = True
            edges_string = ""
            extra_spaces_next_node = False
            while not level_queue.is_empty():
                node = level_queue.dequeue()
                spaces_front = 2 ** (total_layers - current_level + 1) - 2
                spaces_mid = 2 ** (total_layers - current_level + 2) - 2
                dash_count = max(2 ** (total_layers - current_level) - 2, 0)
                spaces_mid -= dash_count * 2
                spaces_front -= dash_count
                init_padding = 2
                spaces_front += init_padding
                if first_in_layer:
                    edges_string += " " * init_padding
                edge_left = "/" if node.left and node.left.data != " " else " "
                edge_right = "\\" if node.right and node.right.data != " " else " "
                if first_in_layer:
                    edges_string += " " * (2 ** (total_layers - current_level) - 1) + edge_left
                else:
                    edges_string += " " * (2 ** (total_layers - current_level + 1) + 1) + edge_left
                edges_string += " " * (2 ** (total_layers - current_level + 1) - 3) + edge_right
                dash_left = "_" if node.left and node.left.data != " " else " "
                dash_right = "_" if node.right and node.right.data != " " else " "
                extra_spaces = 1 if extra_spaces_next_node else 0
                extra_spaces_next_node = False
                data_length = len(str(node.data))
                if data_length > 1:
                    if data_length % 2 == 1:
                        if dash_count > 0:
                            dash_count -= (data_length - 1)
                        else:
                            spaces_mid -= (data_length - 1)
                            spaces_front -= (data_length - 1)
                            extra_spaces_next_node = data_length != 1
                    else:
                        if dash_count > 0:
                            dash_count -= data_length
                            extra_spaces_next_node = True
                        else:
                            spaces_mid -= data_length - 1
                            spaces_front -= data_length - 1
                if first_in_layer:
                    print(" " * spaces_front + dash_left * dash_count + node.data + dash_right * dash_count, end='')
                    first_in_layer = False
                else:
                    print(" " * (spaces_mid - extra_spaces) + dash_left * dash_count + node.data + dash_right * dash_count, end='')
                if node.left:
                    queue.enqueue(node.left)
                if node.right:
                    queue.enqueue(node.right)
            if not queue.is_empty():
                print("\n" + edges_string)
            current_level += 1
class Queue:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return len(self.items) == 0
    def enqueue(self, item):
        self.items.append(item)
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None
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