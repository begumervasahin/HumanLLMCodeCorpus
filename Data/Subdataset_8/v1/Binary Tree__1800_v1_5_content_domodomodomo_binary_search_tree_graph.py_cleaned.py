import graphviz
import random
import string
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
class BinarySearchTree:
    def __init__(self):
        self.root = None
    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert_recursively(self.root, value)
    def _insert_recursively(self, current_node, value):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self._insert_recursively(current_node.left, value)
        elif value > current_node.value:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self._insert_recursively(current_node.right, value)
def source(binary_search_tree, max_depth=0):
    diagraph = _create_diagraph(binary_search_tree, max_depth)
    return diagraph.source
def render(binary_search_tree, max_depth=0, file_name='sample'):
    diagraph = _create_diagraph(binary_search_tree, max_depth)
    diagraph.render('img/' + file_name, cleanup=True)
def _create_diagraph(binary_search_tree, max_depth=0):
    root = binary_search_tree.root
    node_list = [node for node in _node_generator(root)]
    route_list = [list(_route(root, node)) for node in node_list]
    depth_list = [len(route) - 1 for route in route_list]
    max_depth = max_depth if max_depth else max(depth_list)
    height_list = [max_depth - depth for depth in depth_list]
    diagraph = graphviz.Digraph('BST', format='png')
    for node, height in zip(node_list, height_list):
        diagraph.node(str(id(node)), str(node.value))
        if node.left:
            diagraph.edge(str(id(node)), str(id(node.left)))
        elif height:
            _blank_edge(diagraph, str(id(node)), height)
        if node.right:
            diagraph.edge(str(id(node)), str(id(node.right)))
        elif height:
            _blank_edge(diagraph, str(id(node)), height)
    return diagraph
def _blank_edge(diagraph, identity, height):
    diagraph.edge(identity, _blank_tree(diagraph, height - 1), color='gray91')
def _blank_tree(diagraph, height):
    lowercase = string.ascii_lowercase
    identity = ''.join([random.choice(lowercase) for _ in range(10)])
    diagraph.node(identity, '', color='gray91')
    if height:
        _blank_edge(diagraph, identity, height)
        _blank_edge(diagraph, identity, height)
    return identity
def _node_generator(root):
    if root:
        yield root
        for node in _node_generator(root.left):
            yield node
        for node in _node_generator(root.right):
            yield node
def _route(root, node):
    if root:
        if root == node or _route(root.left, node) or _route(root.right, node):
            yield root
if __name__ == "__main__":
    bst = BinarySearchTree()
    values = [5, 3, 7, 2, 4, 6, 8]
    for value in values:
        bst.insert(value)
    render(bst)