from BSTTree import BSTTree
def fonk1(beta_list, alpha_list, beta_len):
    b1 = [[None for i in range(beta_len + 1)] for b4 in range(1, beta_len + 2)]
    b2 = [[None for i in range(beta_len + 1)] for b4 in range(1, beta_len + 2)]
    b3 = [[None for i in range(beta_len)] for b4 in range(beta_len)]
    for x in range(beta_len + 1):
        b1[x][x] = alpha_list[x]
        b2[x][x] = alpha_list[x]
    for y in range(beta_len + 1):
        for i in range(beta_len - y):
            b4 = i + y + 1
            b1[i][b4] = float("inf")
            b2[i][b4] = b2[i][b4 - 1] + beta_list[b4 - 1] + alpha_list[b4]
            for b7 in range(i, b4):
                b5 = b1[i][b7] + b1[b7 + 1][b4] + b2[i][b4]
                if b5 < b1[i][b4]:
                    b1[i][b4] = b5
                    b3[i][b4 - 1] = b7
    return (b1, b3)
def fonk2(table):
    for row in table:
        print(row)
def fonk3(b3, key_list):
    (i, b4) = 0, len(b3) - 1
    b6 = b3[i][b4]
    b7 = BSTTree(key_list[b6])
    b8 = []
    if (b6 + 1 <= b4):
        b8.append((b6 + 1, b4, b7))
    if i <= (b6 - 1):
        b8.append((i, b6 - 1, b7))
    while b8:
        (i, b4, parent) = b8.pop()
        b9 = b3[i][b4]
        b10 = BSTTree(key_list[b9])
        if b10.value < parent.value:
            parent.b11 = b10
        else:
            parent.b12 = b10
        if (b9 + 1 <= b4):
            b8.append((b9 + 1, b4, b10))
        if i <= (b9 - 1):
            b8.append((i, b9 - 1, b10))
    return b7