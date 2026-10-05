def fonk1(b1):
    for last_pos in range(len(b1) - 1, 0, -1):
        a1 = 0
        for pos in range(1, last_pos + 1):
            if b1[pos] > b1[a1]:
                a1 = pos
        b1[last_pos], b1[a1] = b1[a1], b1[last_pos]
b1 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
fonk1(b1)
print(b1)