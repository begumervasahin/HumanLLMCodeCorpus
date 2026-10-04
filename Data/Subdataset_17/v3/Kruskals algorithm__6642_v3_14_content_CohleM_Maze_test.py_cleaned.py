import random
from collections import defaultdict
def create_grid_and_edges(size=9):
    edges = []
    tree = defaultdict(list)
    node_id = 0
    for x in range(size):
        for y in range(size):
            tree[node_id].append((x, y))
            node_id += 1
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if abs(dx) == abs(dy):
                        continue
                    neighbor = (x + dx, y + dy)
                    if 0 <= neighbor[0] < size and 0 <= neighbor[1] < size:
                        edge = sorted([(x, y), neighbor])
                        if edge not in edges:
                            edges.append(edge)
    return tree, edges
def find_trees_containing_edge(tree, edge):
    tree1, tree2 = None, None
    for tree_id, nodes in tree.items():
        if edge[0] in nodes:
            tree1 = tree_id
        if edge[1] in nodes:
            tree2 = tree_id
        if tree1 is not None and tree2 is not None:
            break
    return tree1, tree2
def merge_trees(tree, tree1_id, tree2_id):
    tree[tree1_id].extend(tree[tree2_id])
    tree.pop(tree2_id)
def main():
    tree, edges = create_grid_and_edges(size=9)
    while len(tree) > 1:
        random_index = random.randint(0, len(edges) - 1)
        selected_edge = edges[random_index]
        tree1_id, tree2_id = find_trees_containing_edge(tree, selected_edge)
        if tree1_id == tree2_id:
            continue
        print(f"Connecting edge: {selected_edge}")
        print(f"Before merging, tree {tree1_id}: {tree[tree1_id]}")
        print(f"Before merging, tree {tree2_id}: {tree[tree2_id]}")
        merge_trees(tree, tree1_id, tree2_id)
        edges.pop(random_index)
        print(f"Remaining edges: {len(edges)}, Remaining trees: {len(tree)}")
        print()
    for tree_id, nodes in tree.items():
        print(f"Tree {tree_id}: {nodes}")
if __name__ == "__main__":
    main()