import graphviz
import random
import string
import log
def fonk1(binary_search_tree, b1 = 0):
    b2 = fonk3(binary_search_tree, b1)
    return b2.source
def fonk2(binary_search_tree, b1 = 0, file_name='sample'):
    b2 = fonk3(binary_search_tree, b1)
    b2.fonk2(f'img/{file_name}', b3 = True)
def fonk3(binary_search_tree, b1 = 0):
    b4 = binary_search_tree.b4
    b5 = list(log._node_generator(b4))
    b6 = [list(log._route(b4, node)) for node in b5]
    b7 = [len(route) - 1 for route in b6]
    b1 = b1 if b1 else max(b7)
    b8 = [b1 - depth for depth in b7]
    b2 = graphviz.Digraph('BST', format='png')
    for node, height in zip(b5, b8):
        fonk4(b2, node, height)
    return b2
def fonk4(b2, node, height):
    b9 = str(id(node))
    b2.node(b9, str(node.value))
    if node.left:
        b2.edge(b9, str(id(node.left)))
    elif height:
        fonk5(b2, b9, height)
    if node.right:
        b2.edge(b9, str(id(node.right)))
    elif height:
        fonk5(b2, b9, height)
def fonk5(b2, b9, height):
    b10 = fonk6(b2, height - 1)
    b2.edge(b9, b10, b11 = 'gray91')
def fonk6(b2, height):
    b10 = ''.join(random.choice(string.ascii_lowercase) for _ in range(10))
    b2.node(b10, '', b11 = 'gray91')
    if height:
        fonk5(b2, b10, height)
        fonk5(b2, b10, height)
    return b10