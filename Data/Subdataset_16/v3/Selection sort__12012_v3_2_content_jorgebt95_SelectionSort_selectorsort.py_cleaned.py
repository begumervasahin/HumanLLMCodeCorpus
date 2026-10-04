def fonk1(b3):
    b1 = len(b3)
    for i in range(b1):
        b2 = i
        for j in range(i + 1, b1):
            if b3[j] < b3[b2]:
                b2 = j
        b3[i], b3[b2] = b3[b2], b3[i]
def fonk2():
    b3 = [5, 6, 4, 3, 7, 8]
    b4 = [3, 4, 5, 6, 7, 8]
    fonk1(b3)
    assert b3 = = b4, f"Expected {b4} but got {b3}"
    print("Test passed!")
if b5 = = "__main__":
    fonk2()