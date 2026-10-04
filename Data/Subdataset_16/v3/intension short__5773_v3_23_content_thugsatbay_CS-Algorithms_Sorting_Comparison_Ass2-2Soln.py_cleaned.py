def fonk1(b9, start, b2):
    b1 = [(start, b2)]
    while b1:
        start, b2 = b1.pop()
        b3 = fonk2(b9, start, b2)
        if b3 - 1 > start:
            b1.append((start, b3 - 1))
        if b3 + 1 < b2:
            b1.append((b3 + 1, b2))
def fonk2(b9, start, b2):
    b4 = b9[b2]
    b5 = start - 1
    for j in range(start, b2):
        if b9[j] <= b4:
            b5 += 1
            b9[b5], b9[j] = b9[j], b9[b5]
    b9[b5 + 1], b9[b2] = b9[b2], b9[b5 + 1]
    return b5 + 1
def fonk3(b9):
    fonk1(b9, 0, len(b9) - 1)
    for b5 in range(len(b9)):
        b6 = len(b9) - b5
        if b9[b5] == b6:
            print(b9[b5])
            return
        elif b9[b5] > b6:
            print(b6 - 1)
            return
    print(len(b9))
def fonk4():
    b7 = int(input("Enter the value of b7: ").strip())
    b8 = input("Enter array in the format {1,2,3}: ").strip()[1:-1]
    b9 = list(map(int, b8.split(',')))
    if len(b9) == b7:
        fonk3(b9)
    else:
        print("The value of b7 and the size of the array don't match. Please validate your input.")
if b10 = = "__main__":
    fonk4()