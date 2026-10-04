def fonk1(b3):
    b1 = len(b3)
    for i in range(b1 - 1):
        b2 = i
        for j in range(i + 1, b1):
            if b3[j] < b3[b2]:
                b2 = j
        b3[i], b3[b2] = b3[b2], b3[i]
b3 = [5, 6, 4, 3, 7, 8]
fonk1(b3)
print(b3)
def fonk2():
    b4 = [5, 6, 4, 3, 7, 8]
    fonk1(b4)
    assert b4 = = [3, 4, 5, 6, 7, 8], f"Test failed: {b4}"
fonk2()