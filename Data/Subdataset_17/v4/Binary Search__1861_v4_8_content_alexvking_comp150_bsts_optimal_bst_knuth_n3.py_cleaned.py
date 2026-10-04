from BSTTree import BSTTree
def find_optimal_tree_ordering(beta_list, alpha_list, beta_len):
    exp_table = [[None for _ in range(beta_len + 1)] for _ in range(beta_len + 1)]
    weight_table = [[None for _ in range(beta_len + 1)] for _ in range(beta_len + 1)]
    root_table = [[None for _ in range(beta_len)] for _ in range(beta_len)]
    for x in range(beta_len + 1):
        exp_table[x][x] = alpha_list[x]
        weight_table[x][x] = alpha_list[x]
    for length in range(1, beta_len + 1):
        for i in range(beta_len - length + 1):
            j = i + length
            exp_table[i][j] = float("inf")
            weight_table[i][j] = weight_table[i][j - 1] + beta_list[j - 1] + alpha_list[j]
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
    i, j = 0, len(root_table) - 1
    root_index = root_table[i][j]
    root = BSTTree(key_list[root_index])
    node_stack = []
    if root_index + 1 <= j:
        node_stack.append((root_index + 1, j, root))
    if i <= root_index - 1:
        node_stack.append((i, root_index - 1, root))
    while node_stack:
        i, j, parent = node_stack.pop()
        next_root_index = root_table[i][j]
        node = BSTTree(key_list[next_root_index])
        if node.value < parent.value:
            parent.left = node
        else:
            parent.right = node
        if next_root_index + 1 <= j:
            node_stack.append((next_root_index + 1, j, node))
        if i <= next_root_index - 1:
            node_stack.append((i, next_root_index - 1, node))
    return root