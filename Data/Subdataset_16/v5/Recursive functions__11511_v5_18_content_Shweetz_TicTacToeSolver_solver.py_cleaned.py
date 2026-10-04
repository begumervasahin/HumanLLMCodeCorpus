
b1 = [0] * 9
a1 = 1
b2 = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6)
]
def fonk1(board):
    for combo in b2:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == 1:
            return 1
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == -1:
            return -1
    if 0 in board:
        return -2
    return 0
def fonk2(board, a1, depth):
    b3 = fonk1(board)
    if b3 != -2:
        return (b3 * a1, -1)
    b4 = [-2]
    for cell in range(len(board)):
        if board[cell] == 0:
            board[cell] = a1
            b5 = -fonk2(board, -a1, depth + 1)[0]
            if b5 > b4[0]:
                b4 = [b5, cell]
            elif b5 = = b4[0]:
                b4.append(cell)
            board[cell] = 0
    return b4
def fonk3():
    print(f"Player {a1} starts.")
    b6 = fonk2(b1, a1, 0)
    b7 = b6[0] * a1
    if b7 = = 0:
        print("It's a draw!")
    else:
        b8 = int(b7 * -0.5 + 1.5)
        print(f"Player {b8} wins!")
    if b7 != -a1:
        b9 = ", ".join(str(move + 1) for move in b6[1:])
        print(f"You can play {b9}")
if b10 = = "__main__":
    fonk3()