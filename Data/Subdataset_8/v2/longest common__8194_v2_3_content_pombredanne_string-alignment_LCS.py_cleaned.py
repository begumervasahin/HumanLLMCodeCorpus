def longest_common_subsequence(s1, s2):
    num_rows = len(s2) + 1
    num_cols = len(s1) + 1
    costs = create_table(num_rows, num_cols, 0)
    directions = create_table(num_rows, num_cols, "A")
    for i in range(num_cols):
        costs[0][i] = 0
        directions[0][i] = "F"
    for j in range(1, num_rows):
        costs[j][0] = 0
        directions[j][0] = "F"
    max_row = 0
    max_col = 0
    max_val = 0
    for y in range(1, num_rows):
        for x in range(1, num_cols):
            val_top = costs[y - 1][x]
            val_left = costs[y][x - 1]
            if s1[x - 1] == s2[y - 1]:
                val_diag = costs[y - 1][x - 1] + 1
            else:
                val_diag = -1
            val = max(val_top, val_left, val_diag)
            costs[y][x] = val
            if val > max_val:
                max_val = val
                max_row = y
                max_col = x
            if val == val_left:
                directions[y][x] = "L"
            elif val == val_diag:
                directions[y][x] = "D"
            else:
                directions[y][x] = "T"
    print_table(costs, "costs.txt")
    print_table(directions, "directions.txt")
    align(directions, s1, s2, max_row, max_col, "alignment.txt")
    return costs[max_row][max_col]
def create_table(num_rows, num_cols, value):
    table = []
    for _ in range(num_rows):
        table.append([value] * num_cols)
    return table
def print_table(table, filename):
    with open(filename, 'w') as file:
        for row in table:
            file.write('\t'.join(map(str, row)) + '\n')
def align(direction, s1, s2, row, col, filename):
    with open(filename, 'w') as file:
        x = col
        y = row
        current_dir = direction[y][x]
        lcs = ""
        while current_dir != "F":
            if direction[y][x] == "T":
                y -= 1
            elif direction[y][x] == "L":
                x -= 1
            elif direction[y][x] == "D":
                lcs = s1[x - 1] + lcs
                x -= 1
                y -= 1
            current_dir = direction[y][x]
        for i in range(0, len(lcs), 50):
            file.write(lcs[i:i + 50] + "\n")
s = "AGCGTCTA"
t = "TGCATCTCG"
optimal_score = longest_common_subsequence(s, t)
print(s)
print(t)
print("LCS Score: " + str(optimal_score))