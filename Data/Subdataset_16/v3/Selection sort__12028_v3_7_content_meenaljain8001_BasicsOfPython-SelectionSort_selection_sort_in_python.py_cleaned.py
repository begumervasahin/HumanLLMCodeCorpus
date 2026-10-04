def fonk1(b3):
    for i in range(len(b3)):
        b1 = i
        for j in range(i + 1, len(b3)):
            if b3[b1] > b3[j]:
                b1 = j
        b3[i], b3[b1] = b3[b1], b3[i]
def fonk2(b3):
    for element in b3:
        print(element)
if b2 = = "__main__":
    b3 = [64, 25, 12, 22, 11]
    print("Original array:")
    fonk2(b3)
    fonk1(b3)
    print("Sorted array:")
    fonk2(b3)