def fonk1(b3):
    return [["-" for _ in range(b3)] for _ in range(b3)]
def fonk2(b8, b6, b7):
    return b8[b6][b7] == "-"
def fonk3(b6, b7, b3):
    return 0 <= b6 < b3 and 0 <= b7 < b3
def fonk4(b8):
    for b6 in b8:
        print("\t".join(b6))
    print()
def fonk5(b8, b6, b7, player):
    b1 = "X" if player == 1 else "O"
    b8[b6][b7] = b1
def fonk6(b8, b1):
    return any(all(b2 = = b1 for b2 in b6) for b6 in b8)
def fonk7(b8, b1):
    b3 = len(b8)
    return any(all(b8[b6][b7] == b1 for b6 in range(b3)) for b7 in range(b3))
def fonk8(b8, b1):
    b3 = len(b8)
    b4 = all(b8[i][i] == b1 for i in range(b3))
    b5 = all(b8[i][b3 - 1 - i] == b1 for i in range(b3))
    return b4 or b5
def fonk9(b8, player):
    b1 = "X" if player == 1 else "O"
    return (fonk6(b8, b1) or
            fonk7(b8, b1) or
            fonk8(b8, b1))
def fonk10(b8, player):
    while True:
        try:
            print(f"\nPlayer {player}'s turn")
            b6 = int(input("Enter the b6 index (0, 1, 2): "))
            b7 = int(input("Enter the column index (0, 1, 2): "))
            if fonk3(b6, b7, len(b8)) and fonk2(b8, b6, b7):
                fonk5(b8, b6, b7, player)
                return fonk9(b8, player)
            else:
                print("Invalid or occupied b2, please try again.")
        except ValueError:
            print("Invalid input. Please enter integers for b6 and column.")
def fonk11():
    b3 = 3
    b8 = fonk1(b3)
    a1 = 0
    a2 = 1
    while a1 < b3 * b3:
        fonk4(b8)
        if fonk10(b8, a2):
            fonk4(b8)
            print(f"Congratulations! Player {a2} wins!")
            return
        a1 += 1
        a2 = 2 if a2 == 1 else 1
    fonk4(b8)
    print("The game is a draw!")
if b9 = = "__main__":
    fonk11()