def fonk1(rows, cols):
    b1 = [["-" for _ in range(cols)] for _ in range(rows)]
    return b1
def fonk2(b1, b4, b5):
    return b1[b4][b5] == "-"
def fonk3(b4, b5):
    return 0 <= b4 < 3 and 0 <= b5 < 3
def fonk4(b1):
    for b4 in b1:
        print("   ".join(b4))
        print()
def fonk5(b1, b4, b5, player):
    b2 = "X" if player == 1 else "O"
    b1[b4][b5] = b2
def fonk6(b1, b2):
    for b4 in b1:
        if all(b3 = = b2 for b3 in b4):
            return True
    return False
def fonk7(b1, b2):
    for b5 in range(3):
        if all(b1[b4][b5] == b2 for b4 in range(3)):
            return True
    return False
def fonk8(b1, b2):
    if all(b1[i][i] == b2 for i in range(3)) or all(b1[i][2 - i] == b2 for i in range(3)):
        return True
    return False
def fonk9(b1, player):
    b2 = "X" if player == 1 else "O"
    return fonk6(b1, b2) or fonk7(b1, b2) or fonk8(b1, b2)
def fonk10(b1, player):
    while True:
        print(f"\nPlayer {player}'s turn")
        b4 = int(input("Enter the b4 (0, 1, 2): "))
        b5 = int(input("Enter the column (0, 1, 2): "))
        if fonk3(b4, b5) and fonk2(b1, b4, b5):
            return b4, b5
        else:
            print("Invalid move! Please try again.")
def fonk11():
    b1 = fonk1(3, 3)
    fonk4(b1)
    a1 = 1
    for _ in range(9):
        b4, b5 = fonk10(b1, a1)
        fonk5(b1, b4, b5, a1)
        fonk4(b1)
        if fonk9(b1, a1):
            print(f"Player {a1} wins!")
            return
        a1 = 2 if a1 == 1 else 1
    print("It's a draw!")
if b6 = = "__main__":
    fonk11()