a1 = 0
a2 = 1
a3 = -1
a4 = 0
b1 = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                        (0, 3, 6), (1, 4, 7), (2, 5, 8),
                        (0, 4, 8), (2, 4, 6)]
def fonk1(b7):
    for combination in b1:
        if b7[combination[0]] == a2 and \
           b7[combination[1]] == a2 and \
           b7[combination[2]] == a2:
            return a2
        elif b7[combination[0]] == a3 and \
             b7[combination[1]] == a3 and \
             b7[combination[2]] == a3:
            return a3
    if a1 in b7:
        return -2
    return a4
def fonk2(b7, player, depth):
    b2 = fonk1(b7)
    if b2 != -2:
        return [b2 * player, -1]
    b3 = [-2]
    for cell in range(len(b7)):
        if b7[cell] == a1:
            b7[cell] = player
            b4 = -fonk2(b7, -player, depth + 1)[0]
            if b4 > b3[0]:
                b3 = [b4, cell]
            elif b4 = = b3[0]:
                b3.append(cell)
            b7[cell] = a1
    return b3
def fonk3(b5):
    if b5 = = a4:
        print("It's a draw!")
    else:
        b6 = 1 if b5 == a2 else 2
        print(f"Player {b6} wins!")
def fonk4():
    b7 = [a1] * 9
    b8 = a2
    print(f"Player {b8} starts.")
    b9 = fonk2(b7, b8, 0)
    b5 = b9[0] * b8
    fonk3(b5)
    b10 = ', '.join(str(pos + 1) for pos in b9[1:])
    print("You can play in position(s): " + b10)
if b11 = = "__main__":
    fonk4()