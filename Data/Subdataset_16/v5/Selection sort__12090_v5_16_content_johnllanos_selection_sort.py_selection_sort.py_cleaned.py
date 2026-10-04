def fonk1(b3):
    b1 = len(b3)
    for i in range(b1):
        b2 = i
        for j in range(i + 1, b1):
            if b3[j] < b3[b2]:
                b2 = j
        b3[i], b3[b2] = b3[b2], b3[i]
        print(f"Array after swapping index {i} and {b2}: {b3}")
def fonk2():
    b3 = [100, 48, 70, 29, 2, 17]
    fonk1(b3)
if b4 = = "__main__":
    fonk2()