
def fonk1(rows, cols):
    return [["-" for _ in range(cols)] for _ in range(rows)]
def fonk2(b6, b4, b5):
    return b6[b4][b5] == "-"
def fonk3(b4, b5, b3):
    return 0 <= b4 < b3 and 0 <= b5 < b3
def fonk4(b6):
    for b4 in b6:
        print("\t".join(b4))
    print()
def fonk5(b6, b4, b5, player):
    b1 = "X" if player == 1 else "O"
    b6[b4][b5] = b1
def fonk6(b6, b1):
    for b4 in b6:
        if all(b2 = = b1 for b2 in b4):
            return True
    return False
def fonk7(b6, b1):
    for b5 in range(len(b6)):
        if all(b6[b4][b5] == b1 for b4 in range(len(b6))):
            return True
    return False
def fonk8(b6, b1):
    b3 = len(b6)
    if all(b6[i][i] == b1 for i in range(b3)):
        return True
    if all(b6[i][b3 - 1 - i] == b1 for i in range(b3)):
        return True
    return False
def fonk9(b6, player):
    b1 = "X" if player == 1 else "O"
    return (fonk6(b6, b1) or
            fonk7(b6, b1) or
            fonk8(b6, b1))
def fonk10(b6, player):
    while True:
        try:
            print(f"\nPlayer {player}'s turn")
            b4 = int(input("Enter the b4 index (0, 1, 2): "))
            b5 = int(input("Enter the column index (0, 1, 2): "))
            if fonk3(b4, b5, len(b6)) and fonk2(b6, b4, b5):
                fonk5(b6, b4, b5, player)
                return fonk9(b6, player)
            else:
                print("Invalid or occupied b2, please try again.")
        except ValueError:
            print("Invalid input. Please enter integers for b4 and column.")
def fonk11():
    b3 = 3
    b6 = fonk1(b3, b3)
    a1 = 0
    a2 = 1
    while a1 < b3 * b3:
        fonk4(b6)
        if fonk10(b6, a2):
            fonk4(b6)
            print(f"Congratulations! Player {a2} wins!")
            return
        a1 += 1
        a2 = 2 if a2 == 1 else 1
    fonk4(b6)
    print("The game is a draw!")
if b7 = = "__main__":
    fonk11()