def fonk1(rows, cols):
    b1 = [["-" for _ in range(cols)] for _ in range(rows)]
    return b1
def fonk2(b1, b5, b6):
    return b1[b5][b6] == "-"
def fonk3(b5, b6):
    return 0 <= b5 < 3 and 0 <= b6 < 3
def fonk4(b1):
    for b5 in b1:
        print("   ".join(b5))
        print()
def fonk5(b1, b5, b6, b2):
    if b2 = = 1:
        b1[b5][b6] = "X"
    else:
        b1[b5][b6] = "O"
def fonk6(b1, b4):
    for b5 in b1:
        if all(b3 = = b4 for b3 in b5):
            return True
    return False
def fonk7(b1, b4):
    for b6 in range(3):
        if all(b1[b5][b6] == b4 for b5 in range(3)):
            return True
    return False
def fonk8(b1, b4):
    if all(b1[i][i] == b4 for i in range(3)) or all(b1[i][2 - i] == b4 for i in range(3)):
        return True
    return False
def fonk9(b1, b2):
    b4 = "X" if b2 == 1 else "O"
    return fonk6(b1, b4) or fonk7(b1, b4) or fonk8(b1, b4)
def fonk10(b1, b2):
    while True:
        print(f"\nPlayer {b2}'s turn")
        b5 = int(input("Enter the b5 (0, 1, 2): "))
        b6 = int(input("Enter the column (0, 1, 2): "))
        if fonk3(b5, b6) and fonk2(b1, b5, b6):
            return b5, b6
        else:
            print("Invalid move! Try again.")
def fonk11():
    b1 = fonk1(3, 3)
    fonk4(b1)
    a1 = 1
    for _ in range(9):
        b5, b6 = fonk10(b1, a1)
        fonk5(b1, b5, b6, a1)
        fonk4(b1)
        if fonk9(b1, a1):
            print(f"Player {a1} wins!")
            return
        a1 = 2 if a1 == 1 else 1
    print("It's a draw!")
if b7 = = "__main__":
    fonk11()