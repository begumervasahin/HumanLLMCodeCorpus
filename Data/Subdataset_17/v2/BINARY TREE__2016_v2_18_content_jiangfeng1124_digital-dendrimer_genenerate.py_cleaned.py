import sys
from copy import deepcopy
from anytree import Node, RenderTree
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('Agg')
def read_data(path: str) -> list[list[str]]:
    nodes = []
    with open(path, 'r') as file:
        for line in file:
            nodes.append(line.strip().split())
    nodes.reverse()
    return nodes
def build_tree(nodes: list[list[str]]) -> tuple[list[list[Node]], list[tuple[int, int]]]:
    depth = len(nodes)
    assert len(nodes[0]) == 1, "Root node must be a single node"
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
            if n_cur == n_pre:
                for j in range(n_cur):
                    layer.append(Node(nodes[i][j], parent=tree[i - 1][j]))
                    if i == depth - 1:
                        leaves.append((i, j))
            elif n_cur == 2 * n_pre:
                for j in range(n_cur):
                    layer.append(Node(nodes[i][j], parent=tree[i - 1][j
                    if i == depth - 1:
                        leaves.append((i, j))
            tree.append(layer)
    return tree, leaves
def update_tree(tree: list[list[Node]], i: int, j: int) -> list[list[Node]]:
    dup_tree = deepcopy(tree)
    node = dup_tree[i][j]
    node.parent = None
    return dup_tree
def traverse(tree: list[list[Node]], leaves: list[tuple[int, int]], path: str):
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
    plt.imshow(data, cmap='gray', interpolation='nearest')
    plt.axis('off')
    plt.savefig(filename, bbox_inches='tight')
    plt.close()
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python generate.py [input_file] [output_file] [image_file]", file=sys.stderr)
        sys.exit(-1)
    input_file, output_file, image_file = sys.argv[1], sys.argv[2], sys.argv[3]
    nodes = read_data(input_file)
    tree, leaves = build_tree(nodes)
    paths = set()
    with open(output_file, "w") as fw:
        traverse(tree, leaves, "")
        print("Input tree:")
        display_tree(tree[0][0])
        sorted_paths = sorted(list(paths), reverse=True)
        reversed_paths = [path[::-1] for path in sorted_paths]
        print(f"\nPossible paths written to {output_file}\n")
        for path in reversed_paths:
            fw.write(f"{path}\n")
    matrix = np.asarray([list(map(int, list(path))) for path in reversed_paths])
    matrix = 1 - matrix
    save_image(matrix, image_file)