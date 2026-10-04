
b1 = [0, 0, 0,
         0, 0, 0,
         0, 0, 0]
a1 = 1
b2 = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                        (0, 3, 6), (1, 4, 7), (2, 5, 8),
                        (0, 4, 8), (2, 4, 6)]
def fonk1(b1):
    for combo in b2:
        if b1[combo[0]] == b1[combo[1]] == b1[combo[2]] == 1:
            return 1
        if b1[combo[0]] == b1[combo[1]] == b1[combo[2]] == -1:
            return -1
    if 0 in b1:
        return -2
    return 0
def fonk2(b1, player, depth):
    b3 = fonk1(b1)
    if b3 != -2:
        return (b3 * player, -1)
    b4 = [-2]
    for index in range(len(b1)):
        if b1[index] == 0:
            b1[index] = player
            b5 = -fonk2(b1, -player, depth + 1)[0]
            if b5 > b4[0]:
                b4 = [b5, index]
            elif b5 = = b4[0]:
                b4.append(index)
            b1[index] = 0
    return b4
def fonk3():
    b6 = fonk2(b1, a1, 0)
    b7 = b6[0] * a1
    if a1 = = 1:
        print("Player 1 starts.")
    elif a1 = = -1:
        print("Player 2 starts.")
    if b7 = = 0:
        print("It's a draw!")
    else:
        b8 = 1 if b7 == 1 else 2
        print(f"Player {b8} wins!")
    if b7 != -a1:
        b9 = ", ".join(str(move + 1) for move in b6[1:])
        print(f"You can play at positions: {b9}")
if b10 = = '__main__':
    fonk3()