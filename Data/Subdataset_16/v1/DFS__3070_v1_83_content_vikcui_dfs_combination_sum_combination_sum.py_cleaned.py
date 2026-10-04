def fonk1(b5, a1):
    b5.sort()
    b1 = []
    b2 = []
    fonk2(b5, a1, 0, b2, b1)
    return b1
def fonk2(b5, a1, current_index, b2, b1):
    for j in range(current_index, len(b5)):
        b3 = b5[j]
        if b3 > a1:
            break
        b2.append(b3)
        if b3 < a1:
            fonk2(b5, a1 - b3, j, b2, b1)
        else:
            b1.append(list(b2))
        b2.pop()
if b4 = = "__main__":
    b5 = [2, 3, 6, 7]
    a1 = 7
    b6 = fonk1(b5, a1)
    print("Unique b6:", b6)