import graphviz
import random
import string
import log
def source(binary_search_tree, max_depth=0):
    digraph = _create_digraph(binary_search_tree, max_depth)
    return digraph.source
def render(binary_search_tree, max_depth=0, file_name='sample'):
    digraph = _create_digraph(binary_search_tree, max_depth)
    digraph.render(f'img/{file_name}', cleanup=True)
def _create_digraph(binary_search_tree, max_depth=0):
    root = binary_search_tree.root
    node_list = [node for node in log._node_generator(root)]
    route_list = [list(log._route(root, node)) for node in node_list]
    depth_list = [len(route) - 1 for route in route_list]
    max_depth = max_depth if max_depth else max(depth_list)
    height_list = [max_depth - depth for depth in depth_list]
    digraph = graphviz.Digraph('BST', format='png')
    for node, height in zip(node_list, height_list):
        digraph.node(str(id(node)), str(node.value))
        if node.left:
            digraph.edge(str(id(node)), str(id(node.left)))
        elif height:
            _blank_edge(digraph, str(id(node)), height)
        if node.right:
            digraph.edge(str(id(node)), str(id(node.right)))
        elif height:
            _blank_edge(digraph, str(id(node)), height)
    return digraph
def _blank_edge(digraph, identity, height):
    digraph.edge(identity, _blank_node(digraph, height - 1), color='gray91')
def _blank_node(digraph, height):
    identity = ''.join(random.choice(string.ascii_lowercase) for _ in range(10))
    digraph.node(identity, '', color='gray91')
    if height:
        _blank_edge(digraph, identity, height)
        _blank_edge(digraph, identity, height)
    return identity
if __name__ == '__main__':
    from binary_search_tree import BinaryTree
    bst = BinaryTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(2)
    bst.insert(7)
    bst.insert(12)
    bst.insert(20)
    render(bst, file_name='bst_example')