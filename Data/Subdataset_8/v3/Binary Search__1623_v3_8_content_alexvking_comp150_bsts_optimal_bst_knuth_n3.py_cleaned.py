class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
def find_optimal_tree_ordering(beta_list, alpha_list):
    beta_len = len(beta_list)
    exp_table = [[None] * (beta_len + 1) for _ in range(beta_len + 1)]
    weight_table = [[None] * (beta_len + 1) for _ in range(beta_len + 1)]
    root_table = [[None] * beta_len for _ in range(beta_len)]
    for x in range(beta_len + 1):
        exp_table[x][x] = alpha_list[x]
        weight_table[x][x] = alpha_list[x]
    for y in range(beta_len + 1):
        for i in range(beta_len - y):
            j = i + y + 1
            exp_table[i][j] = float("inf")
            weight_table[i][j] = weight_table[i][j - 1] + beta_list[j - 1] + alpha_list[j]
            for root in range(i, j):
                t = exp_table[i][root] + exp_table[root + 1][j] + weight_table[i][j]
                if t < exp_table[i][j]:
                    exp_table[i][j] = t
                    root_table[i][j - 1] = root
    return exp_table, root_table
def construct_tree_from_root_table(root_table, key_list):
    def build_tree(i, j):
        if i > j:
            return None
        root_index = root_table[i][j]
        root = TreeNode(key_list[root_index])
        root.left = build_tree(i, root_index - 1)
        root.right = build_tree(root_index + 1, j)
        return root
    return build_tree(0, len(root_table) - 1)
def print_table(table):
    for row in table:
        print(row)
beta_list = [1, 2, 3]
alpha_list = [0, 0, 0, 0]
exp_table, root_table = find_optimal_tree_ordering(beta_list, alpha_list)
print("Exp Table:")
print_table(exp_table)
print("\nRoot Table:")
print_table(root_table)
key_list = [10, 20, 30]
root = construct_tree_from_root_table(root_table, key_list)
print("\nConstructed Tree:")
print("Root Value:", root.value)
print("Left Child:", root.left.value if root.left else None)
print("Right Child:", root.right.value if root.right else None)