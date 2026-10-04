import numpy as np
import torch
class TreeConvolutionError(Exception):
    pass
def is_leaf(node, left_child, right_child):
    has_left = left_child(node) is not None
    has_right = right_child(node) is not None
    if has_left != has_right:
        raise TreeConvolutionError("All nodes must have both a left and a right child or no children")
    return not has_left
def flatten_tree(root, transformer, left_child, right_child):
    if not callable(transformer):
        raise TreeConvolutionError("Transformer must be a function mapping a tree node to a vector")
    if not callable(left_child) or not callable(right_child):
        raise TreeConvolutionError("left_child and right_child must be functions mapping a tree node to its child, or None")
    accum = []
    def recurse(node):
        if is_leaf(node, left_child, right_child):
            accum.append(transformer(node))
            return
        accum.append(transformer(node))
        recurse(left_child(node))
        recurse(right_child(node))
    recurse(root)
    try:
        accum = [np.zeros(accum[0].shape)] + accum
    except:
        raise TreeConvolutionError("Output of transformer must have a .shape (e.g., numpy array)")
    return np.array(accum)
def preorder_indexes(root, left_child, right_child, idx=1):
    if not callable(left_child) or not callable(right_child):
        raise TreeConvolutionError("left_child and right_child must be functions mapping a tree node to its child, or None")
    if is_leaf(root, left_child, right_child):
        return idx
    def rightmost(tree):
        if isinstance(tree, tuple):
            return rightmost(tree[2])
        return tree
    left_subtree = preorder_indexes(left_child(root), left_child, right_child, idx=idx + 1)
    max_index_in_left = rightmost(left_subtree)
    right_subtree = preorder_indexes(right_child(root), left_child, right_child, idx=max_index_in_left + 1)
    return (idx, left_subtree, right_subtree)
def tree_conv_indexes(root, left_child, right_child):
    index_tree = preorder_indexes(root, left_child, right_child)
    def recurse(node):
        if isinstance(node, tuple):
            my_id = node[0]
            left_id = node[1][0] if isinstance(node[1], tuple) else node[1]
            right_id = node[2][0] if isinstance(node[2], tuple) else node[2]
            yield [my_id, left_id, right_id]
            yield from recurse(node[1])
            yield from recurse(node[2])
        else:
            yield [node, 0, 0]
    return np.array(list(recurse(index_tree))).flatten().reshape(-1, 1)
def pad_and_combine(arrays):
    if not arrays:
        raise TreeConvolutionError("No arrays provided for padding and combining")
    second_dim = arrays[0].shape[1]
    for arr in arrays[1:]:
        if arr.shape[1] != second_dim:
            raise TreeConvolutionError("All arrays must have the same number of columns")
    max_first_dim = max(arr.shape[0] for arr in arrays)
    padded_arrays = []
    for arr in arrays:
        padded = np.zeros((max_first_dim, second_dim))
        padded[:arr.shape[0]] = arr
        padded_arrays.append(padded)
    return np.array(padded_arrays)
def prepare_trees(trees, transformer, left_child, right_child):
    flat_trees = [flatten_tree(tree, transformer, left_child, right_child) for tree in trees]
    flat_trees = pad_and_combine(flat_trees)
    flat_trees = torch.Tensor(flat_trees).transpose(1, 2)
    indexes = [tree_conv_indexes(tree, left_child, right_child) for tree in trees]
    indexes = pad_and_combine(indexes)
    indexes = torch.Tensor(indexes).long()
    return flat_trees, indexes
if __name__ == "__main__":
    class SimpleNode:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.left = left
            self.right = right
    def transformer(node):
        return np.array([node.value])
    def left_child(node):
        return node.left
    def right_child(node):
        return node.right
    tree = SimpleNode(1, SimpleNode(2, SimpleNode(4), SimpleNode(5)), SimpleNode(3))
    flat_trees, indexes = prepare_trees([tree], transformer, left_child, right_child)
    print("Flattened Trees:")
    print(flat_trees)
    print("Tree Convolution Indexes:")
    print(indexes)