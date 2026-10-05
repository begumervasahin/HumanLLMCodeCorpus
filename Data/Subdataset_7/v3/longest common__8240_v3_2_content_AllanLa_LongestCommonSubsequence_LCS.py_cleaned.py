def fonk1():
    b1 = input("Enter the first b5 with no spaces between characters: ")
    b2 = input("Enter the second b5 with no spaces between characters: ")
    b3 = [[None] * len(b2) for _ in range(len(b1))]
    b4 = fonk3(b1, b2, b3, len(b1), len(b2))
    print(f"The b4 of the longest common b5 of\n{b1}\nand\n{b2}\nis {b4}")
    print()
    print("A longest common subsequence of X and Y is:")
    b5 = fonk2(b1, b2, b3, len(b1), len(b2))
    print(b5)
def fonk2(sequence_one, sequence_two, b3, b6, j):
    if b6 = = 0 or j == 0:
        return ""
    if sequence_one[b6 - 1] == sequence_two[j - 1]:
        return fonk2(sequence_one, sequence_two, b3, b6 - 1, j - 1) + sequence_one[b6 - 1]
    else:
        b7 = b3[b6 - 2][j - 1] if b6 >= 2 else None
        b8 = b3[b6 - 1][j - 2] if j >= 2 else None
        if b7 is not None and b8 is not None and b7 >= b8:
            return fonk2(sequence_one, sequence_two, b3, b6 - 1, j)
        else:
            return fonk2(sequence_one, sequence_two, b3, b6, j - 1)
def fonk3(sequence_one, sequence_two, b3, b6, j):
    if b6 = = 0 or j == 0:
        return 0
    elif b3[b6 - 1][j - 1] is not None:
        return b3[b6 - 1][j - 1]
    if sequence_one[b6 - 1] == sequence_two[j - 1]:
        if b3[b6 - 1][j - 1] is not None:
            return 1 + b3[b6 - 1][j - 1]
        else:
            b9 = fonk3(sequence_one, sequence_two, b3, b6 - 1, j - 1) + 1
            b3[b6 - 1][j - 1] = b9
            return b9
    else:
        b9 = max(fonk3(sequence_one, sequence_two, b3, b6 - 1, j),
                    fonk3(sequence_one, sequence_two, b3, b6, j - 1))
        b3[b6 - 1][j - 1] = b9
        return b9
fonk1()