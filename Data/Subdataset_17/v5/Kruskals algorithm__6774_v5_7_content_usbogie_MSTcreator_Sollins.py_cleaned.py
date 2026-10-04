import copy
from Node import Node
def run_sollins(trees):
    return [run_sollins_on_tree(tree) for tree in trees]
def run_sollins_on_tree(tree):
    subtrees = initialize_subtrees(tree)
    tree_to_mst, mst_to_tree = create_mappings(tree, subtrees)
    while len(subtrees) > 1:
        subtrees = run_phase(subtrees, tree, tree_to_mst, mst_to_tree)
    return subtrees[0]
def initialize_subtrees(tree):
    return [[copy.copy(node)] for node in tree]
def create_mappings(tree, subtrees):
    tree_to_mst = {}
    mst_to_tree = {}
    for subtree in subtrees:
        mst_node = subtree[0]
        mst_node.adjList = {}
        original_node = next(node for node in tree if node == mst_node)
        tree_to_mst[original_node] = mst_node
        mst_to_tree[mst_node] = original_node
    return tree_to_mst, mst_to_tree
def run_phase(subtrees, tree, tree_to_mst, mst_to_tree):
    for subtree in subtrees:
        parent, child, lowest_weight = find_lightest_edge(subtree, tree_to_mst, mst_to_tree)
        if parent and child:
            merge_subtrees(subtrees, subtree, parent, child, lowest_weight)
    return subtrees
def find_lightest_edge(subtree, tree_to_mst, mst_to_tree):
    lowest_weight = float('inf')
    selected_parent = selected_child = None
    for mst_node in subtree:
        original_node = mst_to_tree[mst_node]
        for neighbor, weight in original_node.adjList.items():
            mst_neighbor = tree_to_mst[neighbor]
            if mst_neighbor not in subtree and weight < lowest_weight:
                lowest_weight = weight
                selected_parent = mst_node
                selected_child = mst_neighbor
    return selected_parent, selected_child, lowest_weight
def merge_subtrees(subtrees, subtree, parent, child, weight):
    child_subtree = next(sub for sub in subtrees if child in sub)
    parent.adjList[child] = weight
    child.adjList[parent] = weight
    child_subtree.extend(subtree)
    subtrees.remove(subtree)