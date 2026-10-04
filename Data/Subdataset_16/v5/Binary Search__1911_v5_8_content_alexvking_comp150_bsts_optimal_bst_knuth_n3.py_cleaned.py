from BSTTree import BSTTree
def fonk1(beta_list, alpha_list, beta_len):
    b1 = [[None] * (beta_len + 1) for _ in range(beta_len + 1)]
    b2 = [[None] * (beta_len + 1) for _ in range(beta_len + 1)]
    b3 = [[None] * beta_len for _ in range(beta_len)]
    for i in range(beta_len + 1):
        b1[i][i] = alpha_list[i]
        b2[i][i] = alpha_list[i]
    for length in range(1, beta_len + 1):
        for i in range(beta_len - length + 1):
            b4 = i + length
            b2[i][b4] = b2[i][b4 - 1] + beta_list[b4 - 1] + alpha_list[b4]
            b1[i][b4] = float("inf")
            for b12 in range(i, b4):
                b5 = b1[i][b12] + b1[b12 + 1][b4] + b2[i][b4]
                if b5 < b1[i][b4]:
                    b1[i][b4] = b5
                    b3[i][b4 - 1] = b12
    return b1, b3
def fonk2(table):
    for row in table:
        print(row)
def fonk3(b3, key_list):
    def fonk4(i, b4, b6 = None, b11=True):
        if i > b4:
            return
        b7 = b3[i][b4]
        b8 = BSTTree(key_list[b7])
        if b6:
            if b11:
                b6.b9 = b8
            else:
                b6.b10 = b8
        fonk4(i, b7 - 1, b8, b11 = True)
        fonk4(b7 + 1, b4, b8, b11 = False)
        return b8
    b12 = fonk4(0, len(b3) - 1)
    return b12
