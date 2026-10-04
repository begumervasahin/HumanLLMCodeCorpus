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
    node_list = list(log._node_generator(root))
    route_list = [list(log._route(root, node)) for node in node_list]
    depth_list = [len(route) - 1 for route in route_list]
    max_depth = max_depth if max_depth else max(depth_list)
    height_list = [max_depth - depth for depth in depth_list]
    digraph = graphviz.Digraph('BST', format='png')
    for node, height in zip(node_list, height_list):
        _add_node_with_edges(digraph, node, height)
    return digraph
def _add_node_with_edges(digraph, node, height):
    node_id = str(id(node))
    digraph.node(node_id, str(node.value))
    if node.left:
        digraph.edge(node_id, str(id(node.left)))
    elif height:
        _add_blank_edge(digraph, node_id, height)
    if node.right:
        digraph.edge(node_id, str(id(node.right)))
    elif height:
        _add_blank_edge(digraph, node_id, height)
def _add_blank_edge(digraph, node_id, height):
    blank_id = _create_blank_node(digraph, height - 1)
    digraph.edge(node_id, blank_id, color='gray91')
def _create_blank_node(digraph, height):
    blank_id = ''.join(random.choice(string.ascii_lowercase) for _ in range(10))
    digraph.node(blank_id, '', color='gray91')
    if height:
        _add_blank_edge(digraph, blank_id, height)
        _add_blank_edge(digraph, blank_id, height)
    return blank_id