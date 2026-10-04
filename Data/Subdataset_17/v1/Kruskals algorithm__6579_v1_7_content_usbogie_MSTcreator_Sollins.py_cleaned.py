import copy
from Node import Node
def run_sollins(trees):
    MSTs = []
    for tree in trees:
        MSTs.append(run_sollins_on_tree(tree))
    return MSTs
def run_sollins_on_tree(tree):
    subtrees = []
    tree_to_mst = {}
    mst_to_tree = {}
    for n in tree:
        t = []
        m = copy.copy(n)
        m.adjList = {}
        tree_to_mst[n] = m
        mst_to_tree[m] = n
        t.append(m)
        subtrees.append(t)
    while len(subtrees) > 1:
        subtrees = run_phase(subtrees, tree, tree_to_mst, mst_to_tree)
    return subtrees.pop(0)
def run_phase(subtrees, tree, tree_to_mst, mst_to_tree):
    for subtree in subtrees:
        child = None
        lowest_weight = float('inf')
        parent = None
        for n in subtree:
            tree_node = mst_to_tree[n]
            for neighbor, weight in tree_node.adjList.items():
                temp = tree_to_mst[neighbor]
                if temp not in subtree and weight < lowest_weight:
                    lowest_weight = weight
                    child = temp
                    parent = n
        if parent and child:
            combine_components(subtrees, subtree, parent, child, lowest_weight)
    return subtrees
def combine_components(subtrees, subtree, parent, child, lowest_weight):
    child_subtree = next((sub for sub in subtrees if child in sub), None)
    if child_subtree:
        parent.adjList[child] = lowest_weight
        child.adjList[parent] = lowest_weight
        for node in subtree:
            child_subtree.append(node)
        subtrees.remove(subtree)
    return subtrees