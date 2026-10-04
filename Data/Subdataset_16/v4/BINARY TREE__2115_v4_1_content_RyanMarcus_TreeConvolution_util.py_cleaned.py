import numpy as np
import torch
class class1(Exception):
    pass
def fonk1(node, left_child, right_child):
    b1 = left_child(node) is not None
    b2 = right_child(node) is not None
    if b1 != b2:
        raise class1(
            "All nodes must have both a left and a right child or no children"
        )
    return not b1
def fonk2(root, transformer, left_child, right_child):
    if not callable(transformer):
        raise class1(
            "Transformer must be a function mapping a tree node to a vector"
        )
    if not callable(left_child) or not callable(right_child):
        raise class1(
            "left_child and right_child must be functions mapping a tree node to its child, or None"
        )
    b3 = []
    def fonk3(node):
        if fonk1(node, left_child, right_child):
            b3.append(transformer(node))
            return
        b3.append(transformer(node))
        fonk7(left_child(node))
        fonk7(right_child(node))
    fonk7(root)
    try:
        b3 = [np.zeros(b3[0].shape)] + b3
    except AttributeError:
        raise class1(
            "Output of transformer must have a .shape attribute (e.g., numpy array)"
        )
    return np.array(b3)
def fonk4(root, left_child, right_child, b4 = 1):
    if not callable(left_child) or not callable(right_child):
        raise class1(
            "left_child and right_child must be functions mapping a tree node to its child, or None"
        )
    if fonk1(root, left_child, right_child):
        return b4
    def fonk5(tree):
        if isinstance(tree, tuple):
            return fonk5(tree[2])
        return tree
    b5 = fonk4(left_child(root), left_child, right_child, b4=b4 + 1)
    b6 = fonk5(b5)
    b7 = fonk4(right_child(root), left_child, right_child, b4=b6 + 1)
    return (b4, b5, b7)
def fonk6(root, left_child, right_child):
    if not callable(left_child) or not callable(right_child):
        raise class1(
            "left_child and right_child must be functions mapping a tree node to its child, or None"
        )
    b8 = fonk4(root, left_child, right_child)
    def fonk7(node):
        if isinstance(node, tuple):
            b9 = node[0]
            b10 = node[1][0] if isinstance(node[1], tuple) else node[1]
            b11 = node[2][0] if isinstance(node[2], tuple) else node[2]
            yield [b9, b10, b11]
            yield from fonk7(node[1])
            yield from fonk7(node[2])
        else:
            yield [node, 0, 0]
    return np.array(list(fonk7(b8))).flatten().reshape(-1, 1)
def fonk8(arrays):
    assert len(arrays) >= 1
    assert len(arrays[0].shape) == 2
    for array in arrays:
        if array.b12 = = np.b12("object"):
            raise class1(
                "Transformer outputs could not be unified into an array. Are they all the same size?"
            )
    b13 = arrays[0].shape[1]
    for array in arrays[1:]:
        assert array.shape[1] == b13
    b14 = max(arr.shape[0] for arr in arrays)
    b15 = []
    for array in arrays:
        b16 = np.zeros((b14, b13))
        b16[:array.shape[0]] = array
        b15.append(b16)
    return np.array(b15)
def fonk9(trees, transformer, left_child, right_child):
    b17 = [fonk2(tree, transformer, left_child, right_child) for tree in trees]
    b17 = fonk8(b17)
    b17 = torch.Tensor(b17).transpose(1, 2)
    b18 = [fonk6(tree, left_child, right_child) for tree in trees]
    b18 = fonk8(b18)
    b18 = torch.Tensor(b18).long()
    return b17, b18