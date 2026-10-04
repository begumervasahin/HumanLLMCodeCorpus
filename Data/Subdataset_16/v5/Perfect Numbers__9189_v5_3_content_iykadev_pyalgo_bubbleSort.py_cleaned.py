def fonk1(b2):
    b1 = len(b2)
    for passnum in range(b1 - 1, 0, -1):
        for i in range(passnum):
            if b2[i] > b2[i + 1]:
                b2[i], b2[i + 1] = b2[i + 1], b2[i]
def fonk2():
    b2 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    fonk1(b2)
    print(f"Sorted list: {b2}")
if b3 = = "__main__":
    fonk2()