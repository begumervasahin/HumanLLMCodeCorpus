import copy
from Node import Node
def run_sollins(trees):
    return [run_sollins_on_tree(tree) for tree in trees]
def run_sollins_on_tree(tree):
    subtrees = initialize_subtrees(tree)
    while len(subtrees) > 1:
        subtrees = run_phase(subtrees)
    return subtrees[0]
def initialize_subtrees(tree):
    tree_to_mst = {}
    mst_to_tree = {}
    subtrees = []
    for node in tree:
        mst_node = copy.copy(node)
        mst_node.adjList = {}
        tree_to_mst[node] = mst_node
        mst_to_tree[mst_node] = node
        subtrees.append([mst_node])
    return subtrees
def run_phase(subtrees):
    for subtree in subtrees:
        parent, child, weight = find_lightest_edge(subtree)
        if parent and child:
            combine_components(subtrees, subtree, parent, child, weight)
    return subtrees
def find_lightest_edge(subtree):
    lowest_weight = float('inf')
    parent, child = None, None
    for node in subtree:
        tree_node = mst_to_tree[node]
        for neighbor, weight in tree_node.adjList.items():
            mst_neighbor = tree_to_mst[neighbor]
            if mst_neighbor not in subtree and weight < lowest_weight:
                lowest_weight = weight
                parent, child = node, mst_neighbor
    return parent, child, lowest_weight
def combine_components(subtrees, subtree, parent, child, weight):
    child_subtree = next(sub for sub in subtrees if child in sub)
    if child_subtree:
        parent.adjList[child] = weight
        child.adjList[parent] = weight
        subtree.extend(child_subtree)
        subtrees.remove(child_subtree)