def fonk1():
    b1 = input("Enter the first b6 with no spaces between characters: ")
    b2 = input("Enter the second b6 with no spaces between characters: ")
    return b1, b2
def fonk2(b1, b2):
    return [[None for _ in range(len(b2))] for _ in range(len(b1))]
def fonk3(b1, b2, b5, b3, j):
    if b3 = = 0 or j == 0:
        return 0
    if b5[b3-1][j-1] is not None:
        return b5[b3-1][j-1]
    if b1[b3-1] == b2[j-1]:
        b4 = fonk3(b1, b2, b5, b3-1, j-1) + 1
    else:
        b4 = max(
            fonk3(b1, b2, b5, b3-1, j),
            fonk3(b1, b2, b5, b3, j-1)
        )
    b5[b3-1][j-1] = b4
    return b4
def fonk4(b1, b2, b5, b3, j):
    if b3 = = 0 or j == 0:
        return ""
    if b1[b3-1] == b2[j-1]:
        return fonk4(b1, b2, b5, b3-1, j-1) + b1[b3-1]
    elif b5[b3-2][j-1] >= b5[b3-1][j-2]:
        return fonk4(b1, b2, b5, b3-1, j)
    else:
        return fonk4(b1, b2, b5, b3, j-1)
def fonk5(b1, b2, b4, b6):
    print(f"The length of the longest common subsequence of {b1} and {b2} is {b4}")
    print()
    print("A longest common subsequence of X and Y is")
    print(b6)
def fonk6():
    b1, b2 = fonk1()
    b5 = fonk2(b1, b2)
    b4 = fonk3(b1, b2, b5, len(b1), len(b2))
    b6 = fonk4(b1, b2, b5, len(b1), len(b2))
    fonk5(b1, b2, b4, b6)
if b7 = = "__main__":
    fonk6()