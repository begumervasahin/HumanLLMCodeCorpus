import graphviz
import random
import string
import log
def fonk1(binary_search_tree, b1 = 0):
    b2 = fonk3(binary_search_tree, b1)
    return b2.source
def fonk2(binary_search_tree, b1 = 0, b14='sample'):
    b2 = fonk3(binary_search_tree, b1)
    b2.fonk2('img/' + b14, b3 = True)
def fonk3(binary_search_tree, b1 = 0):
    b4 = binary_search_tree.b4
    b5 = [node for node in log._node_generator(b4)]
    b6 = [list(log._route(b4, node)) for node in b5]
    b7 = [len(route) - 1 for route in b6]
    b1 = b1 if b1 else max(b7)
    b8 = [b1 - depth for depth in b7]
    b2 = graphviz.Digraph('BST', format='png')
    for node, height in zip(b5, b8):
        b2.node(str(id(node)), str(node.value))
        if node.left:
            b2.edge(str(id(node)), str(id(node.left)))
        elif height:
            fonk4(b2, str(id(node)), height)
        if node.right:
            b2.edge(str(id(node)), str(id(node.right)))
        elif height:
            fonk4(b2, str(id(node)), height)
    return b2
def fonk4(b2, b11, height):
    b2.edge(b11, fonk5(b2, height - 1), b9 = 'gray91')
def fonk5(b2, height):
    b10 = string.ascii_lowercase
    b11 = ''.join([random.choice(b10) for _ in range(10)])
    b2.node(b11, '', b9 = 'gray91')
    if height:
        fonk4(b2, b11, height)
        fonk4(b2, b11, height)
    return b11
if b12 = = '__main__':
    from binary_search_tree import BinaryTree
    b13 = BinaryTree()
    b13.insert(10)
    b13.insert(5)
    b13.insert(15)
    b13.insert(2)
    b13.insert(7)
    b13.insert(12)
    b13.insert(20)
    fonk2(b13, b14 = 'bst_example')