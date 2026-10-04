from BSTTree import BSTTree
def find_optimal_tree_ordering(beta_list, alpha_list, beta_len):
    exp_table = [[None] * (beta_len + 1) for _ in range(beta_len + 1)]
    weight_table = [[None] * (beta_len + 1) for _ in range(beta_len + 1)]
    root_table = [[None] * beta_len for _ in range(beta_len)]
    for i in range(beta_len + 1):
        exp_table[i][i] = alpha_list[i]
        weight_table[i][i] = alpha_list[i]
    for length in range(1, beta_len + 1):
        for i in range(beta_len - length + 1):
            j = i + length
            weight_table[i][j] = weight_table[i][j - 1] + beta_list[j - 1] + alpha_list[j]
            exp_table[i][j] = float("inf")
            for root in range(i, j):
                cost = exp_table[i][root] + exp_table[root + 1][j] + weight_table[i][j]
                if cost < exp_table[i][j]:
                    exp_table[i][j] = cost
                    root_table[i][j - 1] = root
    return exp_table, root_table
def print_table(table):
    for row in table:
        print(row)
def construct_tree_inline(root_table, key_list):
    def build_subtree(i, j, parent=None, is_left=True):
        if i > j:
            return
        root_index = root_table[i][j]
        node = BSTTree(key_list[root_index])
        if parent:
            if is_left:
                parent.left = node
            else:
                parent.right = node
        build_subtree(i, root_index - 1, node, is_left=True)
        build_subtree(root_index + 1, j, node, is_left=False)
        return node
    root = build_subtree(0, len(root_table) - 1)
    return root
