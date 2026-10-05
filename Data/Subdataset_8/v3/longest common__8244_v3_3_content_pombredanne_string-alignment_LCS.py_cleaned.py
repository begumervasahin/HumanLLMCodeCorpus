def longest_common_subsequence(s1, s2):
    num_rows = len(s2) + 1
    num_cols = len(s1) + 1
    costs = create_table(num_rows, num_cols, 0)
    directions = create_table(num_rows, num_cols, "A")
    initialize_tables(costs, directions)
    max_row, max_col, max_val = calculate_scores(costs, directions, s1, s2)
    output_tables(costs, directions)
    align_sequences(directions, s1, s2, max_row, max_col, "alignment.txt")
    return max_val
def create_table(num_rows, num_cols, value):
    return [[value] * num_cols for _ in range(num_rows)]
def initialize_tables(costs, directions):
    num_rows, num_cols = len(costs), len(costs[0])
    for i in range(num_cols):
        costs[0][i] = 0
        directions[0][i] = "F"
    for j in range(1, num_rows):
        costs[j][0] = 0
        directions[j][0] = "F"
def calculate_scores(costs, directions, s1, s2):
    max_row, max_col, max_val = 0, 0, 0
    for y in range(1, len(costs)):
        for x in range(1, len(costs[0])):
            val_top = costs[y - 1][x]
            val_left = costs[y][x - 1]
            val_diag = costs[y - 1][x - 1] + 1 if s1[x - 1] == s2[y - 1] else -1
            val = max(val_top, val_left, val_diag)
            costs[y][x] = val
            if val > max_val:
                max_val, max_row, max_col = val, y, x
            directions[y][x] = "L" if val == val_left else ("D" if val == val_diag else "T")
    return max_row, max_col, max_val
def output_tables(costs, directions):
    print_table(costs, "costs.txt")
    print_table(directions, "directions.txt")
def align_sequences(directions, s1, s2, row, col, filename):
    with open(filename, 'w') as file:
        x, y = col, row
        lcs = ""
        while directions[y][x] != "F":
            if directions[y][x] == "L":
                x -= 1
            elif directions[y][x] == "D":
                lcs = s1[x - 1] + lcs
                x, y = x - 1, y - 1
            else:
                y -= 1
        for i in range(0, len(lcs), 50):
            file.write(lcs[i:i + 50] + "\n")
s = "AGCGTCTA"
t = "TGCATCTCG"
optimal_score = longest_common_subsequence(s, t)
print(s)
print(t)
print("LCS Score: " + str(optimal_score))