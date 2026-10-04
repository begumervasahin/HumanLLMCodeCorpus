from BSTTree import BSTTree
def find_optimal_tree_ordering(beta_list, alpha_list):
    n = len(beta_list)
    exp_table = [[float("inf")] * (n + 1) for _ in range(n + 1)]
    weight_table = [[0] * (n + 1) for _ in range(n + 1)]
    root_table = [[None] * n for _ in range(n)]
    for i in range(n + 1):
        exp_table[i][i] = alpha_list[i]
        weight_table[i][i] = alpha_list[i]
    for length in range(1, n + 1):
        for i in range(n - length):
            j = i + length
            weight_table[i][j] = weight_table[i][j - 1] + beta_list[j - 1] + alpha_list[j]
            for root in range(i, j):
                cost = exp_table[i][root] + exp_table[root + 1][j] + weight_table[i][j]
                if cost < exp_table[i][j]:
                    exp_table[i][j] = cost
                    root_table[i][j - 1] = root
    return exp_table, root_table
def print_table(table, title):
    print(f"\n{title}:")
    for row in table:
        print(row)
def construct_tree_inline(root_table, key_list):
    def construct_subtree(i, j):
        if i > j:
            return None
        root_index = root_table[i][j]
        root = BSTTree(key_list[root_index])
        root.left = construct_subtree(i, root_index - 1)
        root.right = construct_subtree(root_index + 1, j)
        return root
    return construct_subtree(0, len(root_table) - 1)
if __name__ == "__main__":
    beta_list = [0.15, 0.10, 0.05, 0.10, 0.20]
    alpha_list = [0.05, 0.10, 0.05, 0.05, 0.10, 0.05]
    key_list = ['A', 'B', 'C', 'D', 'E']
    exp_table, root_table = find_optimal_tree_ordering(beta_list, alpha_list)
    print_table(exp_table, "Expected Cost Table")
    print_table(root_table, "Root Table")
    bst_root = construct_tree_inline(root_table, key_list)
    print("\nOptimal Binary Search Tree constructed.")