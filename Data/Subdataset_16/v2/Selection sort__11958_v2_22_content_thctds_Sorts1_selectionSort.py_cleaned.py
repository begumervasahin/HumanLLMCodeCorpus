def fonk1(b4):
    b1 = len(b4)
    for i in range(b1):
        b2 = i
        for j in range(i + 1, b1):
            if b4[j] < b4[b2]:
                b2 = j
        b4[i, b4[b2]] = b4[b2], b4[i]
    return b4
def fonk2():
    b3 = int(input("Enter the number of elements: "))
    b4 = []
    print("Enter the elements:")
    for _ in range(b3):
        b5 = int(input("Element: "))
        b4.append(b5)
    print("Original array:", b4)
    b6 = fonk1(b4)
    print("Sorted array:", b6)
if b7 = = "__main__":
    fonk2()