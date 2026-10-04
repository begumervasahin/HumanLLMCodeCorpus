def fonk1(b1):
    for fillslot in range(len(b1) - 1, 0, -1):
        a1 = 0
        for location in range(1, fillslot + 1):
            if b1[location] > b1[a1]:
                a1 = location
        b1[fillslot], b1[a1] = b1[a1], b1[fillslot]
b1 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
fonk1(b1)
print(b1)