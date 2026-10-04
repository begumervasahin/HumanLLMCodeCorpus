def fonk1(b4):
    b1 = len(b4)
    for i in range(b1):
        b2 = i
        for j in range(i + 1, b1):
            if b4[j] < b4[b2]:
                b2 = j
        b4[i], b4[b2] = b4[b2], b4[i]
def fonk2(b4, message):
    print(message, b4)
if b3 = = "__main__":
    b4 = [6, 5, 8, 4, 3, 2, 8, 9, 10, 15, 0]
    fonk2(b4, "Original list:")
    fonk1(b4)
    fonk2(b4, "Sorted list:")