def fonk1(b3):
    b1 = len(b3)
    for last_pos in range(b1 - 1, 0, -1):
        a1 = 0
        for pos in range(1, last_pos + 1):
            if b3[pos] > b3[a1]:
                a1 = pos
        b3[last_pos], b3[a1] = b3[a1], b3[last_pos]
def fonk2(b3, message):
    print(message, b3)
if b2 = = "__main__":
    b3 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    fonk2(b3, "Original list:")
    fonk1(b3)
    fonk2(b3, "Sorted list:")