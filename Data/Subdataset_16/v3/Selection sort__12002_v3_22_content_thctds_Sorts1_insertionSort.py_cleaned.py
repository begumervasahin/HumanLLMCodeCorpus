def fonk1(b4):
    for index in range(1, len(b4)):
        b1 = b4[index]
        b2 = index
        while b2 > 0 and b4[b2 - 1] > b1:
            b4[b2] = b4[b2 - 1]
            b2 -= 1
        b4[b2] = b1
def fonk2(b4, message):
    print(message, b4)
if b3 = = "__main__":
    b4 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    fonk2(b4, "Original list:")
    fonk1(b4)
    fonk2(b4, "Sorted list:")