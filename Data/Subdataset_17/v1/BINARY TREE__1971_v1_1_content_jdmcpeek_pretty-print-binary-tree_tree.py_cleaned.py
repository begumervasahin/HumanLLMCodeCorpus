import sys
from copy import deepcopy
class Queue:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def enqueue(self, item):
        self.items.insert(0, item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
    def visit(self):
        sys.stdout.write(self.data)
    def getNumNodes(self):
        total = 0
        if self.left:
            total += self.left.getNumNodes()
        if self.right:
            total += self.right.getNumNodes()
        return total + 1
    @classmethod
    def createTree(cls, depth):
        tree = Node('X')
        cls.createTreeHelper(tree, depth, 1)
        return tree
    @classmethod
    def createTreeHelper(cls, node, depth, cur):
        if cur == depth:
            return
        node.left = Node('X')
        node.right = Node('XX')
        cls.createTreeHelper(node.left, depth, cur + 1)
        cls.createTreeHelper(node.right, depth, cur + 1)
    def getHeight(self):
        return Node.getHeightHelper(self)
    @staticmethod
    def getHeightHelper(node):
        if not node:
            return 0
        else:
            return max(Node.getHeightHelper(node.left), Node.getHeightHelper(node.right)) + 1
    def fillTree(self, height):
        Node.fillTreeHelper(self, height)
    @staticmethod
    def fillTreeHelper(node, height):
        if height <= 1:
            return
        if node:
            if not node.left:
                node.left = Node(' ')
            if not node.right:
                node.right = Node(' ')
            Node.fillTreeHelper(node.left, height - 1)
            Node.fillTreeHelper(node.right, height - 1)
    def prettyPrint(self):
        total_layers = self.getHeight()
        tree = deepcopy(self)
        tree.fillTree(total_layers)
        queue = Queue()
        queue.enqueue(tree)
        gen = 1
        while not queue.isEmpty():
            copy = Queue()
            while not queue.isEmpty():
                copy.enqueue(queue.dequeue())
            first_item_in_layer = True
            edges_string = ""
            extra_spaces_next_node = False
            while not copy.isEmpty():
                node = copy.dequeue()
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
                edge_sym = "/" if node.left and node.left.data != " " else " "
                if first_item_in_layer:
                    edges_string += " " * (pow(2, total_layers - gen) - 1) + edge_sym
                else:
                    edges_string += " " * (pow(2, total_layers - gen + 1) + 1) + edge_sym
                edge_sym = "\\" if node.right and node.right.data != " " else " "
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
                            dash_count -= ((data_length - 1)
                        else:
                            spaces_mid -= (data_length - 1)
                            spaces_front -= (data_length - 1)
                            if data_length != 1:
                                extra_spaces_next_node = True
                    else:
                        if dash_count > 0:
                            dash_count -= (data_length
                            extra_spaces_next_node = True
                        else:
                            spaces_mid -= (data_length - 1)
                            spaces_front -= (data_length - 1)
                if first_item_in_layer:
                    print(" " * spaces_front + dash_left * dash_count + node.data + dash_right * dash_count, end=' ')
                    first_item_in_layer = False
                else:
                    print(" " * (spaces_mid - extra_spaces) + dash_left * dash_count + node.data + dash_right * dash_count, end=' ')
                if node.left:
                    queue.enqueue(node.left)
                if node.right:
                    queue.enqueue(node.right)
            if not queue.isEmpty():
                print("\n" + edges_string)
            gen += 1
if __name__ == '__main__':
    root = Node('A')
    root.left = Node('B')
    root.right = Node('C')
    root.left.left = Node('D')
    root.left.right = Node('E')
    root.left.right.right = Node.createTree(2)
    root.right.left = Node('F')
    root.right.right = Node('G')
    root.left.left.left = Node('H')
    root.left.left.right = Node('I')
    root.left.right.left = Node('J')
    root.right.right.left = Node('N')
    root.right.right.right = Node('O')
    root.prettyPrint()