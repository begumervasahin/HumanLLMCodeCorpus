from BSTTree import BSTTree
def fonk1(beta_list, alpha_list, beta_len):
    b1 = [[None for _ in range(beta_len + 1)] for _ in range(beta_len + 1)]
    b2 = [[None for _ in range(beta_len + 1)] for _ in range(beta_len + 1)]
    b3 = [[None for _ in range(beta_len)] for _ in range(beta_len)]
    for x in range(beta_len + 1):
        b1[x][x] = alpha_list[x]
        b2[x][x] = alpha_list[x]
    for length in range(1, beta_len + 1):
        for i in range(beta_len - length + 1):
            b4 = i + length
            b1[i][b4] = float("inf")
            b2[i][b4] = b2[i][b4 - 1] + beta_list[b4 - 1] + alpha_list[b4]
            for b7 in range(i, b4):
                b5 = b1[i][b7] + b1[b7 + 1][b4] + b2[i][b4]
                if b5 < b1[i][b4]:
                    b1[i][b4] = b5
                    b3[i][b4 - 1] = b7
    return b1, b3
def fonk2(table):
    for row in table:
        print(row)
def fonk3(b3, key_list):
    i, b4 = 0, len(b3) - 1
    b6 = b3[i][b4]
    b7 = BSTTree(key_list[b6])
    b8 = []
    if b6 + 1 <= b4:
        b8.append((b6 + 1, b4, b7))
    if i <= b6 - 1:
        b8.append((i, b6 - 1, b7))
    while b8:
        i, b4, b9 = b8.pop()
        b10 = b3[i][b4]
        b11 = BSTTree(key_list[b10])
        if b11.value < b9.value:
            b9.b12 = b11
        else:
            b9.b13 = b11
        if b10 + 1 <= b4:
            b8.append((b10 + 1, b4, b11))
        if i <= b10 - 1:
            b8.append((i, b10 - 1, b11))
    return b7