import copy
from Node import Node
def find_minimum_spanning_trees(trees):
    minimum_spanning_trees = []
    for tree in trees:
        minimum_spanning_trees.append(run_sollins_on_tree(tree))
    return minimum_spanning_trees
def run_sollins_on_tree(tree):
    subtrees = []
    tree_to_mst = {}
    mst_to_tree = {}
    for node in tree:
        temp_tree_node = list()
        mst_node = copy.copy(node)
        mst_node.adjList = {}
        tree_to_mst[node] = mst_node
        mst_to_tree[mst_node] = node
        temp_tree_node.append(mst_node)
        subtrees.append(temp_tree_node)
    while len(subtrees) != 1:
        subtrees = run_phase(subtrees, tree, tree_to_mst, mst_to_tree)
    return subtrees.pop(0)
def run_phase(subtrees, tree, tree_to_mst, mst_to_tree):
    for subtree in subtrees:
        child = Node(0, 0, 0, {})
        lowest_weight = -1
        parent = Node(0, 0, 0, {})
        for n in subtree:
            tree_node = mst_to_tree[n]
            for p in tree_node.adjList:
                temp = tree_to_mst[p]
                if temp not in subtree and (tree_node.adjList[p] < lowest_weight or lowest_weight == -1):
                    lowest_weight = tree_node.adjList[p]
                    child = temp
                    parent = n
        combine_components(subtrees, subtree, parent, child, lowest_weight)
    return subtrees
def combine_components(subtrees, subtree, parent, child, lowest_weight):
    child_subtree = []
    for sub in subtrees:
        if child in sub:
            child_subtree = sub
    parent.adjList[child] = lowest_weight
    child.adjList[parent] = lowest_weight
    for y in subtree:
        child_subtree.append(y)
    subtrees.remove(subtree)
    return subtrees