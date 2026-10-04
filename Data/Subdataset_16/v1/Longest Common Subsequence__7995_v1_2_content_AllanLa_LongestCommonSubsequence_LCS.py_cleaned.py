def fonk1(sequenceOne, sequenceTwo, array, b1, j):
    if b1 = = 0 or j == 0:
        return 0
    elif array[b1 - 1][j - 1] is not None:
        return array[b1 - 1][j - 1]
    if sequenceOne[b1 - 1] == sequenceTwo[j - 1]:
        if array[b1 - 1][j - 1] is not None:
            return 1 + array[b1 - 1][j - 1]
        else:
            b2 = fonk1(sequenceOne, sequenceTwo, array, b1 - 1, j - 1) + 1
            array[b1 - 1][j - 1] = b2
            return b2
    else:
        b2 = max(fonk1(sequenceOne, sequenceTwo, array, b1 - 1, j),
                    fonk1(sequenceOne, sequenceTwo, array, b1, j - 1))
        array[b1 - 1][j - 1] = b2
        return b2
def fonk2(sequenceOne, sequenceTwo, array, b1, j):
    if b1 = = 0 or j == 0:
        return ""
    if sequenceOne[b1 - 1] == sequenceTwo[j - 1]:
        return fonk2(sequenceOne, sequenceTwo, array, b1 - 1, j - 1) + sequenceOne[b1 - 1]
    else:
        b3 = array[b1 - 2][j - 1] if b1 - 2 >= 0 else None
        b4 = array[b1 - 1][j - 2] if j - 2 >= 0 else None
        if b3 is not None and b4 is not None and b3 >= b4:
            return fonk2(sequenceOne, sequenceTwo, array, b1 - 1, j)
        else:
            return fonk2(sequenceOne, sequenceTwo, array, b1, j - 1)
def fonk3():
    b5 = input("Enter the first b8 with no spaces between characters: ")
    b6 = input("Enter the second b8 with no spaces between characters: ")
    b7 = [[None] * len(b6) for _ in range(len(b5))]
    b2 = fonk1(b5, b6, b7, len(b5), len(b6))
    print("The length of a longest common b8 of ")
    print(b5)
    print("and")
    print(b6)
    print("is " + str(b2))
    print()
    print("A longest common subsequence of X and Y is ")
    b8 = fonk2(b5, b6, b7, len(b5), len(b6))
    print(b8)
def fonk4(array):
    for row in array:
        print(" ".join([str(elem) if elem is not None else '-' for elem in row]))
    print()
fonk3()