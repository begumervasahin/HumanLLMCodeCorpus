def fonk1():
    b1 = input("Enter the first b6 with no spaces between characters: ")
    b2 = input("Enter the second b6 with no spaces between characters: ")
    b3 = []
    for b7 in range(len(b1)):
        b4 = []
        for j in range(len(b2)):
            b4.append(None)
        b3.append(b4)
    b5 = fonk3(b1, b2, b3, len(b1), len(b2))
    print("The length of the longest common b6 of:")
    print(b1)
    print("and")
    print(b2)
    print("is " + str(b5))
    print()
    print("A longest common subsequence of X and Y is:")
    b6 = fonk2(b1, b2, b3, len(b1), len(b2))
    print(b6)
def fonk2(sequenceOne, sequenceTwo, array, b7, j):
    if b7 = = 0 or j == 0:
        return ""
    if sequenceOne[b7 - 1] == sequenceTwo[j - 1]:
        return fonk2(sequenceOne, sequenceTwo, array, b7 - 1, j - 1) + sequenceOne[b7 - 1]
    else:
        b8 = array[b7 - 2][j - 1] if b7 >= 2 else None
        b9 = array[b7 - 1][j - 2] if j >= 2 else None
        if b8 is not None and b9 is not None and b8 >= b9:
            return fonk2(sequenceOne, sequenceTwo, array, b7 - 1, j)
        else:
            return fonk2(sequenceOne, sequenceTwo, array, b7, j - 1)
def fonk3(sequenceOne, sequenceTwo, array, b7, j):
    if b7 = = 0 or j == 0:
        return 0
    elif array[b7 - 1][j - 1] is not None:
        return array[b7 - 1][j - 1]
    if sequenceOne[b7 - 1] == sequenceTwo[j - 1]:
        if array[b7 - 1][j - 1] is not None:
            return 1 + array[b7 - 1][j - 1]
        else:
            b5 = fonk3(sequenceOne, sequenceTwo, array, b7 - 1, j - 1) + 1
            array[b7 - 1][j - 1] = b5
            return b5
    else:
        b5 = max(fonk3(sequenceOne, sequenceTwo, array, b7 - 1, j),
                    fonk3(sequenceOne, sequenceTwo, array, b7, j - 1))
        array[b7 - 1][j - 1] = b5
        return b5
fonk1()