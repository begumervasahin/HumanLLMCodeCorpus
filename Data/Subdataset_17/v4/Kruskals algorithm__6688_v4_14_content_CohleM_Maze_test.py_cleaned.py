import random
from collections import defaultdict
def create_grid_and_edges(grid_size=9):
    edges = []
    tree = defaultdict(list)
    node_id = 0
    for x in range(grid_size):
        for y in range(grid_size):
            tree[node_id].append((x, y))
            node_id += 1
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if abs(dx) == abs(dy):
                        continue
                    neighbor = (x + dx, y + dy)
                    if 0 <= neighbor[0] < grid_size and 0 <= neighbor[1] < grid_size:
                        edge = sorted([(x, y), neighbor])
                        if edge not in edges:
                            edges.append(edge)
    return tree, edges
def find_tree_containing_node(tree, node):
    for tree_id, nodes in tree.items():
        if node in nodes:
            return tree_id, nodes
    return None, None
def merge_trees(tree, tree1_id, tree2_id):
    tree[tree1_id].extend(tree[tree2_id])
    tree.pop(tree2_id)
def main():
    tree, edges = create_grid_and_edges(grid_size=9)
    selected_edges = []
    while len(tree) > 1:
        random_index = random.randint(0, len(edges) - 1)
        selected_edge = edges[random_index]
        tree1_id, tree1_nodes = find_tree_containing_node(tree, selected_edge[0])
        tree2_id, tree2_nodes = find_tree_containing_node(tree, selected_edge[1])
        if tree1_id == tree2_id:
            continue
        print(f"Connecting edge: {selected_edge}")
        print(f"Tree {tree1_id} before merge: {tree1_nodes}")
        print(f"Tree {tree2_id} before merge: {tree2_nodes}")
        merge_trees(tree, tree1_id, tree2_id)
        edges.pop(random_index)
        selected_edges.append(random_index)
        for nodes in tree.values():
            print(nodes)
        print(f"Remaining edges: {len(edges)}, Remaining trees: {len(tree)}")
        print()
    for tree_id, nodes in tree.items():
        print(f"Tree {tree_id}: {nodes}")
if __name__ == "__main__":
    main()