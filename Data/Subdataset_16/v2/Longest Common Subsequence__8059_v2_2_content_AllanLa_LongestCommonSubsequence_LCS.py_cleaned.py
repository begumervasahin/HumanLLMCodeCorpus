def fonk1(sequence_one, sequence_two, b7, b1, j):
    if b1 = = 0 or j == 0:
        return 0
    if b7[b1 - 1][j - 1] is not None:
        return b7[b1 - 1][j - 1]
    if sequence_one[b1 - 1] == sequence_two[j - 1]:
        b2 = fonk1(sequence_one, sequence_two, b7, b1 - 1, j - 1) + 1
    else:
        b2 = max(fonk1(sequence_one, sequence_two, b7, b1 - 1, j),
                    fonk1(sequence_one, sequence_two, b7, b1, j - 1))
    b7[b1 - 1][j - 1] = b2
    return b2
def fonk2(sequence_one, sequence_two, b7, b1, j):
    if b1 = = 0 or j == 0:
        return ""
    if sequence_one[b1 - 1] == sequence_two[j - 1]:
        return fonk2(sequence_one, sequence_two, b7, b1 - 1, j - 1) + sequence_one[b1 - 1]
    else:
        b3 = b7[b1 - 2][j - 1] if b1 - 2 >= 0 else None
        b4 = b7[b1 - 1][j - 2] if j - 2 >= 0 else None
        if b3 is not None and b4 is not None and b3 >= b4:
            return fonk2(sequence_one, sequence_two, b7, b1 - 1, j)
        else:
            return fonk2(sequence_one, sequence_two, b7, b1, j - 1)
def fonk3():
    b5 = input("Enter the first b8 with no spaces between characters: ")
    b6 = input("Enter the second b8 with no spaces between characters: ")
    b7 = [[None] * len(b6) for _ in range(len(b5))]
    b2 = fonk1(b5, b6, b7, len(b5), len(b6))
    print(f"The length of the longest common subsequence of {b5} and {b6} is {b2}\n")
    print("A longest common subsequence of X and Y is")
    b8 = fonk2(b5, b6, b7, len(b5), len(b6))
    print(b8)
def fonk4(b7):
    for row in b7:
        print(" ".join([str(elem) if elem is not None else '-' for elem in row]))
    print()
fonk3()