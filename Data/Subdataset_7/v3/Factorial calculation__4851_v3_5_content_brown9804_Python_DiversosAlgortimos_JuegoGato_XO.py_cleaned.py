def fonk1(rows, cols):
    return [["-" for _ in range(cols)] for _ in range(rows)]
def fonk2(b5, b3, b4):
    return b5[b3][b4] == "-"
def fonk3(b3, b4):
    return 0 <= b3 < 3 and 0 <= b4 < 3
def fonk4(b5):
    for b3 in b5:
        print("   ".join(b3))
    print()
def fonk5(b5, b3, b4, player):
    b1 = "X" if player == 1 else "O"
    b5[b3][b4] = b1
def fonk6(b5, b1):
    for b3 in b5:
        if all(b2 = = b1 for b2 in b3):
            return True
    return False
def fonk7(b5, b1):
    for b4 in range(3):
        if all(b5[b3][b4] == b1 for b3 in range(3)):
            return True
    return False
def fonk8(b5, b1):
    return all(b5[i][i] == b1 for i in range(3)) or all(b5[i][2 - i] == b1 for i in range(3))
def fonk9(b5, player):
    b1 = "X" if player == 1 else "O"
    return fonk6(b5, b1) or fonk7(b5, b1) or fonk8(b5, b1)
def fonk10(b5, player):
    while True:
        print(f"\nPlayer {player}'s turn")
        b3 = int(input("Enter the b3 (0, 1, 2): "))
        b4 = int(input("Enter the column (0, 1, 2): "))
        if fonk3(b3, b4) and fonk2(b5, b3, b4):
            return b3, b4
        else:
            print("Invalid move! Please try again.")
def fonk11():
    b5 = fonk1(3, 3)
    fonk4(b5)
    a1 = 1
    for _ in range(9):
        b3, b4 = fonk10(b5, a1)
        fonk5(b5, b3, b4, a1)
        fonk4(b5)
        if fonk9(b5, a1):
            print(f"Player {a1} wins!")
            return
        a1 = 2 if a1 == 1 else 1
    print("It's a draw!")
if b6 = = "__main__":
    fonk11()