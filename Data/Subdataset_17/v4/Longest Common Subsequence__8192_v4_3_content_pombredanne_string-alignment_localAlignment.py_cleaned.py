def local_alignment_score(s1, s2):
    MATCH = 5
    MISMATCH = -4
    GAP = -6
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
    max_value = 0
    max_row_pos = 0
    max_col_pos = 0
    for y in range(1, num_rows):
        for x in range(1, num_cols):
            val_top = costs[y-1][x] + GAP
            val_left = costs[y][x-1] + GAP
            if s1[x-1] == s2[y-1]:
                val_diag = costs[y-1][x-1] + MATCH
            else:
                val_diag = costs[y-1][x-1] + MISMATCH
            val = max(val_top, val_left, val_diag, 0)
            if val > max_value:
                max_value = val
                max_row_pos = y
                max_col_pos = x
            costs[y][x] = val
            if val == 0:
                directions[y][x] = "F"
            elif val == val_left:
                directions[y][x] = "L"
            elif val == val_diag:
                directions[y][x] = "D"
            else:
                directions[y][x] = "T"
    print_table(costs, "costs.txt")
    print_table(directions, "directions.txt")
    align(directions, s1, s2, max_row_pos, max_col_pos, "alignment.txt")
    return costs[max_row_pos][max_col_pos]
def create_table(num_rows, num_cols, value):
    return [[value for _ in range(num_cols)] for _ in range(num_rows)]
def print_table(table, filename):
    with open(filename, 'w') as file:
        for row in table:
            file.write("\t".join(map(str, row)) + "\n")
def align(directions, s1, s2, row, col, filename):
    top_seq = ""
    bot_seq = ""
    x, y = col, row
    while directions[y][x] != "F":
        if directions[y][x] == "T":
            top_seq = "-" + top_seq
            bot_seq = s2[y-1] + bot_seq
            y -= 1
        elif directions[y][x] == "L":
            top_seq = s1[x-1] + top_seq
            bot_seq = "-" + bot_seq
            x -= 1
        elif directions[y][x] == "D":
            top_seq = s1[x-1] + top_seq
            bot_seq = s2[y-1] + bot_seq
            x -= 1
            y -= 1
    with open(filename, 'w') as file:
        for i in range(0, len(top_seq), 50):
            file.write(top_seq[i:i+50] + "\n")
            file.write(bot_seq[i:i+50] + "\n")
            file.write("\n")
s = "AAGGTATGAATC"
t = "CAGTTGCAA"
optimal_score = local_alignment_score(s, t)
print(s)
print(t)
print("Local alignment score: " + str(optimal_score))