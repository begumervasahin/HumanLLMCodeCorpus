import copy
from Node import Node
def run_sollins(trees):
    return [run_sollins_on_tree(tree) for tree in trees]
def run_sollins_on_tree(tree):
    subtrees = []
    tree_to_mst = {}
    mst_to_tree = {}
    for node in tree:
        mst_node = copy.copy(node)
        mst_node.adjList = {}
        tree_to_mst[node] = mst_node
        mst_to_tree[mst_node] = node
        subtrees.append([mst_node])
    while len(subtrees) > 1:
        subtrees = run_phase(subtrees, tree, tree_to_mst, mst_to_tree)
    return subtrees[0]
def run_phase(subtrees, tree, tree_to_mst, mst_to_tree):
    for subtree in subtrees:
        parent, child, lowest_weight = find_lightest_edge(subtree, tree_to_mst, mst_to_tree)
        if parent and child:
            combine_components(subtrees, subtree, parent, child, lowest_weight)
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
def combine_components(subtrees, subtree, parent, child, weight):
    child_subtree = next(sub for sub in subtrees if child in sub)
    parent.adjList[child] = weight
    child.adjList[parent] = weight
    child_subtree.extend(subtree)
    subtrees.remove(subtree)