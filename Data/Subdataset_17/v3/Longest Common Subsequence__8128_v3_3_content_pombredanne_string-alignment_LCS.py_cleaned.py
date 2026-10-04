def longest_common_subsequence(s1, s2):
    num_rows = len(s2) + 1
    num_cols = len(s1) + 1
    costs = create_table(num_rows, num_cols, 0)
    directions = create_table(num_rows, num_cols, "A")
    initialize_tables(directions, num_rows, num_cols)
    max_row, max_col, max_val = fill_tables(costs, directions, s1, s2, num_rows, num_cols)
    print_table(costs, "costs.txt")
    print_table(directions, "directions.txt")
    align_sequences(directions, s1, s2, max_row, max_col, "alignment.txt")
    return costs[max_row][max_col]
def create_table(num_rows, num_cols, value):
    return [[value for _ in range(num_cols)] for _ in range(num_rows)]
def initialize_tables(directions, num_rows, num_cols):
    for i in range(num_cols):
        directions[0][i] = "F"
    for j in range(1, num_rows):
        directions[j][0] = "F"
def fill_tables(costs, directions, s1, s2, num_rows, num_cols):
    max_row, max_col, max_val = 0, 0, 0
    for y in range(1, num_rows):
        for x in range(1, num_cols):
            val_top = costs[y - 1][x]
            val_left = costs[y][x - 1]
            val_diag = costs[y - 1][x - 1] + 1 if s1[x - 1] == s2[y - 1] else -1
            val = max(val_top, val_left, val_diag)
            costs[y][x] = val
            if val > max_val:
                max_val = val
                max_row = y
                max_col = x
            directions[y][x] = determine_direction(val, val_left, val_diag)
    return max_row, max_col, max_val
def determine_direction(val, val_left, val_diag):
    if val == val_left:
        return "L"
    elif val == val_diag:
        return "D"
    else:
        return "T"
def print_table(table, filename):
    with open(filename, 'w') as file:
        for row in table:
            file.write("\t".join(map(str, row)) + "\n")
def align_sequences(directions, s1, s2, row, col, filename):
    lcs = ""
    x, y = col, row
    while directions[y][x] != "F":
        if directions[y][x] == "T":
            y -= 1
        elif directions[y][x] == "L":
            x -= 1
        elif directions[y][x] == "D":
            lcs = s1[x - 1] + lcs
            x -= 1
            y -= 1
    with open(filename, 'w') as file:
        for i in range(0, len(lcs), 50):
            file.write(lcs[i:i + 50] + "\n")
if __name__ == "__main__":
    s1 = "AGCGTCTA"
    s2 = "TGCATCTCG"
    optimal_score = longest_common_subsequence(s1, s2)
    print(s1)
    print(s2)
    print(f"LCS Score: {optimal_score}")