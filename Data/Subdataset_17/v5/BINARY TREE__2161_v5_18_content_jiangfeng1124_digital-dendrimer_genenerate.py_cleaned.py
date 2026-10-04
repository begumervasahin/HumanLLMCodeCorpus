import sys
from copy import deepcopy
from anytree import Node, RenderTree
import numpy as np
import matplotlib.pyplot as plt
def read_data(path: str) -> list:
    nodes = []
    with open(path, 'r') as file:
        for line in file:
            layer = line.strip().split()
            nodes.append(layer)
    nodes.reverse()
    return nodes
def build_tree(nodes: list) -> tuple:
    depth = len(nodes)
    assert len(nodes[0]) == 1, "Root node must be a single element."
    tree = []
    leaves = []
    for i in range(depth):
        if i == 0:
            root = Node(nodes[0][0])
            tree.append([root])
        else:
            n_pre = len(nodes[i - 1])
            n_cur = len(nodes[i])
            assert n_cur == n_pre or n_cur == 2 * n_pre, f"Incorrect number of nodes in layer: {i}"
            layer = []
            for j in range(n_cur):
                parent_index = j if n_cur == n_pre else j
                layer.append(Node(nodes[i][j], parent=tree[i - 1][parent_index]))
                if i == depth - 1:
                    leaves.append((i, j))
            tree.append(layer)
    return tree, leaves
def update_tree(tree: list, i: int, j: int) -> list:
    dup_tree = deepcopy(tree)
    layer = dup_tree[i]
    node = layer[j]
    node.parent = None
    return dup_tree
def traverse(tree: list, leaves: list, path: str):
    for i, j in leaves:
        node = tree[i][j]
        if node.is_leaf:
            if node.is_root:
                paths.add(path + node.name)
                if len(paths) % 100 == 0:
                    print(len(paths))
                    sys.stdout.flush()
                if len(paths) % 800 == 0:
                    for path in paths:
                        fw.write(f"{path}\n")
                    fw.flush()
                    sys.exit(-1)
            else:
                mod_leaves = deepcopy(leaves)
                if len(node.parent.children) == 1:
                    mod_leaves.append((i - 1, j if len(tree[i]) == len(tree[i - 1]) else j
                mod_leaves.remove((i, j))
                traverse(update_tree(tree, i, j), mod_leaves, path + node.name)
def display_tree(root: Node):
    for pre, fill, node in RenderTree(root):
        print(f"{pre}{node.name}")
def save_image(data: np.ndarray, filename: str):
    fig, ax = plt.subplots()
    ax.set_axis_off()
    ax.imshow(data, cmap='gray', interpolation='nearest')
    plt.savefig(filename, bbox_inches='tight')
    plt.close()
def main(input_file: str, output_file: str, image_file: str):
    nodes = read_data(input_file)
    tree, leaves = build_tree(nodes)
    global paths
    paths = set()
    global fw
    fw = open(output_file, "w")
    traverse(tree, leaves, "")
    print("Input tree:")
    display_tree(tree[0][0])
    sorted_paths = sorted(paths, reverse=True)
    reversed_paths = [path[::-1] for path in sorted_paths]
    with open(output_file, "w") as fw:
        for path in reversed_paths:
            fw.write(f"{path}\n")
    matrix = np.array([list(map(int, list(e))) for e in reversed_paths])
    matrix = 1 - matrix
    plt.imshow(matrix, cmap='gray', interpolation='none')
    plt.savefig(image_file, bbox_inches='tight')
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python generate.py [input_file] [output_file] [image_file]", file=sys.stderr)
        sys.exit(-1)
    main(sys.argv[1], sys.argv[2], sys.argv[3])