from BSTTree import BSTTree
def find_optimal_tree_ordering(beta_list, alpha_list, beta_len):
    exp_table = [[None] * (beta_len + 1) for _ in range(beta_len + 1)]
    weight_table = [[None] * (beta_len + 1) for _ in range(beta_len + 1)]
    root_table = [[None] * beta_len for _ in range(beta_len)]
    for x in range(beta_len + 1):
        exp_table[x][x] = alpha_list[x]
        weight_table[x][x] = alpha_list[x]
    for y in range(1, beta_len + 1):
        for i in range(beta_len - y + 1):
            j = i + y
            exp_table[i][j] = float("inf")
            weight_table[i][j] = weight_table[i][j - 1] + beta_list[j - 1] + alpha_list[j]
            for root in range(i, j):
                t = exp_table[i][root] + exp_table[root + 1][j] + weight_table[i][j]
                if t < exp_table[i][j]:
                    exp_table[i][j] = t
                    root_table[i][j - 1] = root
    return exp_table, root_table
def print_table(table):
    for row in table:
        print(row)
def construct_tree_inline(root_table, key_list):
    stack = [(0, len(root_table) - 1, None)]
    root = None
    while stack:
        i, j, parent = stack.pop()
        root_index = root_table[i][j]
        node = BSTTree(key_list[root_index])
        if root is None:
            root = node
        elif node.value < parent.value:
            parent.left = node
        else:
            parent.right = node
        if root_index + 1 <= j:
            stack.append((root_index + 1, j, node))
        if i <= root_index - 1:
            stack.append((i, root_index - 1, node))
    return root