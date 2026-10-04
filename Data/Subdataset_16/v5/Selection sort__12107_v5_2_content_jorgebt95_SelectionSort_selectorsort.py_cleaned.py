def fonk1(b5):
    b1 = len(b5)
    for i in range(b1 - 1):
        b2 = i
        for j in range(i + 1, b1):
            if b5[j] < b5[b2]:
                b2 = j
        b5[i], b5[b2] = b5[b2], b5[i]
def fonk2():
    b3 = [5, 6, 4, 3, 7, 8]
    fonk1(b3)
    assert b3 = = [3, 4, 5, 6, 7, 8], f"Test failed: {b3}"
    print("Test passed!")
if b4 = = "__main__":
    b5 = [5, 6, 4, 3, 7, 8]
    print("Original list:", b5)
    fonk1(b5)
    print("Sorted list:", b5)
    fonk2()