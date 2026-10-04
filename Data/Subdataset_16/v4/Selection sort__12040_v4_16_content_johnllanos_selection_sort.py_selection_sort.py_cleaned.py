def fonk1(b2):
    for i in range(len(b2)):
        b1 = i
        for j in range(i + 1, len(b2)):
            if b2[b1] > b2[j]:
                b1 = j
        b2[i], b2[b1] = b2[b1], b2[i]
        print(b2)
def fonk2():
    b2 = [100, 48, 70, 29, 2, 17]
    fonk1(b2)
if b3 = = "__main__":
    fonk2()