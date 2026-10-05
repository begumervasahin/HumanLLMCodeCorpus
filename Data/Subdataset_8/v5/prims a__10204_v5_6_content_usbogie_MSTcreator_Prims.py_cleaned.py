import copy
from Node import Node
def run_prims(trees):
    minimum_spanning_trees = []
    for tree in trees:
        minimum_spanning_trees.append(build_minimum_spanning_tree(tree))
    return minimum_spanning_trees
def build_minimum_spanning_tree(tree):
    mst_nodes = []
    tree_to_mst = {}
    mst_to_tree = {}
    for node in tree:
        copied_node = copy.copy(node)
        copied_node.adjList = {}
        tree_to_mst[node] = copied_node
        mst_to_tree[copied_node] = node
    first_node = tree_to_mst[next(iter(tree))]
    mst_nodes.append(first_node)
    while len(mst_nodes) < len(tree):
        next_node = get_next_node(mst_nodes, tree, tree_to_mst, mst_to_tree)
        mst_nodes.append(next_node)
    return mst_nodes
def get_next_node(mst_nodes, tree, tree_to_mst, mst_to_tree):
    lowest_node = None
    lowest_weight = float('inf')
    parent = None
    tree_child = None
    for node in mst_nodes:
        tree_node = mst_to_tree[node]
        for adjacent_node, weight in tree_node.adjList.items():
            if (weight < lowest_weight) and (tree_to_mst[adjacent_node] not in mst_nodes):
                lowest_weight = weight
                lowest_node = tree_to_mst[adjacent_node]
                tree_child = adjacent_node
                parent = node
    if parent is not None and lowest_node is not None:
        tree_parent = mst_to_tree[parent]
        del tree_parent.adjList[tree_child]
        del tree_child.adjList[tree_parent]
        parent.adjList[lowest_node] = lowest_weight
        lowest_node.adjList[parent] = lowest_weight
    return lowest_node