def fonk1(b8, start, b2):
    b1 = [(start, b2)]
    while b1:
        start, b2 = b1.pop()
        b3 = fonk2(b8, start, b2)
        if b3 - 1 > start:
            b1.append((start, b3 - 1))
        if b3 + 1 < b2:
            b1.append((b3 + 1, b2))
def fonk2(b8, start, b2):
    b4 = b8[b2]
    b5 = start - 1
    for j in range(start, b2):
        if b8[j] <= b4:
            b5 += 1
            b8[b5], b8[j] = b8[j], b8[b5]
    b8[b5 + 1], b8[b2] = b8[b2], b8[b5 + 1]
    return b5 + 1
def fonk3(b8):
    fonk1(b8, 0, len(b8) - 1)
    for b5 in range(len(b8)):
        if b8[b5] == len(b8) - b5:
            print(b8[b5])
            return
        elif b8[b5] > len(b8) - b5:
            print(len(b8) - b5 - 1)
            return
    print(len(b8))
def fonk4():
    b6 = int(input("Enter the value of b6: ").strip())
    b7 = input("Enter array: [Example: {1,2,3}]: ").strip()[1:-1]
    b8 = list(map(int, b7.split(',')))
    if len(b8) == b6:
        fonk3(b8)
    else:
        print("N and array size don't match. Validate your input. Exiting program.")
if b9 = = "__main__":
    fonk4()