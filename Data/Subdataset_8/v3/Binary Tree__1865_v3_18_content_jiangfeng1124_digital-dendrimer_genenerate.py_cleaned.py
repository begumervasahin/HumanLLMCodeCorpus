from anytree import Node, RenderTree
from copy import deepcopy
import sys
import numpy as np
import matplotlib.pyplot as plt
def read_data(path):
    nodes = []
    with open(path, 'r') as file:
        for line in file:
            layer = line.strip().split()
            nodes.append(layer)
    nodes.reverse()
    return nodes
def build_tree(nodes):
    depth = len(nodes)
    assert len(nodes[0]) == 1
    tree = []
    leaves = []
    for i in range(depth):
        if i == 0:
            root = Node(nodes[0][0])
            tree.append([root])
        else:
            n_previous = len(nodes[i-1])
            n_current = len(nodes[i])
            assert n_current in (n_previous, 2 * n_previous)
            layer = []
            for j in range(n_current):
                parent_index = j
                layer.append(Node(nodes[i][j], parent=tree[i-1][parent_index]))
                if i == depth - 1:
                    leaves.append((i, j))
            tree.append(layer)
    return tree, leaves
def update_tree(tree, i, j):
    dup_tree = deepcopy(tree)
    dup_tree[i][j].parent = None
    return dup_tree
def traverse(tree, leaves, path, fw):
    paths = set()
    for i, j in leaves:
        node = tree[i][j]
        if node.is_leaf:
            if node.is_root:
                paths.add(path + node.name)
                if len(paths) % 100 == 0:
                    print(len(paths))
                    sys.stdout.flush()
                if len(paths) % 800 == 0:
                    for p in paths:
                        fw.write("{}\n".format(p))
                    fw.flush()
                    sys.exit(-1)
            else:
                mod_leaves = deepcopy(leaves)
                parent_index = j
                mod_leaves.remove((i,j))
                mod_leaves.append((i-1, parent_index))
                traverse(update_tree(tree, i, j), mod_leaves, path + node.name, fw)
def display_tree(root):
    for pre, fill, node in RenderTree(root):
        print("%s%s" % (pre, node.name))
def save_image(data, filename):
    sizes = np.shape(data)
    fig = plt.figure()
    ax = plt.Axes(fig, [0., 0., 1., 1.])
    ax.set_axis_off()
    fig.add_axes(ax)
    img = ax.imshow(data, interpolation='nearest')
    img.set_cmap('gray')
    plt.savefig(filename, cmap='hot')
    plt.close()
if len(sys.argv) != 4:
    print("Usage: python generate.py [input_file] [output_file] [image_file]", file=sys.stderr)
    sys.exit(-1)
nodes = read_data(sys.argv[1])
tree, leaves = build_tree(nodes)
paths = set()
with open(sys.argv[2], "w") as fw:
    traverse(tree, leaves, "", fw)
print("Input tree:")
display_tree(tree[0][0])
print("\nPossible paths written to {}\n".format(sys.argv[2]))
matrix = np.asarray([list(map(int, list(e))) for e in paths])
matrix = 1 - matrix
plt.imshow(matrix, cmap='gray', interpolation='none')
plt.savefig(sys.argv[3], bbox_inches='tight')