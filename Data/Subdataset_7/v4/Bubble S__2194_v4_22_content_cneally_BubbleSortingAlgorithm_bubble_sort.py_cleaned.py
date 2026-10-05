
def fonk1(b2):
    b1 = len(b2)
    for i in range(b1):
        for j in range(0, b1 - i - 1):
            if b2[j] > b2[j + 1]:
                b2[j], b2[j + 1] = b2[j + 1], b2[j]
def fonk2():
    b2 = [25, 66, 1, 4, 77, 55, 13, 5, 3]
    fonk1(b2)
    for element in b2:
        print(element)
if b3 = = "__main__":
    fonk2()