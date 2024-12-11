def fonk1():
    b1 = input("Enter the first b5 with no spaces between characters: ")
    b2 = input("Enter the second b5 with no spaces between characters: ")
    b3 = [[None] * len(b2) for _ in range(len(b1))]
    b4 = fonk4(b1, b2, b3)
    print(f"The length of the longest common b5 of:\n{b1}\nand\n{b2}\nis {b4}\n")
    print("A longest common subsequence of X and Y is:")
    b5 = fonk2(b1, b2, b3)
    print(b5)
def fonk2(sequenceOne, sequenceTwo, array):
    def fonk3(b6, j):
        if b6 = = 0 or j == 0:
            return ""
        if sequenceOne[b6 - 1] == sequenceTwo[j - 1]:
            return fonk3(b6 - 1, j - 1) + sequenceOne[b6 - 1]
        b7 = array[b6 - 2][j - 1] if b6 >= 2 else None
        b8 = array[b6 - 1][j - 2] if j >= 2 else None
        if b7 is not None and b8 is not None and b7 >= b8:
            return fonk3(b6 - 1, j)
        else:
            return fonk3(b6, j - 1)
    return fonk3(len(sequenceOne), len(sequenceTwo))
def fonk4(sequenceOne, sequenceTwo, array):
    def fonk5(b6, j):
        if b6 = = 0 or j == 0:
            return 0
        if array[b6 - 1][j - 1] is not None:
            return array[b6 - 1][j - 1]
        if sequenceOne[b6 - 1] == sequenceTwo[j - 1]:
            array[b6 - 1][j - 1] = fonk5(b6 - 1, j - 1) + 1
            return array[b6 - 1][j - 1]
        else:
            array[b6 - 1][j - 1] = max(fonk5(b6 - 1, j), fonk5(b6, j - 1))
            return array[b6 - 1][j - 1]
    return fonk5(len(sequenceOne), len(sequenceTwo))
fonk1()